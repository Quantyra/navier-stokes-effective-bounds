"""Build the manuscript twice; require a clean LaTeX reference/layout log."""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
out = ROOT / "output" / "pdf"
out.mkdir(parents=True, exist_ok=True)
exe = shutil.which("pdflatex")
if not exe:
    raise SystemExit("pdflatex is required; see README.md")
cmd = [exe, "-interaction=nonstopmode", "-halt-on-error", "-file-line-error",
       "-jobname=effective-bounds", f"-output-directory={out}",
       str(ROOT / "manuscript" / "main.tex")]
for run in range(2):
    result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, errors="replace")
    if result.returncode:
        print(result.stdout[-12000:])
        print(result.stderr)
        raise SystemExit(result.returncode)
log = (out / "effective-bounds.log").read_text(errors="replace")
for forbidden in ("Overfull", "undefined references", "undefined citations", "Rerun to get cross-references right"):
    if forbidden in log:
        raise SystemExit(f"LaTeX quality check failed: {forbidden}. Inspect {out / 'effective-bounds.log'}")
print("PASS: two-pass PDF build; no overfull boxes or unresolved references.")
