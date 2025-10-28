import argparse
from pathlib import Path
import json
from typing import List, Dict
import pandas as pd
from src.metrics import compute_metrics, confusion_to_markdown
from src.backends.sklearn_backend import SklearnBackend
from src.backends.hf_backend import HFBackend

def load_jsonl(path: Path) -> pd.DataFrame:
    rows = []
    for line in path.read_text().splitlines():
        if line.strip():
            rows.append(json.loads(line))
    df = pd.DataFrame(rows)
    if not {"text","label"}.issubset(df.columns):
        raise ValueError("Dataset must contain 'text' and 'label' columns.")
    return df

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=["sklearn", "hf"], required=True)
    ap.add_argument("--data", type=str, required=True)
    ap.add_argument("--outdir", type=str, default="artifacts")
    args = ap.parse_args()

    data_path = Path(args.data)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    df = load_jsonl(data_path)
    texts: List[str] = df["text"].tolist()
    labels: List[int] = df["label"].astype(int).tolist()

    if args.backend == "sklearn":
        model = SklearnBackend()
    else:
        model = HFBackend()

    preds = model.predict(texts)
    metrics = compute_metrics(labels, preds)
    metrics_path = outdir/"metrics.json"
    metrics_path.write_text(json.dumps(metrics, indent=2))

    report_md = ["# Evaluation Report",
                 f"- Backend: **{args.backend}**",
                 f"- Samples: **{len(labels)}**",
                 "",
                 "## Metrics",
                 f"- Accuracy: {metrics['accuracy']:.3f}",
                 f"- Precision: {metrics['precision']:.3f}",
                 f"- Recall: {metrics['recall']:.3f}",
                 f"- F1: {metrics['f1']:.3f}",
                 "",
                 "## Confusion Matrix",
                 confusion_to_markdown(metrics["confusion_matrix"])
                 ]
    (outdir/"report.md").write_text("\n".join(report_md))
    print(json.dumps(metrics))

if __name__ == "__main__":
    main()
