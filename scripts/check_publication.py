"""Exact numerical consistency and snapshot checks, not an analytic proof."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
assert 5 + 2 * F(5, 4) < 8
assert F(1, 2) * 4 * 8 == 16
assert F(1, 2) * 32 * 8 == 128
assert 10 * 16 + 6 * 128 == 928
assert 256 * 486 == 124416
assert 80 * 256 == 20480
assert 80 * 80 * 9 == 57600
assert F(1, 1) / (1 - F(41, 200)) < F(4, 3)
assert F(1, 4) - F(4, 3) * F(1, 16) == F(1, 6)
t = F(41, 20)
cubic = 1 - t / 2 + t*t / 12 - t**3 / 144
assert cubic == F(305719, 1152000) and cubic > F(1, 4)
# Universal algebra behind the selection rule: for V>=1 and N,L>=0,
# V*N/(2*8*V*(N+L+1)) = N/(16*(N+L+1)) <= 1/16.
assert F(1, 2*8) == F(1, 16)
data = json.loads((ROOT / "evidence/provenance.json").read_text(encoding="utf-8"))
for item in data["files"]:
    payload = (ROOT / item["path"]).read_bytes()
    assert hashlib.sha256(payload).hexdigest() == item["sha256"], item["path"]
meta = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
assert meta["creators"] == [{"name": "Fredriksen, Daniel", "affiliation": "Quantyra"}]
assert meta["publication_type"] == "preprint"
assert "doi" not in meta
print("PASS: exact pressure/contraction arithmetic, seven snapshot hashes, and publication metadata.")
print("NOT VERIFIED: the analytic proof, source PDE theorem, global field, novelty, or bit complexity.")
