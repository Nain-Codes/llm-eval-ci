FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir -e .

CMD ["python", "-m", "src.runner", "--task-file", "src/data/math_grade_5.jsonl", "--out", "report.json"]
