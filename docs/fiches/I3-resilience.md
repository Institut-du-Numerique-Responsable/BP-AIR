---
id: I3
titre: Arbitrer résilience et sobriété
description: >-
  Dimensionner la résilience d'un SI au risque réel plutôt qu'au réflexe : chaque niveau de redondance immobilise du matériel, chaque technologie orpheline crée une fragilité que l'infrastructure ne rattrape pas.
theme: Infrastructure et matériel
statut: brouillon
proprietaire: INR/ISIT
contributeurs: []
reviewers: []
version: 0.1
maj: 2026-08-28
fiches_liees: [I1, C4, M2, V2]
---

# I3 — Arbitrer résilience et sobriété

> **Public cible.** Architectes, équipes d'exploitation, ingénieurs de fiabilité (SRE), RSSI, responsables des plans de continuité et de reprise, direction technique.

## Objectif

Dimensionner la résilience au risque que vous acceptez de couvrir, en assumant ce
que chaque niveau de redondance coûte en matériel. Traiter aussi les fragilités que
l'infrastructure ne rattrape pas : technologies orphelines, compétences détenues par
une seule personne, fournisseur unique.

## Contexte et enjeux

La résilience traverse la matrice KPI du guide, colonne entière, de la couche
fonctionnelle à la couche matérielle. Aucune fiche ne la portait jusqu'ici, et la
démarche NR l'abordait par la marge.

**Redonder consomme du matériel.** C'est la tension centrale de cette fiche, et le
guide ne la résout pas d'un côté ou de l'autre. Un service actif-actif sur deux
régions double les serveurs, le stockage et la bande passante inter-sites, avec
l'empreinte de fabrication qui va avec. Un troisième réplica pour un quorum ajoute
50 % de matériel pour une disponibilité marginale que la plupart des services ne
consomment jamais. Ces choix se prennent en réunion d'architecture et se paient en
équipements pendant cinq ans.

**Le surdimensionnement se présente comme une mesure de prudence.** Les équipes sont
davantage tenues responsables des interruptions que du coût d'une redondance
excessive. Cette asymétrie favorise des architectures fondées sur la crainte plutôt
que sur un objectif de disponibilité écrit et arbitré. Un service interne consulté
aux heures ouvrées ne requiert pas le même dispositif qu'un service de paiement.

**Les vraies fragilités sont ailleurs que dans le matériel.** La matrice du guide
les nomme : technologies orphelines, fonctions dupliquées sans référentiel, serveurs
dont plus personne ne connaît la fonction, rotation des équipes projet. Aucune
redondance matérielle ne compense un composant que son mainteneur a abandonné, ni
une procédure de reprise que personne n'a exécutée depuis trois ans.

**La contrainte physique change le calcul.** Reconstituer un parc après un incident
suppose du matériel disponible. Les délais d'approvisionnement se sont allongés, et
un plan de reprise qui suppose une livraison en trois semaines repose sur une
hypothèse qui n'est plus vraie. La sobriété rejoint ici la résilience : un SI plus
léger se reconstitue plus vite.

