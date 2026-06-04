# Contribuer aux fiches AIR

Pas besoin d'être développeur. Tout se fait dans le navigateur. Le Markdown que vous écrivez devient le site automatiquement — **ne vous occupez pas de la mise en forme du site.**

## 1. Éditer une fiche existante

1. Ouvrez le fichier de la fiche dans `docs/fiches/` (ex. `C1-eco-conception-services.md`).
2. Cliquez sur l'icône **crayon** (✏️ « Edit this file ») — ou appuyez sur la touche `.` depuis le dépôt pour ouvrir l'éditeur web complet (`github.dev`).
3. Modifiez le texte. Respectez les **sections du modèle** (Objectif, Contexte, Étapes, KPIs, Pièges…).
4. En bas : « Commit changes » → cochez **« Create a new branch and start a pull request »** → décrivez votre changement.
5. Un autre membre relit, commente, approuve, puis *merge*. Le site se reconstruit seul.

## 2. Créer une nouvelle fiche

1. Copiez `TEMPLATE-fiche.md` dans `docs/fiches/` sous le nom `CODE-titre-court.md` (ex. `G5-formation.md`).
2. Remplissez le **frontmatter** (entête entre `---`) : `id`, `titre`, `theme`, `proprietaire`, `contributeurs`, etc.
3. Ajoutez la fiche à la navigation dans `mkdocs.yml` (sous le bon thème) et au tableau de `docs/index.md`.
4. Ouvrez une Pull Request.

## 3. Le frontmatter (pilotage de la coédition)

```yaml
statut: brouillon         # brouillon → en-revue → validé
proprietaire: INR/ISIT    # entité détentrice de la fiche
contributeurs: [Prénom Nom]   # rédacteurs
reviewers: []             # qui doit relire
version: 0.1
maj: 2026-06-04
```

- Le **propriétaire** est l'entité détentrice (INR/ISIT) ; ajoutez votre nom dans **`contributeurs`** quand vous travaillez sur une fiche (permet de voir qui est déjà dessus et d'éviter les éditions concurrentes).
- Passez `statut` à `en-revue` quand la fiche est prête à relecture, `validé` une fois actée par le GT.
- Avant `validé`, **purgez la section « Notes de coédition »** (en bas de fiche).

## 4. Règles d'écriture

- Public visé : **architectes SI** et **experts numérique responsable**. Ton concret, actionnable.
- Une affirmation chiffrée = une source (ex. *Forrester 2021*, *ADEME*).
- Liens entre fiches : liens Markdown relatifs (`[C2](C2-cycle-vie-donnees.md)`).
- Pour chaque outil, indiquez la **licence / coût** par un préfixe : **🟢 open source · 🆓 gratuit · 💶 payant** (ajoutez *(freemium)* si offre mixte).
- Pas de secret, token, ni donnée interne d'entreprise dans le dépôt (public).

## 5. Rédiger sans Git (alternative)

Pour les contributeurs gênés par Git : rédigez le brouillon dans **HackMD** (<https://hackmd.io>, Markdown temps réel, commentaires), puis un membre à l'aise avec Git reporte le contenu validé dans le dépôt via une PR.

## 6. Workflow de relecture (résumé)

```
brouillon  →  PR  →  relecture (≥1 reviewer)  →  merge  →  site mis à jour  →  statut: validé
```
