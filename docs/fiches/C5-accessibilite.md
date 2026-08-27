---
id: C5
titre: Accessibilité, levier de sobriété
description: >-
  Traiter l'accessibilité comme un chantier d'architecture et non comme une correction de fin de projet : les mêmes exigences allègent les interfaces, prolongent la vie des terminaux et servent la sobriété du SI.
theme: Conception sobre
statut: brouillon
proprietaire: INR/ISIT
contributeurs: []
reviewers: []
version: 0.1
maj: 2026-08-28
fiches_liees: [C1, D1, M1, I2]
---

# C5 — Accessibilité, levier de sobriété

> **Public cible.** Dév front, UX, Product Owners, architectes, QA, référents accessibilité.

## Objectif

Rendre les services utilisables par tous, et se servir de cette exigence pour
alléger les interfaces. Traiter l'accessibilité au moment de la conception, là où
elle coûte peu et rapporte deux fois.

## Contexte & enjeu

**Un axe du NR resté sans chantier.** L'accessibilité forme le deuxième des cinq
axes du Numérique Responsable, elle traverse la matrice KPI du guide, et pourtant
les organisations la traitent en fin de projet, par un audit isolé qui produit une
liste de corrections que personne ne budgète. Elle a longtemps servi de variable
d'ajustement : la première exigence sacrifiée quand le planning se tend, parce
qu'elle passait pour une contrainte externe sans bénéfice interne.

**Ce raisonnement se retourne.** Les exigences d'accessibilité et les exigences de
sobriété demandent la même discipline, et le plus souvent le même travail.

Un contenu structuré en HTML sémantique se lit par un lecteur d'écran, et il pèse
moins qu'une reconstruction du même contenu en composants JavaScript. Une
navigation au clavier fonctionne sans les bibliothèques d'interaction qui alourdissent
les pages. Un contraste suffisant évite les images de texte. Une alternative
textuelle sert la personne qui n'accède pas à l'image, et sert aussi la connexion qui
ne la charge pas. L'amélioration progressive, principe fondateur de l'accessibilité,
produit des services qui fonctionnent sur réseau faible.

**Le gain le plus lourd concerne le matériel.** Le guide établit que 80 % de
l'empreinte d'un équipement est figée dès sa fabrication, ce qui fait de
l'allongement de la durée de vie le premier levier de sobriété. Un service accessible
fonctionne sur un terminal ancien, un navigateur qui n'est pas de la dernière
version, une connexion lente. Il retire donc un motif de renouvellement du parc.
À l'inverse, chaque interface qui exige un appareil récent pousse au remplacement
d'équipements encore fonctionnels, et déplace l'empreinte chez l'utilisateur, hors
de votre bilan mais pas hors du monde.

**La convergence a des limites, autant les nommer.** Les sous-titres et les
transcriptions ajoutent du contenu, même s'ils permettent souvent de se passer de la
vidéo. Les attributs ARIA ajoutent du balisage. Ces surcoûts restent marginaux face
au poids des interfaces qu'ils remplacent, et ils ne justifient aucun arbitrage
contre l'accessibilité.

**L'obligation s'est étendue au privé.** Le European Accessibility Act s'applique
depuis le 28 juin 2025 aux entreprises de plus de 10 salariés et 2 M€ de chiffre
d'affaires fournissant un service B2C couvert. Le RGAA reste opposable au secteur
public. Les échéances figurent en [D1](D1-conformite.md).

