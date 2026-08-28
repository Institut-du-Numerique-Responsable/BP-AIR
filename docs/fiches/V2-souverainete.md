---
id: V2
titre: Souveraineté et réversibilité
description: >-
  Garder la main sur son SI : mesurer le coût de sortie avant de s'engager, exercer la réversibilité plutôt que la contractualiser, et distinguer les charges qui exigent une localisation des autres.
theme: Chaîne de valeur
statut: brouillon
proprietaire: INR/ISIT
contributeurs: []
reviewers: []
version: 0.1
maj: 2026-08-28
fiches_liees: [V1, I2, I3, D1]
---

# V2 — Souveraineté et réversibilité

> **Public cible.** Architectes, DSI, achats, juridique, RSSI, DPO.

## Objectif

Rester capable de changer de fournisseur, de récupérer ses données et de maîtriser
où elles résident. Traiter la souveraineté comme une propriété d'architecture qui se
mesure et s'exerce, au-delà des seules clauses contractuelles.

## Contexte et enjeux

**Le verrouillage ne se joue pas sur le calcul.** Migrer des machines virtuelles
d'un fournisseur à un autre reste faisable. Ce qui vous retient, ce sont les
services managés propriétaires, les formats de données spécifiques, les identités
et les droits, et le volume à extraire. Un SI construit sur des briques génériques
change de fournisseur ; un SI construit sur les services différenciants d'un
fournisseur reste où il est.

**La question n'est pas binaire.** Exiger la souveraineté partout coûte cher et
prive de services utiles. La classer par charge donne un résultat exploitable :
certaines données ne doivent pas sortir d'un périmètre juridique, d'autres sont
publiques et indifférentes. L'architecte trace cette frontière, le juridique la
qualifie, la direction l'arbitre.

**Une clause ne suffit pas à garantir la réversibilité.** Seul un exercice permet de
vérifier l'export des données, sa durée et leur réutilisation dans un autre outil.
Le coût de sortie s'estime avant la signature, lorsque l'organisation dispose encore
d'un pouvoir de négociation.

**Le cadre européen a bougé.** Le **Data Act** impose depuis le 12 septembre 2025 aux
fournisseurs de services de traitement de données de lever les obstacles au
changement : préavis de deux mois à l'initiative du client, période de transition
de 30 jours suivie de 30 jours de récupération, et suppression progressive des frais
de transfert. **DORA**, applicable depuis janvier 2025, impose au secteur financier
une stratégie de risque sur les tiers et des stratégies de sortie documentées. Ces
textes transforment une bonne pratique en obligation, et ils donnent un levier de
négociation à vos achats ([D1](D1-conformite.md)).

**La souveraineté sert la sobriété, et l'inverse.** Les standards ouverts et les
formats interopérables réduisent les conversions, les couches d'adaptation et les
duplications de données. Ce que vous gagnez en liberté de mouvement, vous le gagnez
aussi en flux supprimés ([C4](C4-dette-integration.md)).

## Étapes de mise en œuvre

1. **Classer les charges avant de choisir les hébergements.** Trois catégories
   suffisent : données dont la localisation est contrainte par la loi ou par le
   contrat, données sensibles sans contrainte formelle, données indifférentes.
   Faire qualifier la première catégorie par le juridique, pas par l'architecte
   seul.

2. **Cartographier les dépendances propriétaires.** Pour chaque service managé
   utilisé, noter s'il existe un équivalent standard ou open source, et ce que
   coûterait la bascule. Cette liste est votre inventaire de verrouillage. Elle
   tient sur une page et personne ne l'écrit jamais.

