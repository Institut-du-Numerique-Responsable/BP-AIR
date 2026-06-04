---
id: M1
titre: Faire l'état des lieux (diagnostic)
theme: Mesure & Diagnostic
statut: brouillon
proprietaire: INR/ISIT
contributeurs: [Guillaume Gallon]
reviewers: []
version: 0.1
maj: 2026-06-04
fiches_liees: [G3, G4, M2]
---

# M1 — Faire l'état des lieux (diagnostic)

> **Public cible.** Architectes, Ops/Infra, Dév, Data, RSE.

## Objectif

Mesurer objectivement le point de départ — environnemental, social, maturité — car on n'améliore que ce que l'on mesure.

## Contexte & enjeu

Le diagnostic conditionne toute la suite : sans base de référence, impossible de prioriser ([G4](G4-feuille-de-route.md)) ni de prouver les progrès ([M2](M2-pilotage-kpi.md)). Attention à ne pas se limiter au carbone. Cf. [guide](../guide-unifie.md#27-pilier-6-mesure-pilotage-lequation-de-kaya-appliquee-au-si).

## Étapes de mise en œuvre

1. Piloter la **collecte d'inventaire** (serveurs, postes, applications, données).
2. Déployer des **sondes** de consommation sur un périmètre représentatif.
3. Réaliser des **audits** d'éco-conception (EcoIndex) et d'accessibilité (RGAA / WCAG) sur les applications critiques.
4. Lancer une **enquête** sur les usages et attentes des collaborateurs.
5. Établir un **Bilan Carbone du SI** (Scopes 1, 2, 3) et une **cartographie de maturité** (via WeNR / NumEcoEval).

## KPIs & OKR

- **KPI** : taux d'avancement de la collecte ; nombre de services audités / prévus ; KPI multidimensionnels par couche (taux de données ROT, taux d'usage réel, taux d'équipements réemployés).
- ***OKR*** : premier bilan GES complet finalisé ce semestre ; 100 % des applications critiques auditées ; score de maturité initial produit.

## Pièges à éviter

- Mesurer pour mesurer, sans relier au plan d'action.
- Ne regarder que le carbone (oublier accessibilité, données, social).
- L'**auto-évaluation complaisante** : pour la maturité, croiser les regards (idéalement un tiers).

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

| Outil / Ressource | Usage | Lien |
|---|---|---|
| 🟢 WeNR | Empreinte GES + maturité NR du SI | <https://wenr.isit-europe.org/> |
| 🟢 MyImpact (INR/ISIT) | Calculateur d'empreinte individuelle (enquête/sensibilisation) | <https://myimpact.isit-europe.org/fr/> |
| 🟢 NumEcoEval | Évaluation environnementale des SI | — |
| 🟢 DataVizta (Boavizta) | Impact fabrication/usage | <https://dataviz.boavizta.org/> |
| 🟢 EcoIndex CLI | Audit éco-conception | <https://github.com/cnumr/EcoIndex_python> |
| 🟢 Tanaguru | Accessibilité (RGAA/WCAG) | — |

## Fiches liées

- [G3 — Identifier & prioriser les objectifs](G3-objectifs-odd.md)
- [G4 — Construire la feuille de route](G4-feuille-de-route.md)
- [M2 — Pilotage & tableau de bord KPI](M2-pilotage-kpi.md)

---

!!! note "🗨️ Notes de coédition (à purger avant validation)"
    —
