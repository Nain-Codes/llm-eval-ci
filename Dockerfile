FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir -e .

CMD ["python", "-m", "src.eval_cli", "--backend", "sklearn", "--data", "src/data/sentiment_dev.jsonl", "--outdir", "artifacts"]
