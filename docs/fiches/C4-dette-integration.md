---
id: C4
titre: Résorber la dette d'intégration
description: >-
  Cartographier les flux, réduire les échanges et les copies de données inutiles, puis mesurer les ressources mobilisées par l'intégration.
theme: Conception sobre
statut: brouillon
proprietaire: INR/ISIT
contributeurs: []
reviewers: []
version: 0.2
maj: 2026-08-28
fiches_liees: [C1, C2, I1, M1]
---

# C4 — Résorber la dette d'intégration

> **Public cible.** Architectes d'entreprise, urbanistes SI, architectes d'intégration, équipes d'exploitation et spécialistes des données.

## Objectif

Identifier et réduire les échanges, les copies de données et les dépendances qui
complexifient inutilement le système d'information. Évaluer leurs coûts techniques,
économiques et environnementaux afin d'éclairer les décisions d'architecture.

## Contexte et enjeux

La dette d'intégration apparaît lorsque les échanges s'accumulent, évoluent sans
maîtrise suffisante ou demeurent en service après la disparition de leur besoin.
Elle se traduit par des flux redondants, des données dupliquées, des contrats
d'interface fragiles et des composants techniques maintenus sans usage identifié.

Cette dette reste souvent moins visible que la dette de code. Les organisations
disposent d'outils pour analyser le code, mais rarement d'une cartographie fiable
des flux, de leurs propriétaires et des ressources qu'ils mobilisent.

Chaque échange peut solliciter du calcul, du stockage, du réseau et des mécanismes
d'observabilité. La multiplication des interfaces augmente aussi les coûts
d'exploitation et les risques d'incident. L'enjeu consiste donc à supprimer les
flux inutiles, à rationaliser les copies de données et à adapter les solutions
d'intégration aux besoins réels.

Les architectures distribuées, notamment celles fondées sur des microservices,
demandent une attention particulière. Elles peuvent apporter de l'autonomie lorsque
les services correspondent à des responsabilités clairement délimitées et peuvent
évoluer indépendamment lorsque le besoin le justifie. Un découpage trop fin peut
cependant multiplier les communications réseau, les instances et les données
techniques sans bénéfice équivalent.

