---
id: C2
titre: Maîtriser le cycle de vie des données
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

> **Public cible.** Architectes data, DBA, Dév, métiers propriétaires de données, DPO.

## Objectif

Réduire le poids des données — environ **52 % de dark data** et **33 % de ROT** dans un SI moyen.

## Contexte & enjeu

La donnée est l'objet même de l'informatique, et le plus négligé. Dark data et ROT coûtent en infrastructure, énergie, ETP, et faussent les décisions. Mais une donnée sans valeur aujourd'hui peut en créer demain : décommissionner avec discernement. Cf. [guide unifié](../guide-unifie.md#24-pilier-3-cycle-de-vie-architecture-services-donnees).

## Étapes de mise en œuvre

1. Mettre en place un **catalogue / registre** des données ; qualifier **chaud / froid**.
2. Adapter les **supports de stockage** à la température de la donnée.
3. Organiser des **campagnes de décommissionnement** des dark data et de nettoyage des ROT.
4. Documenter et contextualiser la donnée (source, fraîcheur, échantillonnage) pour limiter biais et duplication.
5. Articuler avec le **RGPD** (durée de conservation, droit à l'effacement).

## KPIs & OKR

- **KPI** : taux de données ROT ; taux de redondance ; % de données cataloguées ; volume de stockage libéré par campagne.
- ***OKR*** : catalogue de données opérationnel ; première campagne de décommissionnement réalisée ce semestre.

## Pièges à éviter

- **Tout effacer** : une donnée sans valeur aujourd'hui peut en créer demain.
- Dupliquer faute de catalogue (confusion sur la donnée « de référence »).
- Négliger la gouvernance → le problème revient à chaque projet.

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

| Outil / Ressource | Usage | Lien |
|---|---|---|
| RGPD / CNIL | Conservation, effacement | <https://www.cnil.fr> |

## Fiches liées

- [C1 — Éco-concevoir les services numériques](C1-eco-conception-services.md)
- [I1 — Optimiser infrastructures & environnements](I1-infrastructures.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)

---

!!! note "🗨️ Notes de coédition (à purger avant validation)"
    —
