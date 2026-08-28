---
id: M1
titre: Faire l'état des lieux (diagnostic)
description: >-
  Réaliser le diagnostic initial d'un système d'information : empreinte environnementale, volet social et maturité numérique responsable.
theme: Mesure et diagnostic
statut: brouillon
proprietaire: INR/ISIT
contributeurs: [Guillaume Gallon]
reviewers: []
version: 0.1
maj: 2026-06-04
fiches_liees: [G3, G4, M2]
---

# M1 — Faire l'état des lieux (diagnostic)

> **Public cible.** Architectes, équipes d'exploitation et d'infrastructure, développeurs, spécialistes des données et équipes RSE.

## Objectif

Établir une situation de référence qui couvre les impacts environnementaux et sociaux ainsi que le niveau de maturité de l'organisation.

## Contexte et enjeux

Le diagnostic conditionne toute la suite : sans base de référence, impossible de prioriser les objectifs ([G3](G3-objectifs-odd.md)), de construire la feuille de route ([G4](G4-feuille-de-route.md)) ou de prouver les progrès ([M2](M2-pilotage-kpi.md)). Attention à ne pas se limiter au carbone. Voir le [guide](../guide-unifie.md#27-pilier-6-mesure-et-pilotage-lequation-de-kaya-appliquee-au-si).

## Étapes de mise en œuvre

1. Piloter la **collecte d'inventaire** (serveurs, postes, applications, données).
2. Déployer des **sondes** de consommation sur un périmètre représentatif.
3. Réaliser des **audits** d'éco-conception (EcoIndex) et d'accessibilité (RGAA / WCAG) sur les applications critiques.
4. Lancer une **enquête** sur les usages et attentes des collaborateurs.
5. Établir un **Bilan Carbone du SI** (Scopes 1, 2, 3) et une **cartographie de maturité** (via WeNR / NumEcoEval).

## Indicateurs et objectifs

- **KPI** : taux d'avancement de la collecte ; nombre de services audités / prévus ; KPI multidimensionnels par couche (taux de données ROT, taux d'usage réel, taux d'équipements réemployés).
- ***OKR*** : premier bilan GES complet finalisé ce semestre ; 100 % des applications critiques auditées ; score de maturité initial produit.

## Pièges à éviter

- Mesurer pour mesurer, sans relier au plan d'action.
- Ne regarder que le carbone (oublier accessibilité, données, social).
- L'**auto-évaluation complaisante** : pour la maturité, croiser les regards (idéalement un tiers).

## Outils et ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Outil / Ressource | Usage | Lien |
|---|---|---|
| 🟢 WeNR | Empreinte GES + maturité NR du SI | <https://wenr.isit-europe.org/> |
| 🟢 MyImpact (INR/ISIT) | Calculateur d'empreinte individuelle (enquête/sensibilisation) | <https://myimpact.isit-europe.org/fr/> |
| 🟢 NumEcoEval | Évaluation environnementale des SI | — |
| 🟢 DataVizta (Boavizta) | Impact fabrication/usage | <https://dataviz.boavizta.org/> |
| 🟢 EcoIndex CLI | Audit éco-conception | <https://github.com/cnumr/EcoIndex_python> |
| 🟢 GPC-ONR (INR) | Auto-évaluation participative de la démarche NR, en complément des mesures techniques | <https://github.com/Institut-du-Numerique-Responsable/GPC-ONR> |
| 🟢 Tanaguru | Accessibilité (RGAA/WCAG) | — |

## Fiches liées

- [G3 — Identifier et prioriser les objectifs](G3-objectifs-odd.md)
- [G4 — Construire la feuille de route](G4-feuille-de-route.md)
- [M2 — Pilotage et tableau de bord KPI](M2-pilotage-kpi.md)
