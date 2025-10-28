# llm-eval-real

A **real, production-style evaluation project** for text classification (sentiment). It includes:

- **Two model backends**:
  - **Transformers (DistilBERT)** for a *real* LLM-style pipeline
  - **Scikit-learn** fast fallback for CI (no GPU, tiny deps)
- **Reproducible eval CLI** that loads a dataset, predicts, and computes metrics:
  - Accuracy, precision, recall, F1, confusion matrix
- **Artifacts**: `metrics.json` + `report.md`
- **GitHub Actions** that run tests + fast evaluation on every push
  - A **manual workflow** can run the full Transformers backend
- **Dockerfile** and **Makefile** for consistent local runs
- Clean, original code with type hints, tests, and documentation

## Quickstart (local)

### Option A — Run real Transformers backend (requires Internet on first run to fetch the model)
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
python -m src.eval_cli --backend hf --data src/data/sentiment_dev.jsonl --outdir artifacts
cat artifacts/metrics.json
```

### Option B — Fast scikit-learn backend
```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
python -m src.eval_cli --backend sklearn --data src/data/sentiment_dev.jsonl --outdir artifacts
```

## Docker
```bash
docker build -t llm-eval-real:latest .
docker run --rm -v "$PWD":/app llm-eval-real:latest   python -m src.eval_cli --backend sklearn --data src/data/sentiment_dev.jsonl --outdir artifacts
```

## GitHub Actions
- Default CI uses the **sklearn** backend (lightweight).
- A manual **workflow_dispatch** job runs the **Transformers** backend (heavier).

License: MIT
