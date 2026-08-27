---
id: M2
titre: Pilotage & tableau de bord KPI
description: >-
  Piloter une démarche numérique responsable par les KPI : indicateurs multidimensionnels, tableau de bord et boucle Mesurer → Agir → Apprendre → Ajuster.
theme: Mesure & Diagnostic
statut: brouillon
proprietaire: INR/ISIT
contributeurs: [Guillaume Gallon]
reviewers: []
version: 0.1
maj: 2026-06-04
fiches_liees: [M1, D2]
---

# M2 — Pilotage & tableau de bord KPI

> **Public cible.** Architectes, RSE, DSI, FinOps, Communication (consommateurs des indicateurs).

## Objectif

Mettre en place un pilotage continu de la démarche NR : indicateurs multidimensionnels, tableau de bord vivant, boucle d'amélioration *Mesurer → Agir → Apprendre → Ajuster*.

## Contexte & enjeu

« On ne pilote que ce que l'on mesure. » Le diagnostic ([M1](M1-diagnostic.md)) donne le point de départ ; le pilotage transforme cette photo en film. Un bon KPI NR croise les **5 axes du NR**, le **cycle de vie**, les **couches d'architecture** et le triptyque **People / Planet / Prosperity**. Cf. [guide](../guide-unifie.md#27-pilier-6-mesure-pilotage-lequation-de-kaya-appliquee-au-si).

## Étapes de mise en œuvre

1. Sélectionner un **jeu de KPI multidimensionnels** par couche (cf. matrice du guide) — éviter la sur-instrumentation.
2. Transposer l'**équation de Kaya au SI** pour relier stratégie et empreinte (intensité carbone, efficience énergétique, efficacité, sobriété).
3. Outiller la collecte automatique (sondes, logs, exports) et brancher un **tableau de bord** (Grafana, PowerBI).
4. Définir la **fréquence de revue** et les responsables de chaque indicateur.
5. Rattacher les indicateurs aux **scopes du Bilan Carbone** (ADEME / ABC) et aux ODD adressés.

## KPIs & OKR

- **KPI** : nombre de KPI suivis automatiquement ; fraîcheur du tableau de bord ; couverture des couches d'architecture.
- ***OKR*** : tableau de bord NR en production ce semestre ; revue trimestrielle instituée ; 100 % des objectifs prioritaires ([G3](G3-objectifs-odd.md)) dotés d'un indicateur.

## Pièges à éviter

- Multiplier les indicateurs au point que personne ne les regarde.
- Mesurer le seul carbone et oublier inclusion, données, éthique, résilience.
- Tableau de bord figé / non alimenté → perte de crédibilité.

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Outil / Ressource | Usage | Lien |
|---|---|---|
| 🟢 WeNR | Empreinte GES + maturité du SI | <https://wenr.isit-europe.org/> |
| 🟢 MyImpact (INR/ISIT) | Calculateur d'empreinte individuelle | <https://myimpact.isit-europe.org/fr/> |
| ImpactCO₂ (ADEME) | Conversion / vulgarisation | <https://impactco2.fr/outils/numerique> |

## Fiches liées

- [M1 — Faire l'état des lieux](M1-diagnostic.md)
- [D2 — Communiquer, valoriser & labelliser](D2-communiquer-valoriser.md)

<!-- Notes de coédition (interne au GT, non publiées sur le site) :
     Fiche nouvelle : extraite et développée à partir du pilotage évoqué dans
     l'ancienne fiche C2. À enrichir par le GT (choix du référentiel KPI,
     exemples concrets par couche). -->
