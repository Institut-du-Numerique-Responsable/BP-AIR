# air-fiches — Architecture Informatique Responsable

Espace de travail collaboratif du **Groupe de Travail AIR** (INR / ISIT) pour co-écrire les fiches de bonnes pratiques.

- **Source** : Markdown, une fiche = un fichier dans `docs/fiches/`.
- **Rendu** : site web généré automatiquement (MkDocs Material) et publié sur GitHub Pages à chaque modification validée. **Aucune mise en forme manuelle** — le Markdown *est* le site.
- **Contexte partagé** : le [guide unifié](docs/guide-unifie.md) (fondations théoriques).

## Structure

```
air-fiches/
├── docs/
│   ├── index.md              # page d'accueil du site
│   ├── guide-unifie.md       # fondations théoriques
│   └── fiches/               # une fiche = un fichier .md
├── TEMPLATE-fiche.md         # modèle à copier pour une nouvelle fiche
├── mkdocs.yml                # config du site (nav par thème)
├── requirements.txt          # dépendance : mkdocs-material
├── CONTRIBUTING.md           # comment co-écrire
└── .github/workflows/        # build & déploiement automatiques
```

## Les 13 fiches, par thème

| Code | Thème | Fiche |
|---|---|---|
| G1–G4 | Gouvernance & Stratégie | Mandat · Parties prenantes · Objectifs & ODD · Feuille de route |
| M1–M2 | Mesure & Diagnostic | Diagnostic · Pilotage & KPI |
| C1–C2 | Conception sobre | Éco-conception des services · Cycle de vie des données |
| I1–I2 | Infrastructure & Matériel | Infrastructures & environnements · Achats responsables |
| V1 | Chaîne de valeur | Maturité des parties prenantes |
| D1–D2 | Déploiement & Valorisation | Conformité · Communiquer & valoriser |

## Prévisualiser en local (optionnel)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve          # http://127.0.0.1:8000
```

## Contribuer

Voir [CONTRIBUTING.md](CONTRIBUTING.md). En bref : éditer le `.md` de la fiche (sur GitHub via le bouton crayon ou la touche `.`), ouvrir une *Pull Request*, faire relire. Le site se met à jour tout seul après le *merge*.
