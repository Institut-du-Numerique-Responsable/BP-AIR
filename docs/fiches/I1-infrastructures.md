---
id: I1
titre: Optimiser infrastructures & environnements
theme: Infrastructure & Matériel
statut: brouillon
proprietaire: INR/ISIT
contributeurs: [Guillaume Gallon]
reviewers: []
version: 0.1
maj: 2026-06-04
fiches_liees: [I2, C2, M1]
---

# I1 — Optimiser infrastructures & environnements

> **Public cible.** Ops, Infra, SRE, architectes techniques, FinOps.

## Objectif

Réduire le gaspillage matériel : **25-30 % des serveurs** tournent sans usage ; un serveur sous-utilisé consomme jusqu'à **60 % de son énergie nominale**.

## Contexte & enjeu

La consolidation peut réduire la consommation de **30 à 60 %**. Le stockage virtuel « indolore » ne l'est pas : multiplier les environnements a un coût réel. Cf. [guide unifié](../guide-unifie.md#26-pilier-5-architecture-logicielle-sobre-eco-conception).

## Étapes de mise en œuvre

1. **Monitorer l'usage réel** (CPU, RAM, I/O via Prometheus / Grafana) ; revue trimestrielle de consolidation / réaffectation / décommissionnement.
2. Politique de **TTL** sur les environnements de test ; arrêt systématique des inutilisés ; suppression des projets terminés.
3. **Virtualisation** : dimensionner au plus juste, bon provisioning disque, supprimer les snapshots obsolètes.
4. **Conteneurisation** : partager les images de base, nettoyer les images/couches orphelines (`docker image prune`).
5. **Logs** : rotation et nettoyage automatiques (Logrotate) ; DEBUG ponctuel.
6. **Archivages** : purger l'historique de versions (SharePoint/OneDrive), nettoyer les fichiers Teams.

## KPIs & OKR

- **KPI** : taux d'usage réel des ressources allouées ; nombre d'environnements décommissionnés.
- ***OKR*** : −15 % de consommation énergétique datacenter via les actions de sobriété (consolidation : −30 à −60 % possibles).

## Pièges à éviter

- Surdimensionner « pour les pics » au lieu d'auto-scaler.
- Multiplier les environnements (le stockage virtuel « indolore » ne l'est pas).
- Augmenter les ressources d'un service sans investiguer la cause (fuite mémoire, code non optimisé).

## Outils & ressources

| Outil / Ressource | Usage | Lien |
|---|---|---|
| Prometheus / Grafana | Monitoring usage réel | <https://grafana.com> |
| DataVizta (Boavizta) | Impact serveurs/cloud | <https://dataviz.boavizta.org/> |

## Fiches liées

- [I2 — Achats numériques responsables](I2-achats-responsables.md)
- [C2 — Maîtriser le cycle de vie des données](C2-cycle-vie-donnees.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)

---

!!! note "🗨️ Notes de coédition (à purger avant validation)"
    —
