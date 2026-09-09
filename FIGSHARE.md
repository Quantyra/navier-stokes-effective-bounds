# Figshare publication and API upload

Published record: https://doi.org/10.6084/m9.figshare.33472651

**Version 2 is published:** https://doi.org/10.6084/m9.figshare.33472651.v2 . It stores the 414,160-byte manuscript PDF and a 443,954-byte ZIP of commit `35b102c2ea7b47aef091f232132f81d69e68348c`. Public download checks verified both MD5 values, exact PDF bytes, and the content of every ZIP entry against that commit. The author is Daniel Fredriksen and the license is Apache 2.0. The publication receipt is `evidence/figshare-publication.json`.

Version 1 was a link-only record. The API upload replaced that link in the editable draft. After checksum verification, a separate authenticated publish operation created version 2 on September 9, 2026 UTC (September 8 local time). The reusable workflow itself remains upload-only.

## Connect the upload workflow

1. In Figshare, open your avatar menu, **Integrations**, then **Personal Tokens → Create personal token**. Use a descriptive name such as `Quantyra bounds GitHub upload`.
2. Save that token as a repository Actions secret named `FIGSHARE_TOKEN`: https://github.com/Quantyra/navier-stokes-effective-bounds/settings/secrets/actions/new . Do not put it in chat, code, a workflow input, or a public issue.
3. Run the **Upload files to Figshare draft** workflow from GitHub Actions. It targets only item `33472651` and uploads the existing manuscript PDF plus a ZIP from the workflow's exact git commit. It checks the title and license, verifies file sizes and MD5 checksums, and skips already-complete identical files on retries. Figshare rejects mixed link/file items, so the workflow replaces only the known link-only entry `68331139` pointing at this repository in the editable draft. It refuses any other link arrangement, leaves public version 1 intact, and does not change metadata or publish.
4. Inspect the resulting draft in Figshare and publish its updated version. Then verify that the public record actually lists downloadable files and update the preferred citation to the resulting version DOI.

The workflow is manual rather than automatically triggered by every push. Figshare's repository-picker auto-sync does not govern these API uploads. The first successful authenticated upload was Actions run `34308796506`. A token is stored as the `FIGSHARE_TOKEN` Actions secret. Because the original token was shared in chat, replace it through GitHub Secrets and revoke the old token in Figshare after the completed transfer.

## Verification

Run `python scripts/test_figshare_upload.py` for mocked upload, retry, and checksum tests. No credentials or network access are needed for these tests. The live transfer and separate publication completed successfully, and the public downloads were independently verified. ZIP compression can differ between git implementations; snapshot verification compared every uncompressed entry as well as Figshare's supplied/computed archive MD5.

API reference: https://docs.figshare.com/v2/
Token instructions: https://info.figshare.com/user-guide/how-to-get-a-personal-token/
