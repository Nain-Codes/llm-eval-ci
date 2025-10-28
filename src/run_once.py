import argparse
from pathlib import Path
from .runner import run_task

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True, help="Allowed: pytest")
    ap.add_argument("--path", required=True, help="Target project path")
    ap.add_argument("--out", default="artifacts/report.md", help="Report path")
    args = ap.parse_args()

    ok, summary = run_task(args.task, Path(args.path), Path(args.out))
    print(summary)
    raise SystemExit(0 if ok else 1)

if __name__ == "__main__":
    main()
