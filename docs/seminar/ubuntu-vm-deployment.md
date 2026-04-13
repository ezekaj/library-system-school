# Ubuntu VM Deployment Guide

This guide is written for the seminar demo where the application is deployed inside an Ubuntu virtual machine.

## 1. Install Base Tools

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip git
```

## 2. Clone The Repository

```bash
git clone git@github.com:ezekaj/library-system-school.git
cd library-system-school
```

If SSH is not configured inside the VM:

```bash
git clone https://github.com/ezekaj/library-system-school.git
cd library-system-school
```

## 3. Create The Virtual Environment

```bash
python3 -m venv .venv
```

If the command fails with an `ensurepip` error:

```bash
sudo apt install -y python3-venv
python3 -m venv .venv
```

## 4. Install Project Dependencies

```bash
.venv/bin/pip install -r requirements.txt
```

## 5. Seed Demo Data

```bash
.venv/bin/python -m scripts.seed_demo
```

This creates:
- the SQLite database in `data/library.db`
- the default admin account
- sample books for the seminar demo

## 6. Start The Application

```bash
.venv/bin/python -m apps.web_app
```

Open the application in the VM browser:

```text
http://127.0.0.1:5000
```

## Default Login

- Email: `admin@library.local`
- Password: `admin123`

## Optional One-Step Bootstrap

```bash
chmod +x scripts/bootstrap_ubuntu.sh
./scripts/bootstrap_ubuntu.sh
```

## Screenshot Checklist For The Seminar

- VirtualBox VM overview
- Ubuntu desktop or terminal
- dependency installation
- seed script success message
- login page
- dashboard with books
- issue book screen/state
- return book result

## Common Errors And Fixes

### `python3 -m venv` fails

Cause: `python3-venv` package missing.

Fix:

```bash
sudo apt install -y python3-venv
```

### `Address already in use`

Cause: port `5000` is already occupied.

Fix:

```bash
.venv/bin/python -m flask --app apps.web_app run --port 5001
```

### Login works but there are no books

Cause: seed script was not run.

Fix:

```bash
.venv/bin/python -m scripts.seed_demo
```
