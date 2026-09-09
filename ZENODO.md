# Zenodo handoff

The repository is ready to connect to Zenodo. No DOI is reserved here and no GitHub release has been created.

1. Sign into Zenodo and open the GitHub integration settings.
2. Make this repository visible to the integration under the Quantyra organization, then enable `Quantyra/navier-stokes-effective-bounds`.
3. After integration is enabled, publish a GitHub release for the reviewed repository snapshot. The first proposed tag is `v0.1.0`.
4. Verify the resulting Zenodo record, especially author, title, preprint type, license, and the presence of `output/pdf/effective-bounds.pdf` in the archived sources.
5. Record the actual DOI in the citation metadata and README after Zenodo assigns it. Preserve the correspondence between each DOI and its archived release.

For a PDF-first record with the manuscript directly previewable rather than only inside a repository archive, a manual Zenodo manuscript deposit is an alternative. Upload the PDF and a supporting source archive, reserve a DOI in that draft if needed, and publish it. Avoid accidentally creating two records represented as the same publication without linking them appropriately.

The `.zenodo.json` file supplies title, author, license, description, and related repository metadata. There is intentionally no DOI field yet.

References: [Zenodo GitHub integration](https://help.zenodo.org/docs/github/), [reserve a DOI](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/).
