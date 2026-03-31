# REST_API

A collection of Python projects exploring REST API development, async programming, data processing with Polars, and GitHub API integration.

---

## 📁 Project Structure

### `REST_API_Server/`
A **Flask-based REST API** with an Excel (`drink_database.xlsx`) backend for managing a drinks database.
- `application.py` — Core Flask app with full CRUD endpoints:
  - `GET /drinks` — Retrieve all drinks
  - `GET /drinks/<id>` — Retrieve a drink by ID
  - `POST /drinks` — Add a new drink (JSON body)
  - `GET /drinks/add/<name>/<description>` — Add a drink via URL (quick test)
  - `DELETE /drinks/<id>` — Delete a drink by ID
- `drink_database.xlsx` — Persistent Excel-based data store
- `requirements.txt` — Python dependencies (Flask, openpyxl, requests, SQLAlchemy, etc.)

---

### `REST_API_CLIENT/`
A **REST API client** for consuming external APIs.
- `test.py` — Fetches and prints active questions from the Stack Overflow API using `requests`
- `copilot_content.ipynb` — Jupyter Notebook for exploring API client interactions

---

### `asynch_polars/`
Demos for **asynchronous Python** and **Polars** data processing.
- `breakfast_maker_async.py` — Demonstrates `asyncio` concurrency using a breakfast-making analogy (`asyncio.gather` vs `asyncio.create_task`)
- `asynch.ipynb` — Notebook version of async programming examples
- `polars.ipynb` — Notebook exploring the Polars DataFrame library

---

### `github_info_collector/`
Tools for **collecting data from the GitHub API**.
- `access_github_info.py` — Script for accessing GitHub API (work in progress)
- `test.ipynb` — Jupyter Notebook for interactively exploring GitHub API responses

> ⚠️ **Note:** Never hardcode API tokens. Use environment variables or a `.env` file to store secrets securely.

---

## 🚀 Getting Started

1. Install dependencies for the server:
   ```bash
   cd REST_API_Server
   pip install -r requirements.txt
   ```
2. Run the Flask server:
   ```bash
   python application.py
   ```
3. Access the API at `http://localhost:5000/drinks`
This Repo has some practice projects and concept explanations for REST APIs, their usage, building web endpoints . The functionality and theory of polars and asyncio have also been explored.
