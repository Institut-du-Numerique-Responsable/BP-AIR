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

Traiter l'IA comme n'importe quelle charge du SI : un service qui doit être **utile,
dimensionné et mesuré**. Encadrer son empreinte avant qu'elle ne s'installe, et
articuler cette sobriété avec les obligations de l'AI Act.

## Contexte & enjeu

L'IA générative concentre trois caractéristiques qui la rendent hostile aux réflexes
habituels d'architecture.

**L'empreinte se déplace vers l'inférence.** L'attention se porte sur l'entraînement,
spectaculaire et ponctuel. Mais un service en production appelle son modèle des
milliers de fois par jour, pendant des années : sur la durée de vie, c'est
l'**inférence qui domine le coût total**, énergie comprise. Un modèle entraîné une
fois et mal servi coûte plus qu'un modèle bien servi.

**Le surdimensionnement est la norme.** Le réflexe est d'appeler le modèle le plus
capable disponible, pour toutes les tâches. Or l'écart d'énergie par requête entre
un grand modèle généraliste et un petit modèle spécialisé se compte en **ordres de
grandeur**. Classer un ticket, extraire une date, reformuler un paragraphe : la
plupart des usages métier ne justifient pas la puissance qu'on leur alloue.

**Le GPU inoccupé est le serveur comateux de 2026.** La fiche [I1](I1-infrastructures.md)
rappelle que 25 à 30 % des serveurs tournent sans usage. Le même gaspillage se
reproduit sur des accélérateurs dix fois plus coûteux et bien plus énergivores,
avec en prime une empreinte de fabrication élevée et une tension sur
l'approvisionnement.

S'y ajoutent deux dimensions que le débat carbone masque souvent : la **consommation
d'eau** des datacenters d'inférence (ODD 6), et le **shadow AI**, c'est-à-dire
l'usage d'outils non validés par des collaborateurs, qui cumule empreinte invisible
et fuite de données.