Voir le [guide](../guide-unifie.md#23-pilier-2-urbanisation-et-architecture-en-couches).

## Étapes de mise en œuvre

1. **Recenser les flux et leurs caractéristiques.** Pour chaque échange, relever la
   source, la destination, les données transportées, le protocole, la fréquence, le
   volume, la criticité, le mode de déclenchement, les garanties de livraison et,
   le cas échéant, la durée de conservation des données produites. Compléter la
   cartographie des applications par une vue des flux qui les relient.

2. **Comparer les flux déclarés aux échanges observés.** Croiser la documentation
   avec les journaux, les traces, les métriques réseau et les configurations des
   ordonnanceurs, brokers, passerelles API et mécanismes de transfert de fichiers.
   Le traçage et le lignage complètent l'inventaire lorsque les systèmes sont
   instrumentés ; ils ne dispensent pas d'échanger avec les exploitants et les
   consommateurs. Analyser chaque écart avant de mettre la cartographie à jour.

3. **Identifier les responsables et les consommateurs.** Associer à chaque flux un
   propriétaire métier, un responsable technique et la liste de ses consommateurs.
   L'absence de responsable ou de consommateur déclenche une analyse ; elle ne suffit
   pas à décider d'une suppression.

4. **Mesurer les ressources mobilisées.** Suivre le volume transféré, le stockage
   des copies, la bande passante, les traitements et les ressources réservées aux
   composants d'intégration. Relier ces mesures au suivi FinOps de
   [I1](I1-infrastructures.md) et, lorsque les données sont disponibles, à
   l'empreinte environnementale des équipements.

5. **Évaluer l'utilité et la criticité.** Appliquer la règle des 3U : le flux est-il
   **u**tile, **u**tilisé et **u**tilisable par d'autres ? Compléter cette analyse par
   les exigences de sécurité, de conformité, de continuité d'activité et de qualité
   des données. La fiche [C1](C1-eco-conception-services.md) applique la même règle
   aux fonctionnalités.

6. **Rationaliser les copies et les interfaces.** Définir le référentiel maître avec
   [C2](C2-cycle-vie-donnees.md), puis supprimer les copies sans usage démontré.
   Choisir le mécanisme d'intégration selon le besoin : API pour une réponse
   immédiate, événement ou message pour découpler les rythmes et absorber les
   indisponibilités, transfert par lot lorsque la fraîcheur attendue le permet. Une
   médiation ESB ou iPaaS peut centraliser certains contrôles ou certaines
   transformations, mais elle ne remplace ni la réduction des flux ni la maîtrise
   des contrats. Évaluer les dépendances temporelles, les garanties de livraison,
   l'idempotence, la reprise et la cohérence attendue. Versionner les contrats
   d'interface et les vérifier par des tests.

7. **Réexaminer le découpage des services.** Vérifier que chaque service porte une
   responsabilité cohérente et que son déploiement séparé répond à un besoin
   explicite : autonomie d'évolution, isolation des risques, exigences de sécurité,
   disponibilité ou caractéristiques de charge. Comparer ce bénéfice au coût des
   instances, des communications réseau et de l'observabilité. Regrouper des services
   peut être pertinent lorsque leur séparation n'apporte pas le bénéfice attendu.

8. **Décommissionner progressivement et prévoir le retour arrière.** Confirmer les
   dépendances déclarées et observées, y compris les traitements périodiques. Définir
   les critères d'arrêt, la durée d'observation et la fenêtre de retour arrière.
   Lorsque c'est possible, suspendre les nouveaux échanges de manière réversible,
   placer le consommateur en lecture seule ou exécuter le flux en parallèle sans
   effet métier, selon le mécanisme concerné. Après l'arrêt, surveiller les erreurs,
   les files d'attente, les rejets et les écarts de données pendant la période
   convenue. Ne supprimer les configurations et les ressources qu'après validation
   des responsables métier et techniques. Archiver ou supprimer les données selon
   les règles de conservation, de conformité et de sécurité applicables. Toute
   nouvelle application doit déclarer ses flux, leurs responsables et leur durée de
   vie avant sa mise en production.

## Indicateurs et objectifs

- **KPI** : part des flux critiques documentés ; part des flux disposant d'un
  propriétaire métier et d'un responsable technique ; écart entre les flux déclarés
  et les flux observés ; nombre de copies sans usage démontré ; volume de données
  transféré ; ressources réservées aux composants d'intégration ; nombre de flux
  arrêtés et ressources libérées.
- ***OKR 1*** : documenter 100 % des flux classés critiques, avec leurs responsables,
  leurs consommateurs et une date de réexamen.
- ***OKR 2*** : après établissement de la référence initiale, fixer une cible datée
  de suppression des flux redondants et des copies sans usage, puis mesurer les
  arrêts validés.

## Pièges à éviter

- Déployer un nouvel outil d'intégration avant d'avoir rationalisé les flux.
- Limiter la cartographie aux applications sans représenter les échanges.
- Laisser la cartographie vieillir sans responsable ni fréquence de mise à jour.
- Supprimer un flux sur la seule base de l'absence de propriétaire déclaré.
- Mesurer uniquement les licences et ignorer le calcul, le stockage et le réseau.
- Considérer qu'un intermédiaire technique suffit à découpler les systèmes sans
  contrats maîtrisés, responsabilités claires ni gestion indépendante de leurs
  évolutions.
- Découper les services plus finement que ne le justifient les responsabilités des
  équipes et les besoins d'évolution.
- Décommissionner sans observation préalable, validation des consommateurs ni
  procédure de rétablissement.

## Outils et ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Catégorie | Outil / Ressource | Usage | Lien |
|---|---|---|---|
| Cartographie | 🟢 **Archi** (ArchiMate) | Modélisation d'architecture d'entreprise, cartographie des flux | <https://www.archimatetool.com/> |
| Cartographie | 🟢 **Backstage** | Catalogue de services avec propriétaire et dépendances déclarés | <https://backstage.io> |
| Flux réels | 🟢 **OpenTelemetry** | Tracing distribué : découvrir les échanges non documentés | <https://opentelemetry.io> |
| Lignage données | 🟢 **OpenLineage** | Standard de traçage des flux de données | <https://openlineage.io> |
| Lignage données | 🟢 **Marquez** | Collecte et visualisation du lignage OpenLineage | <https://marquezproject.ai/> |
| Catalogue données | 🟢 **OpenMetadata** | Catalogue, lignage et repérage des copies redondantes | <https://open-metadata.org> |
| Contrats | 🟢 **OpenAPI** / 🟢 **AsyncAPI** | Contrats versionnés pour API synchrones et événementielles | <https://www.asyncapi.com> |
| Contrats | 🟢 **Pact** | Tests de contrat entre consommateurs et fournisseurs | <https://pact.io> |
| Coût matériel | 🟢 **OpenCost** | Coût par service, y compris briques d'intégration | <https://www.opencost.io/> |
| Empreinte | 🟢 **DataVizta** (Boavizta) | Empreinte de fabrication des serveurs et du stockage mobilisés | <https://dataviz.boavizta.org/> |
| Référentiel | 🟢 **GR491** (INR) | Critères d'architecture et d'urbanisation | <https://gr491.isit-europe.org/> |

## Fiches liées

- [C1 — Éco-concevoir les services numériques](C1-eco-conception-services.md)
- [C2 — Maîtriser le cycle de vie des données](C2-cycle-vie-donnees.md)
- [I1 — Optimiser infrastructures et environnements](I1-infrastructures.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)
