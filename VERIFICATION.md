# Publication preparation verification

Date: 2026-09-08

- Exact rational source-coefficient checks: **PASS**.
- Pressure, contraction, and comparison-polynomial arithmetic: **PASS**.
- All seven archived records match their fixed-source SHA-256 hashes: **PASS**.
- `CITATION.cff` validates against the official CFF 1.2.0 JSON schema: **PASS**. The repository is classified as software/supporting source; its preferred citation is the research article.
- `.zenodo.json` parses, identifies a preprint, and has no invented DOI: **PASS**.
- Two-pass `pdflatex` build: **PASS**, seven pages, no overfull boxes or unresolved references.
- Visual inspection of all seven rendered pages: **PASS**, including equations, tables, citations, margins, and page numbering.
- Original external manuscript retrieved and checksummed; not redistributed.

These are publication-preparation checks. They do not constitute independent human peer review, formal verification, validation of the external PDE theorem, or a novelty/priority determination. Historical mathematical review verdicts and their staffing limits are recorded in `INTEGRITY.md`.

Temporary source downloads, page renderings, LaTeX intermediates, and the local metadata-validation environment are ignored. All final manuscript, source, evidence, and metadata files are tracked.

Figshare version 2 follow-up: the authenticated API upload passed, the updated record was published, and both public files were downloaded and checked. PDF bytes match exactly; every ZIP entry matches archived commit `35b102c2ea7b47aef091f232132f81d69e68348c`. The version DOI and public metadata are recorded in `evidence/figshare-publication.json`. This publication adds no mathematical claim.
