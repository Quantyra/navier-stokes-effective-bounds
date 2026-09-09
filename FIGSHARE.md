# Figshare publication and API upload

Published record: https://doi.org/10.6084/m9.figshare.33472651

Version 1 is publicly accessible, with the expected title, Daniel Fredriksen as author, and Apache 2.0 license. Verification on September 8, 2026 (local time) found one link-only entry pointing at GitHub and no stored file bytes. A DOI-backed link record is not an archived repository snapshot.

## Connect the upload workflow

1. In Figshare, open your avatar menu, **Integrations**, then **Personal Tokens → Create personal token**. Use a descriptive name such as `Quantyra bounds GitHub upload`.
2. Save that token as a repository Actions secret named `FIGSHARE_TOKEN`: https://github.com/Quantyra/navier-stokes-effective-bounds/settings/secrets/actions/new . Do not put it in chat, code, a workflow input, or a public issue.
3. Run the **Upload files to Figshare draft** workflow from GitHub Actions. It targets only item `33472651` and uploads the existing manuscript PDF plus a ZIP from the workflow's exact git commit. It checks the title and license, verifies file sizes and MD5 checksums, and skips already-complete identical files on retries. Figshare rejects mixed link/file items, so the workflow replaces only the known link-only entry `68331139` pointing at this repository in the editable draft. It refuses any other link arrangement, leaves public version 1 intact, and does not change metadata or publish.
4. Inspect the resulting draft in Figshare and publish its updated version. Then verify that the public record actually lists downloadable files and update the preferred citation to the resulting version DOI.

The workflow is manual rather than automatically triggered by every push. Figshare's repository-picker auto-sync does not govern these API uploads. No token has been added or authenticated upload run by this preparation step.

## Verification

Run `python scripts/test_figshare_upload.py` for mocked upload, retry, and checksum tests. No credentials or network access are needed for these tests. The real authenticated transfer remains untested until the user supplies the secret.

API reference: https://docs.figshare.com/v2/
Token instructions: https://info.figshare.com/user-guide/how-to-get-a-personal-token/
