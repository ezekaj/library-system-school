"""Export a Mermaid ERD from the SQLAlchemy metadata."""

from __future__ import annotations

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from shared.model_loader import load_models
from shared.database import Base


ENTITY_ORDER = ["users", "books", "loans"]
RELATIONSHIPS = [
    ("users", "||--o{", "loans", "issues"),
    ("books", "||--o{", "loans", "contains"),
]

TYPE_NAMES = {
    "INTEGER": "int",
    "VARCHAR": "string",
    "TEXT": "text",
    "BOOLEAN": "boolean",
    "DATETIME": "datetime",
}


def normalize_type_name(column_type: object) -> str:
    raw_name = column_type.__class__.__name__.upper()
    return TYPE_NAMES.get(raw_name, raw_name.lower())


def format_column_line(column) -> str:
    parts = [normalize_type_name(column.type), column.name]

    if column.primary_key:
        parts.append("PK")
    if column.foreign_keys:
        parts.append("FK")
    if not column.nullable and not column.primary_key:
        parts.append("required")

    return " ".join(parts)


def render_entity(table) -> list[str]:
    lines = [f"    {table.name} {{"]
    for column in table.columns:
        lines.append(f"        {format_column_line(column)}")
    lines.append("    }")
    return lines


def build_erd_markdown() -> str:
    load_models()

    lines = [
        "# Library System ERD",
        "",
        "This ERD is generated from the current SQLAlchemy models.",
        "",
        "```mermaid",
        "erDiagram",
    ]

    for table_name in ENTITY_ORDER:
        lines.extend(render_entity(Base.metadata.tables[table_name]))

    lines.append("")

    for left, relation, right, label in RELATIONSHIPS:
        lines.append(f"    {left} {relation} {right} : {label}")

    lines.extend(
        [
            "```",
            "",
            "## Notes",
            "",
            "- `users` stores admin accounts.",
            "- `books` stores catalog metadata and available inventory.",
            "- `loans` stores each issue and return transaction.",
        ]
    )

    return "\n".join(lines) + "\n"


def main() -> None:
    output_path = PROJECT_ROOT / "docs" / "erd" / "library-system-erd.md"
    output_path.write_text(build_erd_markdown(), encoding="utf-8")
    print(f"ERD written to {output_path}")


if __name__ == "__main__":
    main()
