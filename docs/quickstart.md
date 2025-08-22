# SamrakshIQ Quickstart Guide

## Introduction
SamrakshIQ is an open-source SMS anonymization tool designed for global compliance with GDPR, HIPAA, and DPDP standards.

## Prerequisites
- Python 3.10+
- Node.js 18+
- Git
- Virtual environment (e.g., `venv`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/samrakshiq.git
   cd samrakshiq
   ```
2. Set up the backend:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Set up the frontend:
   ```bash
   cd src/ui
   npm install
   ```
4. Configure environment variables (e.g., API keys) in `.env` files (see `.env.example`).

## Running the Project
1. Start the backend:
   ```bash
   uvicorn src.api.main:app --reload
   ```
2. Start the frontend:
   ```bash
   cd src/ui
   npm run dev
   ```
3. Access the UI at `http://localhost:5173`.

## Usage
- Upload SMS data via the dashboard.
- Review anonymized messages and metrics.
- Export redacted data securely.

## Troubleshooting
- Ensure ports 8000 (backend) and 5173 (frontend) are free.
- Check logs in `src/api/logs/` for errors.

## Contributing
Fork the repo, create a branch, and submit a pull request. See `CONTRIBUTING.md` for details.