Cf. [guide](../guide-unifie.md#26-pilier-5-architecture-logicielle-sobre-eco-conception).

## Étapes de mise en œuvre

1. **Fixer le niveau visé et le périmètre.** RGAA niveau AA sur les parcours
   critiques, plutôt qu'une ambition globale que personne ne tient. Écrire quels
   services sont concernés et à quelle échéance, en cohérence avec les obligations
   de [D1](D1-conformite.md).

2. **Partir du contenu et de la structure.** Titres hiérarchisés, listes, tableaux
   avec en-têtes, formulaires étiquetés, langue déclarée. Ce socle sémantique porte
   l'accessibilité et allège la page. Il se pose au début, il se rattrape mal.

3. **Concevoir sans dépendre du script.** Le service rend son contenu principal sans
   JavaScript, puis l'améliore quand le script s'exécute. Vous gagnez les lecteurs
   d'écran, les connexions faibles, les terminaux anciens et un poids de page réduit,
   par le même travail.

4. **Écrire les critères dans la Definition of Done.** Contraste, navigation au
   clavier, alternatives textuelles, focus visible. Une exigence qui n'entre pas dans
   la définition du fini se traite en fin de projet, donc mal et cher.

5. **Automatiser ce qui s'automatise.** Les outils (axe-core, Pa11y, Lighthouse)
   couvrent environ un tiers des critères, et ce tiers se vérifie à chaque commit
   dans la chaîne d'intégration continue, aux côtés des contrôles d'éco-conception
   de [C1](C1-eco-conception-services.md).

6. **Tester avec des personnes, pas seulement avec des outils.** Les deux tiers
   restants demandent un examen humain, et le meilleur retour vient des personnes
   concernées. Une session avec un utilisateur de lecteur d'écran apprend plus qu'un
   rapport de cent lignes.

7. **Mesurer les deux gains ensemble.** Suivre le taux de conformité RGAA et le poids
   des pages sur les mêmes parcours. Présenter les deux courbes côte à côte transforme
   l'accessibilité en argument de sobriété, et l'inverse.

8. **Publier la déclaration d'accessibilité.** Elle est obligatoire pour les entités
   concernées, elle rend le niveau réel visible, et elle engage. Un plan pluriannuel
   la complète. Le **Skill Accessibilité** de l'INR la génère au modèle officiel à
   partir des résultats d'audit, ce qui retire le prétexte le plus courant à son
   absence.

9. **Étendre aux documents et aux achats.** Les PDF et les bureautiques diffusés
   comptent, et un logiciel acquis non accessible devient votre problème. Porter
   l'exigence dans les marchés avec [I2](I2-achats-responsables.md).

## KPIs & OKR

- **KPI** : taux de conformité RGAA niveau AA sur les parcours critiques ; nombre de
  critères vérifiés automatiquement dans la chaîne d'intégration ; poids moyen des
  pages sur les mêmes parcours ; part des services disposant d'une déclaration à
  jour ; part des marchés intégrant une exigence d'accessibilité ; âge du terminal le
  plus ancien sur lequel le service reste utilisable.
- ***OKR*** : 75 % de conformité RGAA AA sur les trois parcours principaux ;
  contrôles automatisés en place dans la chaîne d'intégration ; une session de test
  avec des utilisateurs concernés par trimestre.

## Pièges à éviter

- Auditer en fin de projet et découvrir des corrections structurelles quand le budget
  est consommé.
- Croire les outils exhaustifs. Ils couvrent environ un tiers des critères, et la
  navigation réelle échappe à l'analyse statique.
- Poser une surcouche d'accessibilité sur un service inaccessible. Elle ajoute du
  poids, masque le problème et laisse l'obligation entière.
- Traiter l'accessibilité comme une contrainte externe sans bénéfice. Les mêmes
  exigences allègent les pages et prolongent la vie des terminaux.
- Exiger un navigateur récent pour un service de consultation, et pousser au
  renouvellement d'équipements qui fonctionnent.
- Publier une déclaration de complaisance. Elle engage, et l'écart avec la réalité
  se constate.

## Outils & ressources

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

> Cette sélection ne retient que les outils mobilisables sur ce chantier. Le catalogue complet de l'INR (355 ressources classées en 15 thèmes, liens vérifiés) tient la référence à jour : [**Boîte à outils du Numérique Responsable**](https://sustainableit-tools.isit-europe.org/).

| Catégorie | Outil / Ressource | Usage | Lien |
|---|---|---|---|
| Référentiel | **RGAA 4.1.2** (DINUM) | Référentiel français, aligné sur la norme EN 301 549 et les WCAG 2.1 niveau AA. Le RGAA 5, attendu fin 2026, intègrera les WCAG 2.2, les applications mobiles et les documents bureautiques | <https://accessibilite.numerique.gouv.fr/> |
| Référentiel | **WCAG** (W3C) | Recommandations internationales, version 2.2 publiée | <https://www.w3.org/WAI/standards-guidelines/wcag/> |
| Audit | 🟢 **Ara** (DINUM) | Outil officiel de conduite d'audit RGAA et de génération de déclaration | <https://ara.numerique.gouv.fr/> |
| Audit | 🟢 **Asqatasun** | Audit automatisé RGAA et WCAG | <https://www.asqatasun.org/> |
| Intégration continue | 🟢 **axe-core** (Deque) | Moteur de règles intégrable aux tests | <https://github.com/dequelabs/axe-core> |
| Intégration continue | 🟢 **Pa11y** | Contrôle en ligne de commande, adapté aux pipelines | <https://pa11y.org/> |
| Déclaration | 🟢 **Skill Accessibilité** (INR) | Génère une déclaration d'accessibilité RGAA conforme au modèle officiel | [Présentation](https://institut-du-numerique-responsable.github.io/claude_skill_accessibilite/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/claude_skill_accessibilite) |
| Qualité web | **Opquast** | Bonnes pratiques croisant accessibilité, sobriété et qualité | <https://www.opquast.com/> |
| Documentation | 🟢 **MDN Accessibilité** | Référence technique pour les équipes | <https://developer.mozilla.org/fr/docs/Web/Accessibility> |
| Référentiel | 🟢 **GR491** (INR) | Critères croisant accessibilité et éco-conception | <https://gr491.isit-europe.org/> |
| Code | 🟢 **Skill NR** (INR) | Règles RGAA et RGESN pour les assistants IA de code | [Présentation](https://institut-du-numerique-responsable.github.io/skill-nr/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/skill-nr) |

## Fiches liées

- [C1 — Éco-concevoir les services numériques](C1-eco-conception-services.md)
- [D1 — Mettre en œuvre & contrôler la conformité](D1-conformite.md)
- [M1 — Faire l'état des lieux](M1-diagnostic.md)
- [I2 — Politique d'achats numériques responsables](I2-achats-responsables.md)
