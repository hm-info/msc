# MSC Manual

## 📖 Documentation

<https://hm-info.github.io/msc/>

## NR-series job files

- [Türkçe — NR241 / NR242 / NR210](https://hm-info.github.io/msc/nr_job_file_tr.html)
- [English — NR241 / NR242 / NR210](https://hm-info.github.io/msc/nr_job_file_en.html)

The guide documents the 30-column NR job-file layout and the 18-character `nccode` operation blocks: `H` + 3-digit Tool + 2-digit Operation + 2-digit Accessory + 5-digit Position + 5-digit Slot Length. The downloadable CSV uses fictitious customer and order information.

Every Turkish and English guide includes a PDF download. PDFs are generated automatically from the same Markdown during each build and are not committed to the source branch.

Documentation check: `pip install -r requirements.txt` then `mkdocs build --strict`. PDF generation requires Pango, HarfBuzz Subset and DejaVu fonts; the Ubuntu packages are listed in the publishing workflow. Updates to `main` are published automatically through the existing GitHub Pages workflow.
