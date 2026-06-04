# BP-AIR — Fiches de bonnes pratiques · Architecture Informatique Responsable

Espace de travail collaboratif du **Groupe de Travail AIR** (Institut du Numérique Responsable — INR / ISIT) pour **co-écrire** les fiches de bonnes pratiques et les **publier automatiquement** sous forme de site web.

🌐 **Site en ligne** : <https://institut-du-numerique-responsable.github.io/BP-AIR/>

---

## 1. Le principe en une phrase

Vous écrivez du **Markdown** (texte simple) dans ce dépôt → un robot le transforme en **site web** et le publie tout seul. **Aucune mise en forme manuelle**, aucun outil à installer pour contribuer.

---

## 2. Comment ça marche (architecture)

```
                 ┌─────────────────────────────────────────--─┐
   Vous éditez   │  Dépôt GitHub (les fichiers .md)           │
   une fiche  ──►│  docs/fiches/*.md  +  docs/guide-unifie.md │
                 └───────────────────┬─────────────────────--─┘
                                     │  push / merge sur "main"
                                     ▼
                 ┌──────────────────────────────--────────────┐
   Automatique   │  GitHub Actions (.github/workflows)        │
   (~30 s)       │  1. installe MkDocs Material               │
                 │  2. construit le site (HTML)               │
                 │  3. le déploie sur GitHub Pages            │
                 └───────────────────┬─────────────────--─────┘
                                     ▼
                 ┌───────────────────────────────────────-───┐
   Résultat      │  Site public, à jour                      │
                 │  institut-du-numerique-responsable        │
                 │       .github.io/BP-AIR/                  │
                 └────────────────────────────────────────-──┘
```

**Briques techniques :**

| Élément | Rôle |
|---|---|
| **Markdown** (`.md`) | Le contenu, écrit par le GT. Source unique de vérité. |
| **MkDocs** + thème **Material** | Moteur qui transforme le Markdown en site (menu, recherche, thème clair/sombre). |
| **`mkdocs.yml`** | Configuration : titre, navigation par thème, options. |
| **GitHub Actions** (`.github/workflows/deploy.yml`) | Construit et déploie le site à chaque modification de `main`. |
| **GitHub Pages** | Héberge le site public gratuitement. |

> Personne n'a besoin de comprendre cette mécanique pour contribuer. Elle tourne seule.

---

## 3. Structure du dépôt

```
BP-AIR/
├── docs/                       # tout le contenu du site
│   ├── index.md                # page d'accueil
│   ├── guide-unifie.md         # fondations théoriques (6 piliers, matrice, outils, glossaire)
│   ├── assets/
│   │   ├── img/                # illustrations et schémas
│   │   └── extra.css           # styles (figures, zoom)
│   └── fiches/                 # une fiche = un fichier .md
│       ├── G1-mandat.md
│       ├── ...
│       └── D2-communiquer-valoriser.md
├── TEMPLATE-fiche.md           # modèle à copier pour créer une fiche
├── mkdocs.yml                  # configuration + navigation
├── requirements.txt            # dépendance (mkdocs-material)
├── CONTRIBUTING.md             # guide détaillé de contribution
├── README.md                   # ce fichier
└── .github/
    ├── workflows/deploy.yml    # build + déploiement automatiques
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/fiche.md
```

### Les 13 fiches, par thème

| Code | Thème | Fiches |
|---|---|---|
| G1–G4 | **Gouvernance & Stratégie** | Mandat · Parties prenantes · Objectifs & ODD · Feuille de route |
| M1–M2 | **Mesure & Diagnostic** | Diagnostic · Pilotage & KPI |
| C1–C2 | **Conception sobre** | Éco-conception des services · Cycle de vie des données |
| I1–I2 | **Infrastructure & Matériel** | Infrastructures & environnements · Achats responsables |
| V1 | **Chaîne de valeur** | Maturité des parties prenantes |
| D1–D2 | **Déploiement & Valorisation** | Conformité · Communiquer & valoriser |

