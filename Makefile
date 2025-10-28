.PHONY: dev test run docker clean

dev:
	python -m venv .venv && . .venv/bin/activate && pip install -e .

test:
	pytest -q

run:
	python -m src.runner --task-file src/data/math_grade_5.jsonl --out report.json

docker:
	docker build -t llm-eval-ci:orig .
	docker run --rm -v $(PWD):/app llm-eval-ci:orig python -m src.runner --task-file src/data/math_grade_5.jsonl --out report.json

clean:
	rm -f report.json
	rm -rf .venv
