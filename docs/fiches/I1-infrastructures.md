---
id: I1
titre: Optimiser infrastructures & environnements
description: >-
  Optimiser infrastructures et environnements : 25 à 30 % des serveurs tournent sans usage et un serveur sous-utilisé consomme jusqu'à 60 % de son énergie nominale.
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

La consolidation peut réduire la consommation de **30 à 60 %**. Le stockage virtuel « indolore » ne l'est pas : multiplier les environnements a un coût réel. Cf. [guide](../guide-unifie.md#26-pilier-5-architecture-logicielle-sobre-eco-conception).

## Étapes de mise en œuvre

1. **Monitorer l'usage réel** (CPU, RAM, I/O via Prometheus / Grafana, Netdata) ; revue trimestrielle de consolidation / réaffectation / décommissionnement.
2. **Mesurer la consommation électrique et carbone** de l'infrastructure (sondes type Scaphandre / Kepler ; estimation cloud via Cloud Carbon Footprint, DataVizta) pour prioriser sur des données réelles, pas ressenties.
3. **Right-sizing** : ajuster les ressources allouées aux besoins observés (recommandeurs Goldilocks, KRR sur Kubernetes ; provisioning disque adapté ; suppression des snapshots obsolètes).
4. Politique de **TTL** et d'extinction hors heures sur les environnements de test (Cloud Custodian, kube-green) ; arrêt systématique des inutilisés ; suppression des projets terminés.
5. **Conteneurisation** : partager les images de base, analyser et alléger les couches (`dive`), nettoyer les images/couches orphelines (`docker image prune`).
6. **Auto-scaling & carbon-aware** : préférer l'élasticité au surdimensionnement (KEDA) ; quand c'est possible, décaler les charges flexibles vers les heures bas-carbone (Carbon Aware SDK).
7. **Logs** : rotation et nettoyage automatiques (Logrotate, Grafana Loki) ; DEBUG ponctuel.
8. **Archivages** : purger l'historique de versions (SharePoint/OneDrive), nettoyer les fichiers Teams.
9. **Piloter les coûts (FinOps)** comme proxy de la sobriété : attribuer et suivre la dépense par service (OpenCost, Infracost en CI/CD).

## KPIs & OKR

- **KPI** : taux d'usage réel des ressources allouées ; nombre d'environnements décommissionnés.
- ***OKR*** : −15 % de consommation énergétique datacenter via les actions de sobriété (consolidation : −30 à −60 % possibles).

## Pièges à éviter

- Surdimensionner « pour les pics » au lieu d'auto-scaler.
- Multiplier les environnements (le stockage virtuel « indolore » ne l'est pas).
- Augmenter les ressources d'un service sans investiguer la cause (fuite mémoire, code non optimisé).

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

| Catégorie | Outil / Ressource | Usage | Lien |
|---|---|---|---|
| Monitoring | 🟢 **Prometheus + Grafana** | Métriques d'usage réel (CPU, RAM, I/O), tableaux de bord | <https://grafana.com> |
| Monitoring | 🟢 **Netdata** | Supervision temps réel par ressource, faible empreinte | <https://www.netdata.cloud/> |
| Énergie / carbone | 🟢 **Scaphandre** | Mesure de la consommation électrique des hôtes et VM | <https://github.com/hubblo-org/scaphandre> |
| Énergie / carbone | 🟢 **Kepler** | Estimation de l'énergie des workloads Kubernetes | <https://sustainable-computing.io/> |
| Énergie / carbone | 🟢 **Cloud Carbon Footprint** | Empreinte carbone des usages cloud (AWS/GCP/Azure) | <https://www.cloudcarbonfootprint.org/> |
| Énergie / carbone | 🟢 **DataVizta** (Boavizta) | Impact fabrication/usage serveurs & cloud | <https://dataviz.boavizta.org/> |
| Virtualisation (VMware) | **EasyVirt** (DC Scope / CO2 Scope) | Optimisation, capacité et empreinte carbone d'environnements VMware/VDI | <https://www.easyvirt.com/> |
| Right-sizing | 🟢 **Goldilocks** (Fairwinds) | Recommandations de dimensionnement (VPA) Kubernetes | <https://github.com/FairwindsOps/goldilocks> |
| Right-sizing | 🟢 **KRR** (Robusta) | Recommandations de ressources sans agent | <https://github.com/robusta-dev/krr> |
| Cycle de vie env. | 🟢 **Cloud Custodian** | Règles automatiques : TTL, arrêt des ressources inutilisées | <https://cloudcustodian.io/> |
| Cycle de vie env. | 🟢 **kube-green** | Extinction des namespaces hors heures ouvrées | <https://kube-green.dev/> |
| Conteneurs | 🟢 **dive** | Analyse des couches d'image, repérage du superflu | <https://github.com/wagoodman/dive> |
| Élasticité | 🟢 **KEDA** | Auto-scaling événementiel (scale-to-zero) | <https://keda.sh/> |
| Carbon-aware | 🟢 **Carbon Aware SDK** (GSF) | Décaler les charges flexibles vers les heures bas-carbone | <https://github.com/Green-Software-Foundation/carbon-aware-sdk> |
| Logs | 🟢 **Grafana Loki** | Agrégation/rotation des logs, rétention maîtrisée | <https://grafana.com/oss/loki/> |
| FinOps | 🟢 **OpenCost** | Coût par service/namespace (proxy de sobriété) | <https://www.opencost.io/> |
| FinOps | 🟢 **Infracost** | Estimation du coût de l'infra (IaC) en CI/CD | <https://www.infracost.io/> |

## Fiches liées

- [I2 — Achats numériques responsables](I2-achats-responsables.md)
- [C2 — Maîtriser le cycle de vie des données](C2-cycle-vie-donnees.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)
