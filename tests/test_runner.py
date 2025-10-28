from pathlib import Path
from src.runner import run_task

def test_disallow():
    ok, msg = run_task("bash", Path("."), Path("artifacts/report.md"))
    assert not ok and "not allowed" in msg

def test_missing_path(tmp_path):
    ok, msg = run_task("pytest", tmp_path / "missing", tmp_path / "report.md")
    assert not ok and "Path not found" in msg
