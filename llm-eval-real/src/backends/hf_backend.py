from typing import List
from transformers import pipeline

class HFBackend:
    """
    Uses Hugging Face transformers sentiment pipeline (DistilBERT fine-tuned on SST-2).
    Requires internet on first run to download weights.
    """
    def __init__(self) -> None:
        self.pipe = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def predict(self, texts: List[str]) -> List[int]:
        out = self.pipe(texts, truncation=True)
        labels = [1 if r["label"].upper().startswith("POS") else 0 for r in out]
        return labels
