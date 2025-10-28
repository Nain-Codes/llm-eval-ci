from typing import List, Dict
import numpy as np

def compute_metrics(y_true: List[int], y_pred: List[int]) -> Dict:
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    tp = int(((y_true==1) & (y_pred==1)).sum())
    tn = int(((y_true==0) & (y_pred==0)).sum())
    fp = int(((y_true==0) & (y_pred==1)).sum())
    fn = int(((y_true==1) & (y_pred==0)).sum())
    total = len(y_true)
    acc = (tp+tn)/max(total,1)
    prec = tp/max(tp+fp,1)
    rec = tp/max(tp+fn,1)
    f1 = 2*prec*rec/max(prec+rec,1e-9)
    return {
        "total": total,
        "accuracy": float(acc),
        "precision": float(prec),
        "recall": float(rec),
        "f1": float(f1),
        "confusion_matrix": [[tn, fp],[fn, tp]],
    }

def confusion_to_markdown(cm: List[List[int]]) -> str:
    tn, fp = cm[0]
    fn, tp = cm[1]
    lines = [
        "|      | Pred 0 | Pred 1 |",
        "|------|--------|--------|",
        f"| **True 0** | {tn} | {fp} |",
        f"| **True 1** | {fn} | {tp} |",
    ]
    return "\n".join(lines)
