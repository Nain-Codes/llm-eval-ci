# llm-eval-ci (original, minimal)

A **fully original, tiny evaluation template** that simulates how you'd evaluate
reasoning tasks. It includes:

- A **toy dataset** (`src/data/math_grade_5.jsonl`)
- A **baseline "model"** (`src/model/baseline.py`) that solves simple math by parsing the question (no external LLMs)
- An **evaluator** that computes predictions and accuracy
- **GitHub Actions** CI that runs tests and generates an **evaluation report** artifact (`report.json`)
- **Dockerfile** and **Makefile** for reproducible runs

This demonstrates the exact skills in the job description: **reproducible environments, CI/CD, CLI tooling, data handling, and clear documentation** — without copying any upstream code.

> Later, you can plug in a real LLM (local or API) by implementing another model class with the same interface.

## Quickstart (local)

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
pytest -q
python -m src.runner --task-file src/data/math_grade_5.jsonl --out report.json
cat report.json
```

## Docker

```bash
docker build -t llm-eval-ci:orig .
docker run --rm -v "$PWD":/app llm-eval-ci:orig   python -m src.runner --task-file src/data/math_grade_5.jsonl --out report.json
```

## Extending (plug in your own model)
Create a new file like `src/model/my_llm.py` with a class that implements:
```python
class MyModel:
    def predict(self, question: str) -> str: ...
```
Then edit `src/runner.py` to import and use `MyModel`.

## Security
- No secrets or keys are required.
- If you add API models, pass keys via environment variables (never commit them).

## License
MIT
