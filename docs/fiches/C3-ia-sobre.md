---
id: C3
titre: Concevoir & exploiter des services d'IA sobres
description: >-
  Encadrer l'empreinte des services d'intelligence artificielle : arbitrage du besoin, dimensionnement du modèle, sobriété de l'inférence, taux d'occupation GPU et conformité AI Act.
theme: Conception sobre
statut: brouillon
proprietaire: INR/ISIT
contributeurs: []
reviewers: []
version: 0.1
maj: 2026-08-27
fiches_liees: [C1, C2, I1, D1]
---

# C3 — Concevoir & exploiter des services d'IA sobres

> **Public cible.** Architectes, Data Scientists, MLOps, Ops/Infra, Product Owners, DPO.

## Objectif

Traiter un service d'IA comme les autres charges du SI : **utile, dimensionné,
mesuré**. Encadrer son empreinte pendant qu'elle est encore modeste, et tenir les
obligations d'inventaire de l'AI Act avec les mêmes livrables.

## Contexte & enjeu

Trois écarts entre l'IA générative et les réflexes d'architecture que vous
appliquez au reste du SI.

**L'inférence pèse plus que l'entraînement.** Vous entraînez, ou faites entraîner,
une fois. Vous servez le modèle des milliers de fois par jour, pendant des années.
Sur la durée de vie du service, l'**inférence domine le coût total**, énergie
comprise, et c'est pourtant l'entraînement qui capte les discussions.

**Vous appelez le plus gros modèle par défaut.** L'écart d'énergie par requête entre
un grand modèle généraliste et un petit modèle spécialisé se compte en **ordres de
grandeur**. Classer un ticket, extraire une date, reformuler un paragraphe : ces
usages n'exigent pas la puissance qu'on leur alloue.

**Vous réservez des GPU que personne n'utilise.** La fiche [I1](I1-infrastructures.md)
compte 25 à 30 % de serveurs qui tournent sans usage. Vous reproduisez ce gaspillage
sur des cartes dix fois plus coûteuses et plus énergivores, dont l'empreinte de
fabrication est élevée et l'approvisionnement tendu.

Deux dimensions échappent au débat carbone : la **consommation d'eau** des
datacenters d'inférence (ODD 6), et le **shadow AI**, ces outils que vos
collaborateurs utilisent sans validation, qui cumulent empreinte invisible et fuite
de données.

