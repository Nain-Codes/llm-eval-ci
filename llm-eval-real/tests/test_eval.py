import json
from pathlib import Path
from src.eval_cli import load_jsonl
from src.metrics import compute_metrics

def test_dataset_loads():
    df = load_jsonl(Path("src/data/sentiment_dev.jsonl"))
    assert len(df) >= 10
    assert {"text","label"}.issubset(df.columns)

def test_metrics_shape():
    y_true = [0,1,1,0]
    y_pred = [0,1,0,0]
    m = compute_metrics(y_true, y_pred)
    assert set(m.keys()) == {"total","accuracy","precision","recall","f1","confusion_matrix"}
