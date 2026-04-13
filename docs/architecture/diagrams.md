# Architecture Diagrams

## Logical Architecture

```mermaid
flowchart LR
    Browser[Student or Teacher Browser]
    WebApp[Web App\nFlask + Jinja]
    AuthService[Auth Service]
    CatalogService[Catalog Service]
    CirculationService[Circulation Service]
    SQLite[(SQLite Database)]

    Browser --> WebApp
    WebApp --> AuthService
    WebApp --> CatalogService
    WebApp --> CirculationService
    AuthService --> SQLite
    CatalogService --> SQLite
    CirculationService --> SQLite
```

## Deployment Architecture

```mermaid
flowchart TD
    Host[Host Computer]
    VBox[VirtualBox]
    Ubuntu[Ubuntu VM]
    Repo[Git Repository]
    App[Flask Application]
    DB[(SQLite Database)]
    Browser[Firefox or Chromium]

    Host --> VBox
    VBox --> Ubuntu
    Ubuntu --> Repo
    Repo --> App
    App --> DB
    Browser --> App
```

## Explanation

- The browser interacts only with the Flask web application.
- The web application stays thin and delegates operations to small service modules.
- Each service owns a narrow responsibility.
- SQLite keeps deployment simple enough for a school seminar and Ubuntu VM demo.
