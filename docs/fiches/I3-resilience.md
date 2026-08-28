---
id: I3
titre: Arbitrer résilience et sobriété
description: >-
  Définir un niveau de résilience adapté à chaque service, tester les dispositifs de reprise et maîtriser les ressources consacrées à la redondance.
theme: Infrastructure et matériel
statut: brouillon
proprietaire: INR/ISIT
contributeurs: []
reviewers: []
version: 0.2
maj: 2026-08-28
fiches_liees: [I1, C4, M2, V2]
---

# I3 — Arbitrer résilience et sobriété

> **Public cible.** Architectes, équipes d'exploitation, ingénieurs de fiabilité (SRE), RSSI, responsables des plans de continuité et de reprise, direction technique.

## Objectif

Définir un niveau de résilience adapté à la criticité de chaque service. Réduire les
points de défaillance techniques, humains et fournisseurs, puis vérifier que les
dispositifs de continuité et de reprise fonctionnent avec les moyens prévus.

## Contexte et enjeux

La résilience permet à un service de continuer à fonctionner, éventuellement en
mode dégradé, puis de revenir à une situation normale après un incident. Le niveau
attendu dépend des conséquences d'une interruption : sécurité des personnes,
obligations réglementaires, pertes financières, atteinte aux données ou gêne pour
les utilisateurs.

La redondance réduit certains risques, mais elle mobilise du calcul, du stockage,
du réseau et des équipements supplémentaires. Elle augmente aussi le nombre de
composants à exploiter et à tester. L'organisation doit donc comparer le risque
couvert aux coûts économiques et environnementaux de chaque scénario.

La résilience ne repose pas uniquement sur l'infrastructure. Une dépendance non
maintenue, une procédure inconnue de l'équipe, une sauvegarde impossible à restaurer
ou un fournisseur irremplaçable peuvent interrompre un service pourtant redondé.
L'analyse doit couvrir ces fragilités et les hypothèses d'approvisionnement en
matériel ou en capacité cloud.

Voir le [guide](../guide-unifie.md#29-le-retour-de-la-contrainte-physique).

## Étapes de mise en œuvre

1. **Classer les services selon leur criticité.** Évaluer les conséquences d'une
   interruption avec les métiers, la sécurité et la conformité. Recenser les
   dépendances nécessaires au fonctionnement de chaque service, y compris les
   fournisseurs et les échanges décrits dans [C4](C4-dette-integration.md).

2. **Définir les objectifs de continuité et de reprise.** Pour chaque service,
   préciser la disponibilité attendue sur une période définie et avec une méthode de
   mesure convenue, le mode dégradé acceptable, le délai cible de rétablissement du
   service (**RTO**) et l'ancienneté maximale admissible des données restaurées,
   exprimée en durée (**RPO**). Faire valider ces objectifs par le responsable métier
   et les réexaminer après tout changement important.

3. **Comparer plusieurs scénarios d'architecture.** Étudier des scénarios adaptés au
   service, dont une option sans redondance permanente lorsqu'elle reste compatible
   avec le risque. Pour chacun, documenter les risques couverts, les risques résiduels,
   le délai de reprise, les compétences requises et les ressources mobilisées.
   Expliquer pourquoi les options écartées ne conviennent pas. Évaluer les coûts et
   l'empreinte avec [I1](I1-infrastructures.md) avant de choisir.

4. **Traiter les points de défaillance non matériels.** Repérer les composants qui
   ne sont plus maintenus ou ne disposent pas de solution de remplacement. Identifier
   les procédures connues d'une seule personne, les fournisseurs difficiles à
   remplacer et les hypothèses d'approvisionnement fragiles. Prévoir une action,
   un responsable et une échéance pour chaque risque significatif.

5. **Préparer et tester les modes de fonctionnement.** Documenter les procédures de
   bascule, de fonctionnement dégradé, de restauration et de retour à la normale.
   Tester les sauvegardes sur un environnement isolé et organiser des exercices
   adaptés au risque. L'ingénierie du chaos peut compléter ces exercices lorsque
   l'équipe maîtrise l'outil et les conséquences des perturbations injectées. Pour
   chaque exercice, définir à l'avance le scénario, le périmètre, les critères de
   succès, les rôles, les critères d'arrêt et les preuves à conserver. Vérifier le
   service rendu, l'intégrité et la cohérence des données, le RTO, le RPO et le retour
   à la normale.

6. **Mesurer les résultats et corriger les écarts.** Comparer le délai de
   rétablissement observé au RTO et le point de reprise effectivement restauré au
   RPO. Analyser les échecs, suivre les actions correctives et répéter le test. Une
   disponibilité supérieure à l'objectif ne suffit pas à réduire la redondance :
   toute modification exige une nouvelle analyse de risque et un test du scénario
   retenu.

7. **Réexaminer périodiquement les choix.** Revoir la criticité, les objectifs et
   l'architecture après un incident, un changement de fournisseur ou une évolution
   importante du service. Supprimer les composants et les capacités devenus inutiles
   lorsque les tests confirment que le niveau de résilience reste conforme au besoin.

## Indicateurs et objectifs

- **KPI** : part des services critiques dotés d'objectifs validés ; part des
  sauvegardes critiques restaurées avec succès ; part des exercices qui respectent
  le RTO et le RPO ; nombre de points de défaillance sans plan de traitement ; taux
  de réalisation des actions correctives dans le délai prévu ; capacité de calcul,
  stockage, trafic réseau, équipements, coût et, lorsque cela peut être mesuré,
  empreinte environnementale consacrés à la redondance, par service et par rapport à
  une architecture de référence.
- ***OKR 1*** : documenter et faire valider les objectifs de continuité et de reprise
  de 100 % des services critiques avant la date convenue avec le commanditaire.
- ***OKR 2*** : tester chaque année, selon un scénario documenté, la reprise de 100 %
  des services critiques et suivre jusqu'à leur clôture les actions correctives issues
  des exercices.

## Pièges à éviter

- Appliquer le même niveau de résilience à tous les services sans analyser leur
  criticité.
- Confondre le nombre de copies avec la capacité à reprendre le service.
- Définir un RTO ou un RPO sans vérifier que l'architecture peut le respecter.
- Tester la bascule sans tester la restauration des données et le retour à la normale.
- Ignorer les dépendances humaines, logicielles et fournisseurs.
- Organiser un exercice susceptible d'affecter la production sans périmètre, critères
  d'arrêt ni procédure de retour arrière.
- Réduire une capacité sur la seule base de la disponibilité passée.

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
| Cadre | **NIS2** | Exigences européennes de cybersécurité et de continuité pour les entités concernées | <https://eur-lex.europa.eu/eli/dir/2022/2555/oj?locale=fr> |
| Cadre | **DORA** | Résilience opérationnelle numérique du secteur financier | <https://eur-lex.europa.eu/eli/reg/2022/2554/oj?locale=fr> |
| Référentiel | 🟢 **GR491** (INR) | Critères de durabilité et de robustesse | <https://gr491.isit-europe.org/> |

## Fiches liées

- [I1 — Optimiser infrastructures et environnements](I1-infrastructures.md)
- [C4 — Résorber la dette d'intégration](C4-dette-integration.md)
- [V2 — Souveraineté et réversibilité](V2-souverainete.md)
- [M2 — Pilotage et tableau de bord KPI](M2-pilotage-kpi.md)