Cf. [guide](../guide-unifie.md#26-pilier-5-architecture-logicielle-sobre-eco-conception).

## Étapes de mise en œuvre

1. **Arbitrer le besoin avant la technologie.** Passer le service d'IA par la règle
   des **3U** : **U**tile, **U**tilisé, **U**tilisable. Poser ensuite la question
   que la mode escamote : *une solution déterministe suffirait-elle ?* Une règle
   métier, une recherche plein texte ou un modèle classique traitent une part des
   cas qu'on envoie à un LLM, pour une fraction de l'empreinte. Écrire l'arbitrage
   dans le dossier d'architecture, vous le rouvrirez.

2. **Dimensionner le modèle par le bas.** Partir du plus petit modèle candidat et
   remonter seulement si le seuil de qualité n'est pas atteint, jamais l'inverse.
   Fixer ce seuil *avant* les essais, sur un jeu d'évaluation représentatif.
   Envisager la **distillation** et la **quantification** pour les usages à volume.

3. **Préférer la RAG au réentraînement.** Pour ancrer un modèle dans vos données
   métier, une recherche augmentée coûte moins qu'un fine-tuning, s'actualise sans
   réentraîner et reste auditable. Garder l'ajustement fin pour les cas où le format
   de sortie ou le domaine l'imposent.

4. **Rendre l'inférence sobre.** Mettre en cache les réponses aux requêtes
   récurrentes ; **grouper les appels** (*batching*) plutôt que les traiter un à un ;
   plafonner la longueur des contextes et des réponses ; couper le *streaming* quand
   il n'apporte rien. Un serveur d'inférence adapté (vLLM, TGI) multiplie le débit à
   matériel constant.

5. **Piloter le taux d'occupation des GPU.** Le suivi porte sur la carte, pas sur la
   machine : un serveur peut afficher un CPU chargé pendant que ses huit GPU, la
   partie chère, restent à 5 %. Instrumenter l'usage GPU (DCGM, Kepler) au même
   titre que CPU et RAM en [I1](I1-infrastructures.md).
   Mutualiser les cartes entre équipes, appliquer une politique de **TTL** aux
   environnements d'expérimentation, éteindre les *notebooks* que plus personne
   n'ouvre.

6. **Mesurer l'empreinte par appel et par service.** Instrumenter les appels aux API
   de modèles (EcoLogits) et l'entraînement (CodeCarbon) pour obtenir un coût
   environnemental **par requête**. Une estimation annuelle globale ne vous dira pas
   quel service arbitrer.

7. **Décaler ce qui peut l'être.** Entraînements, réindexations et traitements par
   lots sont des charges flexibles : les planifier aux heures bas-carbone
   (Carbon Aware SDK), à l'inverse de l'inférence interactive.

8. **Gouverner les usages.** Tenir un **inventaire des systèmes d'IA** en production
   et en test : finalité, modèle, données d'entraînement, fournisseur, niveau de
   risque. L'AI Act l'exige, et il vous sert à repérer le shadow AI. La **Charte IA
   Responsable** de l'INR porte l'engagement, la fiche [D1](D1-conformite.md) les
   échéances.

9. **Articuler avec la gouvernance des données.** « On gardera tout, ça servira à
   entraîner » : voilà comment vos équipes fabriquent les *dark data* de
   [C2](C2-cycle-vie-donnees.md). Appliquer les durées de conservation aux corpus
   comme au reste.

## KPIs & OKR

- **KPI** : énergie et gCO₂e **par requête d'inférence** ; taux d'occupation des GPU ;
  part des requêtes servies par le cache ; part des usages traités par un petit modèle
  ou une solution déterministe ; systèmes d'IA inventoriés rapportés aux systèmes
  estimés ; coût mensuel par service (proxy FinOps).
- ***OKR*** : inventaire des systèmes d'IA complet et tenu à jour ce semestre ;
  taux d'occupation GPU porté au-dessus de 60 % ; 50 % des appels du service
  principal servis par un modèle plus petit à qualité constante.

## Pièges à éviter

- **Appeler le plus gros modèle par défaut**, faute d'avoir fixé un seuil de qualité.
- Ne mesurer que l'entraînement, quand la dérive s'installe en production, appel
  après appel.
- Réserver des GPU « pour le projet » et les laisser tourner à vide entre deux essais.
- Confondre coût facturé et empreinte. Un forfait à prix fixe supprime le signal
  d'usage : vous payez pareil que le service soit sobre ou non.
- Accumuler des corpus « au cas où » et recréer le problème de [C2](C2-cycle-vie-donnees.md).
- Renvoyer l'AI Act au juridique. Il réclame un inventaire et une traçabilité, deux
  livrables d'architecture.
- Raisonner en kWh seuls et oublier l'eau et la fabrication.

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Catégorie | Outil / Ressource | Usage | Lien |
|---|---|---|---|
| Mesure | 🟢 **EcoLogits** (GenAI Impact) | Empreinte des appels aux API de LLM, par requête | <https://ecologits.ai> |
| Mesure | 🟢 **CodeCarbon** | Émissions d'un entraînement ou d'un traitement | <https://codecarbon.io> |
| Mesure | 🟢 **ML CO2 Impact** | Estimation rapide avant lancement | <https://mlco2.github.io/impact/> |
| Comparaison | **AI Energy Score** (Hugging Face, Salesforce) | Classement énergétique des modèles par tâche | <https://huggingface.co/spaces/AIEnergyScore/Leaderboard> |
| Occupation GPU | 🟢 **DCGM Exporter** (NVIDIA) | Métriques par carte GPU vers Prometheus | <https://github.com/NVIDIA/dcgm-exporter> |
| Occupation GPU | 🟢 **Kepler** | Énergie des workloads Kubernetes, GPU compris | <https://sustainable-computing.io/> |
| Inférence | 🟢 **vLLM** | Serveur d'inférence à haut débit (batching continu) | <https://github.com/vllm-project/vllm> |
| Planification | 🟢 **Carbon Aware SDK** (GSF) | Décaler entraînements et lots vers les heures bas-carbone | <https://github.com/Green-Software-Foundation/carbon-aware-sdk> |
| Matériel | 🟢 **DataVizta** (Boavizta) | Empreinte de fabrication des serveurs et des cartes GPU | <https://dataviz.boavizta.org/> |
| Code | 🟢 **Green Claude** (INR) | Pratiques de sobriété IA et audit d'éco-conception dans l'IDE | [Présentation](https://institut-du-numerique-responsable.github.io/green-claude/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/green-claude) |
| Code | 🟢 **Skill NR** (INR) | Règles d'éco-conception pour 11 assistants IA de code | [Présentation](https://institut-du-numerique-responsable.github.io/skill-nr/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/skill-nr) |
| Gouvernance | **Charte IA Responsable** (INR) | Cadre d'engagement pour une IA éthique et éco-responsable | <https://charter.isit-europe.org/charte-ia/?lang=fr_FR> |
| Formation | 🟢 **MOOC IA Responsable** (Académie NR) | Acculturation des équipes | <https://www.academie-nr.org/mooc-ia/fr/index.html> |

## Fiches liées

- [C1 — Éco-concevoir les services numériques](C1-eco-conception-services.md)
- [C2 — Maîtriser le cycle de vie des données](C2-cycle-vie-donnees.md)
- [I1 — Optimiser infrastructures & environnements](I1-infrastructures.md)
- [D1 — Mettre en œuvre & contrôler la conformité](D1-conformite.md)
