# Explicit pressure and local contraction bounds

A research note giving explicit sufficient constants for the pressure datum and leading local analytic axis problem in the September 2026 forced Navier–Stokes construction attributed to OpenAI.

**[Read the manuscript (PDF)](output/pdf/effective-bounds.pdf)** · [LaTeX source](manuscript/main.tex) · [Claims and review status](INTEGRITY.md) · [Provenance](evidence/provenance.json)

## Results

- Pressure majorants `P0 = 16 Pbar²` and `P1 = 128 Pbar²` on a fixed complex rectangle, conditional on the stated radial envelope.
- An explicit complex tube and weighted coefficient bounds for the leading axis problem.
- A noncircular `Lambda`-then-`C` choice giving displacement and contraction factor at most `1/16`, and real normalized angular profile at least `1/6` on `0 ≤ Y ≤ 4.1`.

The source already contains the local contraction method. This note makes sufficient bounds and dependencies explicit. It does not certify globally admissible outer data or the completed velocity field. It is not a fluid computer, a SAT algorithm, or a complexity result. Novelty has not been independently established.

## Reproduce the checks and PDF

Requires Python 3 (standard library only for checks) and a LaTeX installation containing `pdflatex`, `amsmath`, `amsthm`, `booktabs`, `lmodern`, `geometry`, `hyperref`, and `microtype`.

```text
python scripts/check_source_coefficient_majorants.py
python scripts/check_publication.py
python scripts/build.py
```

The arithmetic checks support the written arguments; they do not formally verify the analytic theorem. The build runs LaTeX twice and rejects unresolved references and overfull boxes. The PDF has also been rendered for visual inspection.

## Publication and citation

Author: **Daniel Fredriksen**, Quantyra. Prepared with OpenAI Codex assistance; see the manuscript disclosure. Version **0.1.0**. License: **Apache-2.0**, preserving the source repository's license.

Published Figshare record: **[10.6084/m9.figshare.33472651](https://doi.org/10.6084/m9.figshare.33472651)**. Cite the archived files as version 2: **[10.6084/m9.figshare.33472651.v2](https://doi.org/10.6084/m9.figshare.33472651.v2)**.

Figshare version 2 stores the manuscript PDF and a source ZIP of commit `35b102c2ea7b47aef091f232132f81d69e68348c`. Both public downloads were verified: the PDF is byte-identical to the manuscript, and all ZIP entries match that commit. Later citation/status updates on GitHub are outside that frozen snapshot. See [the publication receipt](evidence/figshare-publication.json) and [API workflow](FIGSHARE.md). Version 1 was a link-only record. No GitHub release or Zenodo deposit has been created.

**Future GitHub releases automatically publish a corresponding Figshare version.** The release workflow builds and verifies the manuscript and source archive, publishes them, and attaches a DOI receipt to the GitHub release. Ordinary commits do not publish. See [release behavior and retry handling](FIGSHARE.md#automatic-github-releases).

## Evidence

The `evidence/` directory preserves seven original research/review records byte for byte from a fixed source commit. These are historical supporting records, not additional publication claims. Their old workstream labels and references to other research notes are retained for provenance; only the three mathematical records listed in [the evidence guide](evidence/README.md) are dependencies of this note.

The external manuscript is cited and checksummed, not redistributed. No active source worktree or parent research task is part of this publication repository.