3. **Estimer le coût de sortie avant de signer.** Volume à extraire, frais de
   transfert, durée d'indisponibilité, réécriture applicative, compétences à
   acquérir. Un chiffre, même approximatif, change la négociation. Le
   [clausier NR de l'INR](https://institutnr.org/clausier-numerique-ecoresponsable)
   fournit des clauses types à intégrer aux CCTP ([I2](I2-achats-responsables.md)).

4. **Exercer la réversibilité, ne pas la contractualiser seulement.** Programmer un
   export complet par an sur les services critiques, mesurer sa durée, vérifier que
   les données importées sont exploitables dans un autre outil. C'est le même
   principe que l'exercice de reprise de [I3](I3-resilience.md), pour la même
   raison : une procédure jamais jouée est une hypothèse.

5. **Préférer les standards ouverts aux interfaces propriétaires.** À service rendu
   équivalent, une brique conforme à un standard documenté vous laisse une porte de
   sortie. Cette préférence se décide au moment du choix, quand elle est gratuite,
   et coûte cher trois ans plus tard.

6. **Négocier la localisation et l'accès aux données.** Où résident les données au
   repos, où transitent-elles, quelles juridictions peuvent y accéder, et selon
   quelles procédures. Les qualifications nationales et européennes
   (SecNumCloud en France, travaux EUCS au niveau européen) donnent un langage
   commun aux achats.

7. **Évaluer la concentration du risque.** Combien de vos services critiques
   dépendent du même fournisseur, et que se passe-t-il s'il change ses conditions,
   augmente ses tarifs ou se retire d'un marché ? Cette question relève de
   l'architecture autant que des achats, et rejoint l'analyse de fragilité de
   [I3](I3-resilience.md).

8. **Documenter l'arbitrage, pas seulement la décision.** Écrire ce que vous avez
   accepté comme dépendance et pourquoi. Un successeur qui trouve la décision sans
   son motif la reproduit ou la défait au hasard.

## Indicateurs et objectifs

- **KPI** : part des services critiques disposant d'une stratégie de sortie
  documentée ; coût de sortie estimé, par fournisseur ; date du dernier export de
  réversibilité réussi ; part des données soumises à contrainte de localisation
  effectivement conformes ; nombre de services critiques concentrés sur un même
  fournisseur ; part des interfaces reposant sur un standard ouvert.
- ***OKR*** : classification des charges par contrainte de localisation achevée ce
  semestre ; un exercice de réversibilité réel sur le service le plus critique ;
  coût de sortie chiffré pour les trois principaux fournisseurs.

## Pièges à éviter

- Confondre clause de réversibilité et réversibilité. Tant que l'export n'a pas été
  exécuté et le résultat vérifié, vous avez un document, pas une capacité.
- Traiter la souveraineté en tout ou rien, et payer une exigence maximale sur des
  données publiques.
- Adopter le multicloud comme assurance. Vous multipliez les compétences, les coûts
  et les surfaces d'attaque, souvent au-delà du risque couvert.
- Estimer le coût de sortie au moment de partir. Il se chiffre avant la signature,
  quand vous avez encore un pouvoir de négociation.
- Négliger les identités et les droits. Ils sont le point de verrouillage le plus
  profond et le moins visible du dossier de migration.
- Réduire la souveraineté à la localisation physique des serveurs, en ignorant la
  juridiction qui s'applique au fournisseur.

## Outils et ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Catégorie | Outil / Ressource | Usage | Lien |
|---|---|---|---|
| Cadre | **Data Act** | Obligations de changement de fournisseur applicables depuis le 12 septembre 2025 | <https://digital-strategy.ec.europa.eu/en/policies/data-act> |
| Cadre | **DORA** | Stratégies de sortie et risque sur les tiers, secteur financier | <https://www.digital-operational-resilience-act.com/> |
| Qualification | **SecNumCloud** (ANSSI) | Qualification française des offres cloud de confiance | <https://cyber.gouv.fr/secnumcloud> |
| Écosystème | **Gaia-X** | Cadre européen d'interopérabilité et de portabilité | <https://gaia-x.eu/> |
| Achats | 🟢 **Clausier NR** (INR) | Clauses types pour CCTP et CCAP, réversibilité comprise | <https://institutnr.org/clausier-numerique-ecoresponsable> |
| Alternatives | 🟢 **Socle interministériel de logiciels libres** | Logiciels libres recommandés par l'État | <https://code.gouv.fr/fr/> |
| Alternatives | 🟢 **OpenStack** / 🟢 **OpenNebula** | Socles d'infrastructure ouverts | <https://openstack.org> |
| Données | **CNIL** | Transferts hors UE et bases légales | <https://www.cnil.fr> |
| Maturité | 🟢 **Guide Maturité PP** (INR/ISIT) | Évaluation des fournisseurs, complète l'analyse de dépendance | <https://institutnr.org/guide-maturite-parties-prenantes> |

## Fiches liées

- [V1 — Évaluer et influencer la maturité des parties prenantes](V1-maturite-parties-prenantes.md)
- [I2 — Politique d'achats numériques responsables](I2-achats-responsables.md)
- [I3 — Arbitrer résilience et sobriété](I3-resilience.md)
- [D1 — Mettre en œuvre et contrôler la conformité](D1-conformite.md)
