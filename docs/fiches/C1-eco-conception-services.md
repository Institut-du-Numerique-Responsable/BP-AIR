---
id: C1
titre: Éco-concevoir les services numériques
description: >-
  Éco-concevoir les services numériques : intégrer la sobriété dès la conception et la maintenir dans le temps (RGESN, GR491, EcoIndex).
theme: Conception sobre
statut: brouillon
proprietaire: INR/ISIT
contributeurs: [Guillaume Gallon]
reviewers: []
version: 0.1
maj: 2026-06-04
fiches_liees: [C2, M1, D1]
---

# C1 — Éco-concevoir les services numériques

> **Public cible.** Dév, Product Owners, architectes, UX, QA.

## Objectif

Intégrer la sobriété **dès la conception** des services, et la maintenir dans le temps.

## Contexte & enjeux

Près de **45 % des fonctionnalités développées ne sont jamais utilisées**. L'éco-conception ajoutée en fin de projet est coûteuse et superficielle ; intégrée en amont, elle réduit poids, requêtes et dette. Cf. [guide](../guide-unifie.md#26-pilier-5-architecture-logicielle-sobre-eco-conception).

## Étapes de mise en œuvre

1. Appliquer la **règle des 3U** dès la conception métier (Utile, Utilisé, Utilisable).
2. Privilégier les **standards ouverts** (REST, JSON, ODF, CSV).
3. Maîtriser **poids des pages, nombre de requêtes, poids des médias** (EcoIndex, YellowLab, RequestMap).
4. **Automatiser** les contrôles en CI/CD (analyse statique / EcoCode, tests de performance, scan d'accessibilité) et intégrer des critères NR dans la **Definition of Done**.
5. Assurer **rétrocompatibilité** et **auto-scaling** ; choisir des hébergeurs engagés.
6. Mettre en place des **revues d'architecture et de code** spécifiques NR.

## KPIs & OKR

- **KPI** : score EcoIndex / poids moyen des pages ; taux d'applications conformes RGAA (niveau AA) ; taux d'usage réel des fonctionnalités (3U).
- ***OKR*** : 75 % de conformité RGAA AA sur les 3 sites principaux.

## Pièges à éviter

- Éco-conception « en fin de projet » → coûteuse et superficielle.
- Optimiser le front en ignorant le backend et les requêtes.
- Laisser la dette s'accumuler : un service éco-conçu se dégrade au fil des maintenances non outillées.

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Outil / Ressource | Usage | Lien |
|---|---|---|
| 🟢 EcoIndex CLI | Poids des pages, CI/CD | <https://github.com/cnumr/EcoIndex_python> |
| 🟢 YellowLab Tools | Requêtes, perfs front | <https://yellowlab.tools/> |
| RequestMap | Cartographie des requêtes | <https://requestmap.webperf.tools/> |
| 🟢 GR491 (INR) | Référentiel d'éco-conception | <https://gr491.isit-europe.org/> |
| RGESN | Référentiel général d'éco-conception | <https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/> |
| 🟢 Green Claude (INR) | Audit d'éco-conception et sobriété IA directement dans Claude Code | [Présentation](https://institut-du-numerique-responsable.github.io/green-claude/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/green-claude) |
| 🟢 Skill NR (INR) | Règles RGESN/GR491/Opquast/RGAA pour 11 assistants IA de code (Copilot, Cursor, Continue, Gemini CLI…) | [Présentation](https://institut-du-numerique-responsable.github.io/skill-nr/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/skill-nr) |

## Fiches liées

- [C2 — Maîtriser le cycle de vie des données](C2-cycle-vie-donnees.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)
- [D1 — Mettre en œuvre & contrôler la conformité](D1-conformite.md)