Voir le [guide](../guide-unifie.md#29-le-retour-de-la-contrainte-physique).

## Étapes de mise en œuvre

1. **Écrire les objectifs par service, pas par défaut.** RTO et RPO négociés avec le
   métier, service par service, écrits et signés. Sans cet arbitrage, chaque équipe
   applique le niveau maximal qu'elle sait déployer. Classer les services en trois
   niveaux suffit : critique, important, standard.

2. **Chiffrer chaque niveau de redondance en matériel.** Combien de serveurs, de
   stockage et de liens pour passer de standard à important, puis à critique ?
   Présenter ce chiffrage au métier avec le coût et l'empreinte associés
   ([I1](I1-infrastructures.md), DataVizta). Une direction qui voit le prix de la
   quatrième neuf révise souvent son exigence.

3. **Recenser les technologies orphelines.** Pour chaque brique du socle : dernière
   version publiée, activité du mainteneur, existence d'un successeur. Un composant
   sans publication depuis dix-huit mois entre en surveillance. La dépendance
   abandonnée est le point de rupture que les tests de charge ne révèlent jamais.

4. **Recenser les points uniques humains.** Quelle procédure ne sait exécuter qu'une
   seule personne ? Quel composant n'a qu'un mainteneur interne ? La rotation des
   équipes figure dans la matrice KPI du guide pour cette raison. Documenter et
   faire tourner coûte moins qu'un départ non anticipé.

5. **Exécuter les procédures de reprise pour de vrai.** Une bascule jamais jouée est
   une hypothèse, pas un plan. Programmer des exercices réels, y compris la
   restauration de sauvegardes, et mesurer l'écart avec le RTO annoncé. L'ingénierie
   du chaos (Chaos Toolkit, LitmusChaos) automatise cette vérification en continu.

6. **Préférer la simplicité à la redondance.** Supprimer un composant retire un mode
   de panne et le matériel qui le portait. La réduction des flux de
   [C4](C4-dette-integration.md) sert la résilience autant que la sobriété : moins
   de dépendances, moins de chemins de rupture, moins de machines à maintenir.

7. **Dégrader plutôt que tomber.** Prévoir un mode dégradé explicite, en lecture
   seule ou à fonctionnalités réduites, plutôt qu'une bascule complète coûteuse.
   Un service qui perd sa recherche mais garde sa consultation rend encore service,
   pour une fraction de l'infrastructure.

8. **Étendre l'analyse aux fournisseurs.** Vos dépendances externes portent une part
   de votre disponibilité. Croiser avec [V1](V1-maturite-parties-prenantes.md) pour
   la maturité, et avec [V2](V2-souverainete.md) pour la réversibilité et la
   concentration du risque sur un fournisseur unique.

9. **Suivre l'écart entre le prévu et le constaté.** Disponibilité réelle rapportée
   à l'objectif, RTO mesuré en exercice rapporté au RTO annoncé. Un objectif dépassé
   de façon constante signale une redondance à réduire, donc du matériel à rendre.

## Indicateurs et objectifs

- **KPI** : part des services dotés d'un RTO et d'un RPO écrits ; disponibilité
  constatée rapportée à l'objectif, par niveau de service ; nombre de composants
  sans publication depuis dix-huit mois ; nombre de procédures critiques exécutables
  par une seule personne ; date du dernier exercice de reprise réussi ; matériel
  immobilisé par la redondance, en serveurs et en tonnes de CO₂e.
- ***OKR*** : tous les services critiques dotés d'objectifs écrits et signés ce
  semestre ; un exercice de reprise réel par trimestre sur le périmètre critique ;
  inventaire des technologies orphelines établi et présenté au comité d'architecture.

## Pièges à éviter

- Appliquer le niveau de résilience maximal partout, faute d'objectifs négociés.
  Vous payez le dispositif d'un service de paiement pour un intranet.
- Confondre redondance et résilience. Trois copies d'un composant fragile donnent
  trois composants fragiles.
- Écrire un plan de reprise sans jamais l'exécuter, puis découvrir en incident que
  les sauvegardes ne se restaurent pas.
- Bâtir un plan de reprise sur une hypothèse d'approvisionnement matériel de trois
  semaines qui ne tient plus.
- Traiter la résilience comme un sujet d'infrastructure. Une technologie orpheline
  et un mainteneur unique cassent un SI que la redondance protège parfaitement.
- Multiplier les régions cloud pour la résilience et créer un couplage nouveau,
  celui du plan de contrôle du fournisseur.

## Outils et ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Catégorie | Outil / Ressource | Usage | Lien |
|---|---|---|---|
| Vérification | 🟢 **Chaos Toolkit** | Exercices d'injection de panne automatisés | <https://www.chaostoolkit.org/> |
| Vérification | 🟢 **LitmusChaos** | Ingénierie du chaos sur Kubernetes | <https://litmuschaos.io/> |
| Obsolescence | 🟢 **CNCF Landscape** | Maturité et activité des briques du socle | <https://landscape.cncf.io> |
| Observabilité | 🟢 **Prometheus + Grafana** | Disponibilité constatée par service | <https://grafana.com> |
| Empreinte | 🟢 **DataVizta** (Boavizta) | Coût environnemental du matériel de redondance | <https://dataviz.boavizta.org/> |
| Coût | 🟢 **OpenCost** | Coût de la redondance par service | <https://www.opencost.io/> |
| Cadre | **NIS2** | Exigences de résilience pour les entités essentielles et importantes | <https://www.enisa.europa.eu/> |
| Cadre | **DORA** | Résilience opérationnelle du secteur financier, applicable depuis janvier 2025 | <https://www.digital-operational-resilience-act.com/> |
| Référentiel | 🟢 **GR491** (INR) | Critères de durabilité et de robustesse | <https://gr491.isit-europe.org/> |

## Fiches liées

- [I1 — Optimiser infrastructures et environnements](I1-infrastructures.md)
- [C4 — Résorber la dette d'intégration](C4-dette-integration.md)
- [V2 — Souveraineté et réversibilité](V2-souverainete.md)
- [M2 — Pilotage et tableau de bord KPI](M2-pilotage-kpi.md)