Cf. [guide](../guide-unifie.md#26-pilier-5-architecture-logicielle-sobre-eco-conception).

## Étapes de mise en œuvre

1. **Arbitrer le besoin avant la technologie.** Appliquer la règle des **3U** à l'IA
   elle-même : le service est-il **U**tile, sera-t-il **U**tilisé, est-il
   **U**tilisable ? Puis la question qui fâche : *une solution déterministe
   suffirait-elle ?* Une règle métier, une recherche plein texte ou un modèle
   classique règlent une part importante des cas soumis à un LLM, pour une fraction
   de l'empreinte. Documenter ce choix, il sera réinterrogé.

2. **Dimensionner le modèle par le bas.** Partir du plus petit modèle candidat et
   remonter seulement si le seuil de qualité n'est pas atteint, jamais l'inverse.
   Fixer ce seuil *avant* les essais, sur un jeu d'évaluation représentatif.
   Envisager la **distillation** et la **quantification** pour les usages à volume.

3. **Préférer la RAG au réentraînement.** Pour ancrer un modèle dans des données
   métier, une recherche augmentée coûte structurellement moins qu'un fine-tuning,
   se met à jour sans réentraîner et reste auditable. Réserver l'ajustement fin aux
   cas où le format de sortie ou le domaine l'exigent réellement.

4. **Rendre l'inférence sobre.** Mettre en cache les réponses aux requêtes
   récurrentes ; **grouper les appels** (*batching*) plutôt que les traiter un à un ;
   plafonner la longueur des contextes et des réponses ; couper le *streaming* quand
   il n'apporte rien. Un serveur d'inférence adapté (vLLM, TGI) multiplie le débit à
   matériel constant.

5. **Piloter le taux d'occupation des accélérateurs.** Instrumenter l'usage GPU
   (DCGM, Kepler) au même titre que CPU et RAM en [I1](I1-infrastructures.md).
   Mutualiser les cartes entre équipes, appliquer une politique de **TTL** aux
   environnements d'expérimentation, éteindre les *notebooks* oubliés. Un GPU réservé
   et inactif est le pire poste du SI.

6. **Mesurer l'empreinte par appel et par service.** Instrumenter les appels aux API
   de modèles (EcoLogits) et l'entraînement (CodeCarbon) pour obtenir un coût
   environnemental **par requête**, pas une estimation annuelle. Sans cette
   granularité, aucun arbitrage n'est possible.

7. **Décaler ce qui peut l'être.** Entraînements, réindexations et traitements par
   lots sont des charges flexibles : les planifier aux heures bas-carbone
   (Carbon Aware SDK), à l'inverse de l'inférence interactive.

8. **Gouverner les usages.** Tenir un **inventaire des systèmes d'IA** en production
   ou en test. Il est exigé par l'AI Act et il résout le shadow AI. Y consigner
   finalité, modèle, données d'entraînement, fournisseur et niveau de risque.
   S'appuyer sur la **Charte IA Responsable** de l'INR pour l'engagement, et sur la
   fiche [D1](D1-conformite.md) pour les échéances réglementaires.

9. **Articuler avec la gouvernance des données.** L'IA fournit le meilleur prétexte à
   la rétention indéfinie : « on gardera tout, ça servira à entraîner ». C'est la
   fabrique à *dark data* décrite en [C2](C2-cycle-vie-donnees.md). Les durées de
   conservation s'appliquent aussi aux corpus.

## KPIs & OKR

- **KPI** : énergie et gCO₂e **par requête d'inférence** ; taux d'occupation des GPU ;
  part des requêtes servies par le cache ; part des usages traités par un modèle
  petit ou déterministe ; nombre de systèmes d'IA inventoriés / estimés ; coût mensuel
  par service (proxy FinOps).
- ***OKR*** : inventaire des systèmes d'IA complet et tenu à jour ce semestre ;
  taux d'occupation GPU porté au-dessus de 60 % ; 50 % des appels du service
  principal servis par un modèle plus petit à qualité constante.

## Pièges à éviter

- **Appeler le plus gros modèle par défaut**, faute d'avoir fixé un seuil de qualité.
- Ne mesurer que l'entraînement, alors que la dérive se joue en production, appel après appel.
- Réserver des GPU « pour le projet » et les laisser inactifs entre deux essais.
- Confondre coût facturé et empreinte : une API bon marché n'est pas une API sobre,
  et un forfait masque totalement le signal d'usage.
- Accumuler des corpus « au cas où » et recréer le problème de [C2](C2-cycle-vie-donnees.md).
- Traiter la conformité AI Act comme un sujet juridique séparé : elle impose un
  inventaire et une traçabilité qui sont, précisément, des livrables d'architecture.
- Négliger l'eau et la fabrication en ne raisonnant qu'en kWh.

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils directement mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) est la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Catégorie | Outil / Ressource | Usage | Lien |
|---|---|---|---|
| Mesure | 🟢 **EcoLogits** (GenAI Impact) | Empreinte des appels aux API de LLM, par requête | <https://ecologits.ai> |
| Mesure | 🟢 **CodeCarbon** | Émissions d'un entraînement ou d'un traitement | <https://codecarbon.io> |
| Mesure | 🟢 **ML CO2 Impact** | Estimation rapide avant lancement | <https://mlco2.github.io/impact/> |
| Comparaison | **AI Energy Score** (Hugging Face, Salesforce) | Classement énergétique des modèles par tâche | <https://huggingface.co/spaces/AIEnergyScore/Leaderboard> |
| Occupation GPU | 🟢 **DCGM Exporter** (NVIDIA) | Métriques GPU vers Prometheus | <https://github.com/NVIDIA/dcgm-exporter> |
| Occupation GPU | 🟢 **Kepler** | Énergie des workloads Kubernetes, GPU compris | <https://sustainable-computing.io/> |
| Inférence | 🟢 **vLLM** | Serveur d'inférence à haut débit (batching continu) | <https://github.com/vllm-project/vllm> |
| Planification | 🟢 **Carbon Aware SDK** (GSF) | Décaler entraînements et lots vers les heures bas-carbone | <https://github.com/Green-Software-Foundation/carbon-aware-sdk> |
| Matériel | 🟢 **DataVizta** (Boavizta) | Empreinte de fabrication des serveurs et accélérateurs | <https://dataviz.boavizta.org/> |
| Code | 🟢 **Green Claude** (INR) | Pratiques de sobriété IA et audit d'éco-conception dans l'IDE | [Présentation](https://institut-du-numerique-responsable.github.io/green-claude/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/green-claude) |
| Code | 🟢 **Skill NR** (INR) | Règles d'éco-conception pour 11 assistants IA de code | [Présentation](https://institut-du-numerique-responsable.github.io/skill-nr/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/skill-nr) |
| Gouvernance | **Charte IA Responsable** (INR) | Cadre d'engagement pour une IA éthique et éco-responsable | <https://charter.isit-europe.org/charte-ia/?lang=fr_FR> |
| Formation | 🟢 **MOOC IA Responsable** (Académie NR) | Acculturation des équipes | <https://www.academie-nr.org/mooc-ia/fr/index.html> |

## Fiches liées

- [C1 — Éco-concevoir les services numériques](C1-eco-conception-services.md)
- [C2 — Maîtriser le cycle de vie des données](C2-cycle-vie-donnees.md)
- [I1 — Optimiser infrastructures & environnements](I1-infrastructures.md)
- [D1 — Mettre en œuvre & contrôler la conformité](D1-conformite.md)
