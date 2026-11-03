# MSC Manual

Topic navigation: Getting started → Job files → NR241 / NR242 / NR210, SC220-40 / SC220-80; Machine settings → Profile definitions, Macro mapping, End milling settings. The Turkish home page is `index.html`; the English home page is `home-en.html`. The header language switch opens the same topic in the other language. Existing guide URLs remain valid.

Konu menüsü: Başlangıç → İş dosyaları → NR241 / NR242 / NR210, SC220-40 / SC220-80; Makine ayarları → Profil tanımları, Makro eşleştirme, Kertme ayarları. Üst dil seçimi açık konuyu korur. Ana sayfalar her dilde beş rehber kartı içerir; PDF indirme bağlantıları rehberlerin başındadır.

## 📖 Documentation

<https://hm-info.github.io/msc/>

## NR-series job files

- [Türkçe — NR241 / NR242 / NR210](https://hm-info.github.io/msc/nr_job_file_tr.html)
- [English — NR241 / NR242 / NR210](https://hm-info.github.io/msc/nr_job_file_en.html)

The guide documents the 30-column NR job-file layout and the 18-character `nccode` operation blocks: `H` + 3-digit Tool + 2-digit Operation + 2-digit Accessory + 5-digit Position + 5-digit Slot Length. The downloadable CSV uses fictitious customer and order information.

## SC220 job files

- [Türkçe — SC220-40 / SC220-80](https://hm-info.github.io/msc/sc220_job_file_tr.html)
- [English — SC220-40 / SC220-80](https://hm-info.github.io/msc/sc220_job_file_en.html)

SC220-40 / SC220-80 use the same 30-column layout as NR241; only the `nccode` block differs: `H` + 2-digit Tool + 2-digit Operation + 2-digit Accessory + 5-digit Position (12 characters, no slot length).

Every Turkish and English guide includes a PDF download. PDFs are generated automatically from the same Markdown during each build and are not committed to the source branch.

Documentation check: `pip install -r requirements.txt` then `mkdocs build --strict`. PDF generation requires Pango, HarfBuzz Subset and DejaVu fonts; the Ubuntu packages are listed in the publishing workflow. Updates to `main` are published automatically through the existing GitHub Pages workflow.
