---
id: D1
titre: Mettre en œuvre & contrôler la conformité
description: >-
  Mettre en œuvre et contrôler la conformité numérique responsable : l'architecte passe de concepteur à coach et contrôleur des standards NR.
theme: Déploiement & Valorisation
statut: brouillon
proprietaire: INR/ISIT
contributeurs: [Guillaume Gallon]
reviewers: []
version: 0.1
maj: 2026-06-04
fiches_liees: [G4, C1, D2]
---

# D1 — Mettre en œuvre & contrôler la conformité

> **Public cible.** Architectes, équipes projet, Ops, QA.

## Objectif

Déployer concrètement les chantiers tout en garantissant le respect des standards NR : l'architecte passe de concepteur à coach et contrôleur.

## Contexte & enjeu

La conformité se vérifie, elle ne se décrète pas. Des standards définis sans outillage de contrôle restent lettre morte ; un contrôle vécu comme friction est rejeté. Cf. [guide](../guide-unifie.md#23-pilier-2-urbanisation-architecture-en-couches).

## Le cadre réglementaire

Les textes ci-dessous contraignent votre SI, avec des échéances datées. Ces dates
pèsent autant que les obligations : une direction arbitre et budgète un chantier daté
là où elle repousse un *nice-to-have*. La fiche [G1](G1-mandat.md) y trouve son
argument.

| Texte | Qui est concerné | Échéance | Ce que ça implique pour le SI |
|---|---|---|---|
| **AI Act**, règlement (UE) 2024/1689 | Fournisseurs et **déployeurs** de systèmes d'IA | Interdictions et obligations GPAI déjà applicables ; **application générale au 2 août 2026** ; exigences substantielles pour le haut risque annexe III repoussées au **2 décembre 2027** par l'omnibus numérique (règlement (UE) 2026/1744), annexe I au **2 août 2028** | Inventaire des systèmes d'IA, classification par niveau de risque, transparence envers les utilisateurs, traçabilité. Cf. [C3](C3-ia-sobre.md) |
| **CSRD** et normes **ESRS** | Après l'omnibus, seuils **cumulatifs** : plus de 1 000 salariés **et** plus de 450 M€ de CA | Vague 1 inchangée (rapport 2025 sur l'exercice 2024) ; **vague 2 : premier rapport en 2028** sur l'exercice 2027 ; ESRS révisés obligatoires pour les exercices ouverts en 2027 | Le SI devient fournisseur de données extra-financières auditables : traçabilité des consommations, périmètre Scope 3, fraîcheur des chiffres. Cf. [M2](M2-pilotage-kpi.md) |
| **Loi REEN** (2021-1485), art. 35 | Communes et EPCI de **plus de 50 000 habitants** | Programme de travail depuis le 1<sup>er</sup> janvier 2023 ; **stratégie numérique responsable depuis 2025** | Stratégie formalisée, publiée et pilotée, pas une intention |
| **RGESN** (ARCEP / ARCOM), article 25 de la loi REEN | Services numériques de l'État et des collectivités de plus de 50 000 habitants | Applicable **depuis 2024** | **Déclaration d'écoconception à publier** sur le service. Grille d'audit exploitable telle quelle. Cf. [C1](C1-eco-conception-services.md) |
| **European Accessibility Act**, directive (UE) 2019/882 transposée par le décret 2023-931 | **Secteur privé** : entreprises de plus de 10 salariés et plus de 2 M€ de CA fournissant un service B2C couvert (e-commerce, banque, transport, télécoms, médias, livres numériques) | **Depuis le 28 juin 2025** | L'accessibilité passe d'exigence de qualité à obligation légale sanctionnée. Audit RGAA / WCAG des parcours concernés |
| **RGAA** | Secteur public et organismes délégataires | En vigueur | Déclaration d'accessibilité, plan pluriannuel, audit |
| **RGPD** | Toute organisation traitant des données personnelles | En vigueur | Durées de conservation et droit à l'effacement, le levier juridique des campagnes de purge de [C2](C2-cycle-vie-donnees.md) |

!!! warning "Vérifier avant de s'engager"
    Les règlements et directives omnibus de 2025-2026 ont modifié les périmètres et
    les échéances de la CSRD et de l'AI Act, et plusieurs transpositions sont en
    cours. Faites confirmer l'applicabilité par votre direction juridique avant
    d'inscrire une échéance dans une feuille de route.

Ces sept textes réclament au fond les mêmes livrables : un **inventaire** (des
équipements, des données, des systèmes d'IA), une **traçabilité** des mesures et des
**preuves archivées**. Construisez-les une fois et servez-les à plusieurs
réglementations, plutôt que d'ouvrir un chantier par texte.

## Étapes de mise en œuvre

1. Mettre à jour les **cadres de référence** (templates, catalogues de services, modèles d'architecture).
2. **Accompagner** les équipes (expertise, solutions conformes et performantes).
3. **Valider la conformité** via revues d'architecture / de code NR systématiques pour les nouveaux projets.
4. Archiver les **preuves de conformité** à chaque jalon.
5. **Tenir la cartographie des obligations** : textes applicables, périmètre du SI
   concerné, échéance, responsable. La revoir chaque année, les périmètres bougent.
6. **Mutualiser les livrables de conformité** (inventaires, traçabilité, preuves)
   entre les textes plutôt que d'ouvrir un chantier par réglementation.

## KPIs & OKR

- **KPI** : % d'actions de la feuille de route démarrées ; taux de consommation du budget ; jalons atteints dans les délais ; preuves de conformité archivées par jalon ; **couverture de la cartographie réglementaire** (textes applicables identifiés et dotés d'un responsable) ; part des services concernés disposant d'une déclaration à jour (écoconception, accessibilité).
- ***OKR*** : 100 % des nouveaux projets passés en revue NR ; preuves archivées pour chaque jalon majeur.

## Pièges à éviter

- Définir des standards sans outiller le contrôle (la conformité se vérifie, elle ne se décrète pas).
- Faire du contrôle un point de friction plutôt qu'un accompagnement.
- Renvoyer la conformité réglementaire au juridique. L'AI Act et la CSRD réclament
  des inventaires et de la traçabilité, deux livrables d'architecture.
- Découvrir une échéance six mois avant, faute de cartographie tenue.
- Confondre déclaration publiée et conformité réelle : la déclaration engage.

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Outil / Ressource | Usage | Lien |
|---|---|---|
| 🟢 GR491 (INR) | Référentiel d'éco-conception | <https://gr491.isit-europe.org/> |
| RGESN | Contrôle de conformité | <https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/> |
| Charte IA Responsable (INR) | Cadre d'engagement IA éthique et éco-responsable, en appui de l'AI Act | <https://charter.isit-europe.org/charte-ia/?lang=fr_FR> |
| 🟢 Skill NR (INR) | Contrôle d'éco-conception outillé côté assistants IA de code | [Présentation](https://institut-du-numerique-responsable.github.io/skill-nr/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/skill-nr) |
| 🟢 Green Claude (INR) | Audit RGESN/GR491 automatisé dans l'IDE : le contrôle de conformité au plus près du code | [Présentation](https://institut-du-numerique-responsable.github.io/green-claude/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/green-claude) |

## Fiches liées

- [G4 — Construire la feuille de route](G4-feuille-de-route.md)
- [C1 — Éco-concevoir les services numériques](C1-eco-conception-services.md)
- [D2 — Communiquer, valoriser & labelliser](D2-communiquer-valoriser.md)
