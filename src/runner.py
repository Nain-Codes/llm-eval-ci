import subprocess, shlex, time
from pathlib import Path

# Allowlist of safe developer tools. Extend as needed.
ALLOWED = {
    "pytest": "pytest -q"
}

def run_task(task: str, project_path: Path, out_path: Path):
    if task not in ALLOWED:
        return False, f"Task '{task}' not allowed. Allowed: {list(ALLOWED)}"
    if not project_path.exists():
        return False, f"Path not found: {project_path}"

    cmd = ALLOWED[task]
    start = time.time()
    try:
        proc = subprocess.run(
            shlex.split(cmd),
            cwd=str(project_path),
            capture_output=True,
            text=True,
            timeout=60
        )
        duration = time.time() - start
    except subprocess.TimeoutExpired:
        return False, "Timed out"

    success = proc.returncode == 0
    out_path.parent.mkdir(parents=True, exist_ok=True)
    report = [
        "# Execution Report",
        f"- Task: {task}",
        f"- Path: {project_path}",
        f"- Duration: {duration:.2f}s",
        f"- Exit code: {proc.returncode}",
        "",
        "## STDOUT",
        "```",
        proc.stdout.strip(),
        "```",
        "",
        "## STDERR",
        "```",
        proc.stderr.strip(),
        "```"
    ]
    out_path.write_text("\\n".join(report))
    return success, f"{'PASS' if success else 'FAIL'} in {duration:.2f}s"
