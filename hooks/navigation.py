"""Show a topic tree in the current language and preserve the topic on switching."""

from copy import copy

from mkdocs.structure.nav import Navigation, Section


PAIRS = (
    ("index.md", "home-en.md"),
    ("nr_job_file_tr.md", "nr_job_file_en.md"),
    ("profile_definitions_tr.md", "profile_definitions_en.md"),
    ("macro_mapping_tr.md", "macro_mapping_en.md"),
    ("endmilling_settings_tr.md", "endmilling_settings_en.md"),
)


def on_page_context(context, page, config, nav, **kwargs):
    source = page.file.src_uri
    pair = next((pair for pair in PAIRS if source in pair), PAIRS[0])
    english = source == pair[1]
    language = "en" if english else "tr"
    labels = (
        ("Getting started", "NR241 / NR242 / NR210", "Profile definitions",
         "Macro mapping", "End milling settings")
        if english else
        ("Başlangıç", "NR241 / NR242 / NR210", "Profil tanımları",
         "Makro eşleştirme", "Kertme ayarları")
    )
    sources = [item[1 if english else 0] for item in PAIRS]
    pages_by_source = {item.file.src_uri: item for item in nav.pages}
    pages = []
    for uri, title in zip(sources, labels):
        item = copy(pages_by_source[uri])
        item.parent = None
        item.title = title
        item.active = uri == source
        pages.append(item)

    sections = [
        Section("Job files" if english else "İş dosyaları", [pages[1]]),
        Section("Machine settings" if english else "Makine ayarları", pages[2:]),
    ]
    for section in sections:
        section.active = any(item.active for item in section.children)
        for item in section.children:
            item.parent = section
    localized_nav = Navigation([pages[0], *sections], pages)
    localized_nav.homepage = pages[0]

    local_config = copy(config)
    local_config["theme"] = copy(config["theme"])
    local_config["theme"]["language"] = language
    local_config["site_name"] = "MSC User Guide" if english else "MSC Kullanım Rehberi"
    local_config["site_description"] = (
        "Job files, profile definitions, macro mapping and end milling settings for MSC machines."
        if english else config["site_description"]
    )
    local_config["extra"] = dict(config["extra"])
    local_config["extra"]["homepage"] = pages[0].url
    local_config["extra"]["alternate"] = [
        {"name": "Türkçe", "lang": "tr", "link": pages_by_source[pair[0]].url},
        {"name": "English", "lang": "en", "link": pages_by_source[pair[1]].url},
    ]
    current = sources.index(source) if source in sources else 0
    local_page = pages[current]
    local_page.previous_page = pages[current - 1] if current else None
    local_page.next_page = pages[current + 1] if current < len(pages) - 1 else None
    context.update(config=local_config, nav=localized_nav, page=local_page)
    return context
