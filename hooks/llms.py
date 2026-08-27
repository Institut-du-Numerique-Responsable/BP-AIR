"""Génère llms.txt et llms-full.txt au build.

Deux fichiers, deux usages (spec llmstxt.org) :
  - llms.txt      : index navigable — un lien + une phrase par page.
  - llms-full.txt : le corpus complet en un seul fichier, pour qu'un assistant
                    puisse citer le guide sans parcourir 15 URLs.

Les deux sont dérivés du contenu réel : aucune liste à maintenir à la main, donc
aucune dérive possible entre le site et ce que lisent les assistants.
"""

import os
import re

HEADER = """# {site_name}

> {site_description}

{intro}

## Publié par

Institut du Numérique Responsable (INR), association loi 1901 créée en 2018 —
https://institutnr.org — avec ISIT Belgique (https://isit-be.org) et ISIT Suisse
(https://isit-ch.org). Travaux du Groupe de Travail Architecture Informatique
Responsable (AIR).

Licence : CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0/).
Attribution et partage dans les mêmes conditions obligatoires, y compris pour
les reprises par des systèmes d'IA.

Citation : voir CITATION.cff — https://github.com/Institut-du-Numerique-Responsable/BP-AIR/blob/main/CITATION.cff
Contributeurs : {site_url}contributeurs/
"""

INTRO = (
    "Deux niveaux de lecture. Le **guide** pose les fondations : six piliers, matrice "
    "de décision de l'architecte, équation de Kaya appliquée au SI, alignement sur les "
    "ODD. Les **fiches** décrivent chacune un chantier opérationnel selon une trame "
    "constante — objectif, contexte, étapes, KPI, pièges courants, outils.\n\n"
    "Les fiches sont codées par thème : G (gouvernance), M (mesure), C (conception "
    "sobre), I (infrastructure), V (chaîne de valeur), D (déploiement). Sauf mention "
    "contraire, elles sont en statut brouillon : documents de travail publiés en "
    "transparence avant validation par le groupe de travail."
)


def _strip_md(text):
    """Retire le frontmatter et les artefacts de rendu, garde le texte utile."""
    text = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"<figure markdown>.*?</figure>", "", text, flags=re.S)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def on_post_build(config, **kwargs):
    site_url = config["site_url"] or ""
    pages = []
    for root, _dirs, files in os.walk(config["docs_dir"]):
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            path = os.path.join(root, name)
            rel = os.path.relpath(path, config["docs_dir"])
            raw = open(path, encoding="utf-8").read()

            meta = {}
            fm = re.match(r"\A---\n(.*?)\n---\n", raw, flags=re.S)
            if fm:
                for key in ("titre", "description", "theme", "id", "statut"):
                    m = re.search(
                        rf"^{key}:\s*(?:>-\s*\n\s+)?(.+?)$", fm.group(1), flags=re.M
                    )
                    if m:
                        meta[key] = m.group(1).strip().strip('"')

            title = meta.get("titre")
            if not title:
                h1 = re.search(r"^#\s+(.+)$", raw, flags=re.M)
                title = h1.group(1).strip() if h1 else rel
            if meta.get("id"):
                title = f"{meta['id']} — {title}"

            slug = rel[:-3]
            url = site_url + ("" if slug == "index" else slug + "/")
            pages.append(
                {
                    "title": title,
                    "url": url,
                    "desc": meta.get("description", ""),
                    "theme": meta.get("theme", ""),
                    "statut": meta.get("statut", ""),
                    "body": _strip_md(raw),
                    "rel": rel,
                }
            )

    pages.sort(key=lambda p: (p["rel"] != "index.md", p["rel"]))

    # --- llms.txt : index
    out = [
        HEADER.format(
            site_name=config["site_name"],
            site_description=config["site_description"],
            intro=INTRO,
            site_url=site_url,
        ),
        "## Pages",
        "",
    ]
    for p in pages:
        line = f"- [{p['title']}]({p['url']})"
        if p["desc"]:
            line += f": {p['desc']}"
        out.append(line)
    out += [
        "",
        "## Code source",
        "",
        "- [Dépôt GitHub](https://github.com/Institut-du-Numerique-Responsable/BP-AIR): sources Markdown, historique et contributions.",
        f"- [Corpus complet]({site_url}llms-full.txt): l'intégralité du guide et des fiches en un seul fichier.",
        "",
    ]
    with open(os.path.join(config["site_dir"], "llms.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    # --- llms-full.txt : corpus
    full = [
        f"# {config['site_name']} — corpus complet",
        "",
        f"> {config['site_description']}",
        "",
        f"Source : {site_url}",
        "Licence : CC BY-SA 4.0 — attribution « Institut du Numérique Responsable / ISIT — GT AIR » requise.",
        "",
        "---",
        "",
    ]
    for p in pages:
        full += [f"<!-- source: {p['url']} -->", "", p["body"], "", "---", ""]
    with open(
        os.path.join(config["site_dir"], "llms-full.txt"), "w", encoding="utf-8"
    ) as fh:
        fh.write("\n".join(full))

    print(f"INFO    -  llms.txt / llms-full.txt générés ({len(pages)} pages)")
