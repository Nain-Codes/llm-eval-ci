# tool-exec-service

A small, production-style **tool execution service** for running allowed developer tools (e.g., `pytest`) in a controlled subprocess.
It emphasizes reproducibility and operational hygiene:

- **Dockerized build**
- **GitHub Actions** pipeline (unit tests, integration run, report artifact)
- Minimal **HTTP API** (FastAPI) to trigger executions programmatically
- Strict **allowlist** for tools to prevent unsafe execution
- A real **workspace/** with a unit-tested utility to demonstrate end-to-end behavior

## Local usage
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e .
pytest -q
python -m src.run_once --task pytest --path workspace --out artifacts/report.md
cat artifacts/report.md
```

## API (optional)
```bash
uvicorn src.app:app --reload
# POST http://127.0.0.1:8000/run with JSON: {"task":"pytest","path":"workspace"}
```

## Docker
```bash
docker build -t tool-exec-service:latest .
docker run --rm -p 8000:8000 tool-exec-service:latest
```
