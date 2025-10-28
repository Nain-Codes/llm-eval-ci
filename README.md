# tool-exec-service
![CI](https://github.com/Nain-Codes/tool-exec-service/actions/workflows/ci.yml/badge.svg)

Tool Exec Service is a lightweight, production-style execution framework that safely runs developer tools like pytest in controlled environments. It focuses on reproducibility, Dockerized builds, and GitHub Actions automation, demonstrating clean DevOps and ML engineering practices for real-world agent and LLM infrastructure.

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
**Tech Stack:** Python · FastAPI · Docker · GitHub Actions · Pytest · CI/CD · Infrastructure-as-Code principles
