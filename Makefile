.PHONY: dev test eval-sklearn eval-hf docker clean

dev:
	python -m venv .venv && . .venv/bin/activate && pip install -e .

test:
	pytest -q

eval-sklearn:
	python -m src.eval_cli --backend sklearn --data src/data/sentiment_dev.jsonl --outdir artifacts

eval-hf:
	python -m src.eval_cli --backend hf --data src/data/sentiment_dev.jsonl --outdir artifacts

docker:
	docker build -t llm-eval-real:latest .
	docker run --rm -v $(PWD):/app llm-eval-real:latest python -m src.eval_cli --backend sklearn --data src/data/sentiment_dev.jsonl --outdir artifacts

clean:
	rm -rf artifacts
	rm -rf .venv
