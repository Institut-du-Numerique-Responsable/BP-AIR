---
id: C2
titre: Maîtriser le cycle de vie des données
description: >-
  Maîtriser le cycle de vie des données pour réduire leur poids dans le SI : dark data (≈52 %), données ROT (≈33 %), archivage et purge.
theme: Conception sobre
statut: brouillon
proprietaire: INR/ISIT
contributeurs: [Guillaume Gallon]
reviewers: []
version: 0.1
maj: 2026-06-04
fiches_liees: [C1, I1, M1]
---

# C2 — Maîtriser le cycle de vie des données

> **Public cible.** Architectes des données, administrateurs de bases de données, développeurs, métiers responsables des données et DPO.

## Objectif

Réduire les volumes stockés en repérant les données redondantes, obsolètes, inutilisées ou dépourvues de contexte.

## Contexte et enjeux

Les organisations accumulent souvent des données sans définir leur durée de conservation, leur valeur ni leur responsable. Ces données inutilisées, ainsi que les données redondantes, obsolètes ou triviales (ROT), mobilisent des infrastructures et de l'énergie. Elles peuvent aussi fausser les décisions. Une donnée sans valeur aujourd'hui peut toutefois en créer demain : supprimez-la avec discernement. Voir le [guide](../guide-unifie.md#24-pilier-3-cycle-de-vie-architecture-services-donnees).

## Étapes de mise en œuvre

1. Mettre en place un **catalogue / registre** des données ; qualifier **chaud / froid**.
2. Adapter les **supports de stockage** à la température de la donnée.
3. Organiser des **campagnes de décommissionnement** des dark data et de nettoyage des ROT.
4. Documenter et contextualiser la donnée (source, fraîcheur, échantillonnage) pour limiter biais et duplication.
5. Articuler avec le **RGPD** (durée de conservation, droit à l'effacement).

## Indicateurs et objectifs

- **KPI** : taux de données ROT ; taux de redondance ; % de données cataloguées ; volume de stockage libéré par campagne.
- ***OKR*** : catalogue de données opérationnel ; première campagne de décommissionnement réalisée ce semestre.

## Pièges à éviter

- **Tout effacer** : une donnée sans valeur aujourd'hui peut en créer demain.
- Dupliquer faute de catalogue (confusion sur la donnée « de référence »).
- Négliger la gouvernance → le problème revient à chaque projet.

## Outils et ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Outil / Ressource | Usage | Lien |
|---|---|---|
| RGPD / CNIL | Conservation, effacement | <https://www.cnil.fr> |

## Fiches liées

- [C1 — Éco-concevoir les services numériques](C1-eco-conception-services.md)
- [I1 — Optimiser infrastructures et environnements](I1-infrastructures.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)
