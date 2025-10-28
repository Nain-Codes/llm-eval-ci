from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
from .runner import run_task

app = FastAPI()

class RunRequest(BaseModel):
    task: str
    path: str
    out: str | None = None

@app.post("/run")
def run(req: RunRequest):
    project_path = Path(req.path)
    out_path = Path(req.out) if req.out else Path("artifacts/report.md")
    ok, summary = run_task(req.task, project_path, out_path)
    return {"ok": ok, "summary": summary, "report": str(out_path)}