---

## 4. Utiliser le site (lecture)

Rien à installer. Ouvrez <https://institut-du-numerique-responsable.github.io/BP-AIR/> :

- **Menu de gauche** : les fiches rangées par thème.
- **Barre de recherche** (en haut) : recherche plein texte dans tout le contenu.
- **Bouton clair/sombre** (en haut).
- Le site est **responsive** (lisible sur mobile).

---

## 5. Éditer une fiche (le plus simple — dans le navigateur)

Pas besoin de Git en ligne de commande.

1. Sur le site ou GitHub, ouvrez le fichier de la fiche dans `docs/fiches/`.
2. Cliquez sur l'icône **crayon ✏️** (« Edit this file »). *(Astuce : depuis la page d'accueil du dépôt, la touche `.` ouvre un éditeur web complet, `github.dev`.)*
3. Modifiez le texte en respectant les **sections du modèle** (Objectif, Contexte, Étapes, KPIs, Pièges…).
4. En bas : **Commit changes** → choisissez **« Create a new branch and start a pull request »**.
5. Un autre membre **relit et approuve** la Pull Request, puis la **merge**.
6. ~30 s plus tard, le **site est à jour automatiquement**.

### Créer une nouvelle fiche

1. Copiez `TEMPLATE-fiche.md` dans `docs/fiches/` en la nommant `CODE-titre-court.md` (ex. `G5-formation.md`).
2. Remplissez l'entête `---` (frontmatter) : `id`, `titre`, `theme`, `proprietaire`, `contributeurs`…
3. Ajoutez-la dans `mkdocs.yml` (sous le bon thème) **et** dans le tableau de `docs/index.md`.
4. Ouvrez une Pull Request.

### L'entête de chaque fiche (frontmatter)

```yaml
---
id: C1
titre: Éco-concevoir les services numériques
theme: Conception sobre
statut: brouillon        # brouillon → en-revue → validé
proprietaire: INR/ISIT   # entité détentrice de la fiche
contributeurs: [Prénom Nom]   # rédacteurs ; ajoutez-vous quand vous contribuez
reviewers: []
version: 0.1
maj: 2026-06-04
---
```

- Ajoutez votre nom dans `contributeurs` quand vous travaillez sur une fiche (évite les éditions concurrentes : voyez qui est déjà dessus).
- Passez `statut` à `en-revue` quand la fiche est prête, `validé` quand le GT l'a actée.
- Avant `validé`, **supprimez la section « Notes de coédition »** en bas de fiche.

### Ajouter une image / un schéma

1. Déposez le fichier dans `docs/assets/img/` (nom explicite, ex. `cartographie-urbanisation.png`).
2. Insérez-le dans une fiche/section avec une légende — le **zoom plein écran** au clic est automatique :

   ```markdown
   <figure markdown>
     ![Texte alternatif décrivant l'image](../assets/img/mon-schema.png)
     <figcaption>Légende affichée sous l'image.</figcaption>
   </figure>
   ```

   Chemin : `assets/img/...` depuis `index.md` / `guide-unifie.md`, **`../assets/img/...`** depuis une fiche dans `docs/fiches/`.
3. Renseignez toujours le **texte alternatif** (accessibilité) et **créditez la source** si l'image n'est pas la vôtre.

> ⚖️ Les schémas issus des publications INR/ISIT sont sous licence **CC BY-SA 4.0** : attribution + même licence obligatoires.

> Détail complet du workflow et des règles d'écriture : **[CONTRIBUTING.md](CONTRIBUTING.md)**.

---

## 6. Travailler à plusieurs (branche protégée + Pull Requests)

La branche `main` est **protégée** : personne ne pousse directement dessus. Toute évolution passe par une **Pull Request (PR) relue**. C'est ce qui rend la coédition sûre — rien n'arrive en ligne sans relecture, et l'historique reste propre.

