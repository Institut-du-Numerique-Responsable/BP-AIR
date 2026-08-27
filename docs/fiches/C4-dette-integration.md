---
id: C4
titre: Résorber la dette d'intégration
description: >-
  Traiter la dette d'intégration, invisible et non outillée, comme la dette de code : cartographier les flux, réduire les copies de données et chiffrer le coût matériel de chaque échange.
theme: Conception sobre
statut: brouillon
proprietaire: INR/ISIT
contributeurs: []
reviewers: []
version: 0.1
maj: 2026-08-28
fiches_liees: [C1, C2, I1, M1]
---

# C4 — Résorber la dette d'intégration

> **Public cible.** Architectes d'entreprise, urbanistes SI, architectes d'intégration, Ops, Data.

## Objectif

Piloter le SI comme un système d'échanges. Réduire le nombre de flux, les copies
d'une même donnée et les couplages, en chiffrant ce que chacun coûte en matériel et
en énergie.

## Contexte & enjeu

Vous outillez la dette de code depuis quinze ans : linters, analyse statique, seuils
de couverture, tout cela bloque une *pull request*. La dette d'intégration n'a rien
de comparable. Aucun outil ne la mesure par défaut, aucune équipe ne la porte, et
elle grossit à chaque projet qu'on livre.

**Elle croît plus vite que le SI.** Vingt applications reliées deux à deux
autorisent jusqu'à 190 liaisons. Chaque application ajoutée sans urbanisation
multiplie les points de contact, et vous héritez d'un graphe que personne ne sait
dessiner en entier. Le guide rappelle qu'une cartographie tenue à jour fait baisser
les coûts d'exploitation de 20 à 30 %
([Forrester, 2021](../guide-unifie.md#23-pilier-2-urbanisation-architecture-en-couches)).

**Elle se paie en serveurs.** Les revues d'architecture comptent les licences et
s'arrêtent là. Un flux de réplication nocturne maintient allumés un serveur
d'intégration, une baie de stockage et un lien réseau, pour recopier une donnée que
vous détenez déjà. Une donnée de référence dupliquée cinq fois occupe
cinq fois le stockage, et le stockage porte son empreinte de fabrication avant
même d'être branché. Un broker déployé en cluster pour la haute disponibilité,
c'est trois serveurs de plus, allumés en permanence, pour transporter des messages
dont une partie n'a plus de destinataire.

**Le matériel vous rattrape.** Pendant vingt ans, vous avez pu raisonner en
abstractions : la capacité suivait, l'énergie n'apparaissait pas sur votre facture,
le matériel arrivait en quelques semaines. Depuis, la tension sur les composants, le
prix de l'électricité et les datacenters qui refusent des raccordements ont changé
l'équation. Le guide pose la règle : **80 % de l'empreinte d'un équipement est figée
dès sa fabrication**. Le serveur que vous ajoutez pour porter un flux arrive avec sa
dette environnementale constituée, avant son premier message traité.

**Le découpage en microservices fabrique de la dette d'intégration.** Laissez le
débat « microservices ou monolithe » aux conférences et posez la question du seuil :
à partir de quelle granularité le coût de coordination dépasse-t-il le bénéfice
d'autonomie ? Sa version matérielle se compte. Chaque service porte son
runtime, son *sidecar* de service mesh, ses répliques minimales pour la haute
disponibilité et sa collecte d'observabilité. Quarante services en trois répliques,
ce sont cent vingt instances, chacune avec un plancher de RAM et de CPU que personne
ne consomme. Un appel qui coûtait un saut en mémoire devient une sérialisation, un
chiffrement TLS et un aller-retour réseau. Le tracing distribué génère ensuite un
volume de données proportionnel au nombre de sauts que vous avez créés.

Chaque flux redondant immobilise du matériel qui aurait servi ailleurs, ou qui
n'aurait pas eu besoin d'être acheté.

Cf. [guide](../guide-unifie.md#23-pilier-2-urbanisation-architecture-en-couches).

## Étapes de mise en œuvre

1. **Cartographier les flux, pas seulement les applications.** La plupart des
   cartographies listent des briques et taisent ce qui circule entre elles.
   Recenser pour chaque flux sa source, sa destination, sa fréquence, son volume,
   son protocole et **son propriétaire métier**. Un flux sans propriétaire est un
   candidat au décommissionnement.

2. **Partir des flux réels, pas des flux documentés.** L'écart entre les deux est
   la mesure de votre dette. Le tracing distribué (OpenTelemetry) et le *lineage*
   de données (OpenLineage, OpenMetadata) montrent ce qui circule vraiment,
   y compris les échanges qu'aucun schéma n'a jamais décrits.

3. **Mesurer la dette.** Nombre de flux inter-applicatifs, part de liaisons
   point-à-point, nombre de copies de chaque donnée de référence, volume répliqué
   chaque nuit, flux sans consommateur identifié. Ces cinq chiffres suffisent à
   ouvrir la discussion en comité d'architecture.

4. **Appliquer la règle des 3U aux flux.** Ce flux est-il **U**tile, est-il
   **U**tilisé, est-il **U**tilisable par d'autres que son créateur ? La fiche
   [C1](C1-eco-conception-services.md) applique la règle aux fonctionnalités, elle
   vaut autant pour les échanges.

5. **Réduire les copies avant d'optimiser les transports.** Une donnée de référence
   servie par une API à la demande remplace cinq réplications nocturnes et les
   serveurs qui les portent. Établir le référentiel maître avec
   [C2](C2-cycle-vie-donnees.md), puis supprimer les copies devenues inutiles.

6. **Interroger la granularité du découpage.** Pour chaque service, poser le test de
   Conway : quelle équipe en est propriétaire, et livre-t-elle sur son propre cycle ?
   Si la même équipe possède douze services, le découpage n'achète aucune autonomie
   et facture toute la complexité, en coordination comme en instances. Regrouper vers
   un monolithe modulaire est une décision d'architecture recevable, pas un aveu.
   Rapporter le plancher de ressources (instances × réplicas × RAM réservée) à la
   charge servie donne le chiffre qui tranche.

7. **Découpler par le contrat plutôt que par l'outillage.** Un schéma versionné et
   testé (OpenAPI, AsyncAPI, tests de contrat) découple deux équipes sans ajouter
   d'infrastructure. Un ESB inséré au milieu de flux non rationalisés ajoute une
   couche à maintenir et un cluster à alimenter, sans réduire le nombre d'échanges.

8. **Chiffrer le coût physique de l'intégration.** Combien de serveurs, de stockage
   et de bande passante vos échanges mobilisent-ils ? Rapprocher ce chiffrage du
   suivi FinOps de [I1](I1-infrastructures.md) et de l'empreinte de fabrication
   (DataVizta). Un flux dont personne ne défend le coût matériel se supprime plus
   facilement qu'un flux discuté sur des principes.

9. **Décommissionner par lots, avec un filet.** Couper d'abord en observation
   (le flux tourne, plus personne ne le lit), mesurer l'absence de réclamation
   pendant un cycle métier complet, puis supprimer et rendre le matériel.

10. **Poser une règle d'entrée.** Toute nouvelle application déclare ses flux, leur
   propriétaire et leur durée de vie prévue avant d'entrer en production. Sans cette
   règle, vous recommencerez la cartographie dans trois ans.

## KPIs & OKR

- **KPI** : nombre de flux inter-applicatifs ; part de liaisons point-à-point ;
  nombre de copies par donnée de référence ; volume répliqué par nuit ; flux sans
  propriétaire déclaré ; serveurs et stockage dédiés à l'intégration ; écart entre
  flux documentés et flux observés ; **plancher de ressources réservé rapporté à la
  charge servie** ; nombre de services par équipe propriétaire.
- ***OKR*** : cartographie des flux complète et datée ce semestre ; toute donnée de
  référence ramenée à deux copies au plus ; 20 % de liaisons point-à-point
  supprimées sur l'année, avec le matériel correspondant rendu.

## Pièges à éviter

- Acheter un ESB ou un iPaaS pour traiter la dette d'intégration. Vous ajoutez une
  couche et un cluster à alimenter pendant que le nombre de flux reste le même.
- Surveiller la qualité du code et ignorer ce qui circule entre les applications.
- Cartographier une fois, publier un joli schéma, puis le laisser vieillir. Une
  carte fausse coûte plus cher que pas de carte.
- Supprimer un flux sans avoir identifié ses consommateurs, y compris le tableur
  d'un service que personne n'a déclaré.
- Compter l'intégration en licences et jamais en serveurs, en stockage ni en kWh.
- Confondre découplage et indirection : passer par un intermédiaire de plus ne
  découple rien si les deux extrémités partagent toujours le même modèle.
- Découper en microservices sans équipes autonomes en face. Vous payez le réseau,
  les répliques et le *sidecar* pour une autonomie que l'organisation n'exerce pas.
- Traiter le regroupement de services comme un retour en arrière. Le monolithe
  modulaire redonne des appels en mémoire et divise le plancher de ressources.

## Outils & ressources

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
- [I1 — Optimiser infrastructures & environnements](I1-infrastructures.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)
