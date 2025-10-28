from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

class SklearnBackend:
    """
    Trains a quick logistic regression on the provided eval data (holdout via simple split).
    For demonstration, we fit on a subset and predict on the remainder (not perfect science).
    This is fast and CI-friendly.
    """
    def __init__(self) -> None:
        self.pipe: Pipeline | None = None

    def predict(self, texts: List[str]) -> List[int]:
        n = len(texts)
        split = max(int(0.6*n), 1)
        train, test = texts[:split], texts[split:]

        # Fake labels for training: heuristic (contains "good"/"great" => 1 else 0)
        y_train = [1 if any(w in t.lower() for w in ["good","great","love","awesome","fantastic"]) else 0 for t in train]

        self.pipe = Pipeline([
            ("tfidf", TfidfVectorizer(max_features=5000)),
            ("clf", LogisticRegression(max_iter=100)),
        ])
        self.pipe.fit(train, y_train)

        if split == n:
            return [0]*n

        preds = self.pipe.predict(test).tolist()
        return ([0]*split) + preds