### Règles en vigueur sur `main`
- ❌ Pas de push direct sur `main`.
- ✅ Toute modification via une **branche** + une **Pull Request**.
- 👁️ **1 approbation** d'un autre membre minimum avant de pouvoir fusionner.
- 🤖 La **construction du site doit réussir** (vérification automatique `build`, qui lance `mkdocs build --strict` : liens cassés, navigation invalide = PR bloquée).
- 🔄 La PR doit être **à jour** avec `main` avant fusion.

### Le parcours d'une évolution ou d'une correction

```
1. Créer une branche       (depuis main)
        │
2. Modifier la / les fiche(s) en Markdown
        │
3. Ouvrir une Pull Request  → décrire le changement
        │
4. Vérification auto "build" (mkdocs --strict)   ──┐
        │                                          │ doivent être OK
5. Relecture + approbation d'un membre  ───────────┘
        │
6. Fusion (Merge) dans main
        │
7. Déploiement automatique → site à jour (~30 s)
```

### A. Tout dans le navigateur (recommandé pour la plupart)
1. Ouvrez la fiche dans `docs/fiches/`, cliquez **✏️ Edit**.
2. Faites vos modifications.
3. **Commit changes** → cochez **« Create a new branch and start a pull request »** → nommez la branche (ex. `correction-C1-typo`) → **Propose changes**.
4. Renseignez le titre/description, **Create pull request**.
5. Attendez le ✅ de la vérification `build`, demandez la relecture (`Reviewers`).
6. Après approbation, cliquez **Merge pull request**. Le site se met à jour seul.

### B. En local avec Git (pour les contributions plus larges)
```bash
git clone https://github.com/Institut-du-Numerique-Responsable/BP-AIR.git
cd BP-AIR
git switch -c ma-contribution          # nouvelle branche
# … éditer les fichiers, prévisualiser avec « mkdocs serve » (voir §7) …
git add -A && git commit -m "Décrit le changement"
git push -u origin ma-contribution
gh pr create --fill                    # ou ouvrir la PR depuis l'interface GitHub
```

### Bonnes pratiques
- **Une PR = un sujet** (une fiche ou une correction ciblée) → relecture plus simple, fusion plus rapide.
- Ajoutez-vous dans `contributeurs` (frontmatter) de la fiche travaillée.
- Nom de branche parlant : `ajout-G5-formation`, `maj-outils-I1`, `correction-liens-C2`.
- Répondez aux commentaires de relecture en poussant de nouveaux commits sur la **même branche** (la PR se met à jour automatiquement).

---

## 7. Prévisualiser en local (optionnel, pour les plus à l'aise)

Pour voir le rendu avant de pousser :

```bash
git clone https://github.com/Institut-du-Numerique-Responsable/BP-AIR.git
cd BP-AIR
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # ouvre http://127.0.0.1:8000 (recharge auto)
```

---

## 8. Contribuer sans Git (alternative)

Pour les membres bloqués par Git ou par les règles de sécurité de leur entreprise : rédigez le brouillon dans **HackMD** (<https://hackmd.io>, Markdown en temps réel, commentaires), puis un membre à l'aise avec Git reporte le contenu validé dans le dépôt via une Pull Request.

---

## 9. Publication — résumé

| Question | Réponse |
|---|---|
| Qui publie ? | Personne manuellement — GitHub Actions le fait à chaque merge sur `main`. |
| Combien de temps ? | ~30 secondes après le merge. |
| Où voir l'état ? | Onglet **Actions** du dépôt. |
| Coût ? | Gratuit (dépôt public + GitHub Pages). |

---

*Contenu fusionnant le Livre Blanc AIR (INR, 2024), le Guide des Bonnes Pratiques AIR (2026) et le Guide d'évaluation de la maturité NR des parties prenantes (INR/ISIT, 2024).*
