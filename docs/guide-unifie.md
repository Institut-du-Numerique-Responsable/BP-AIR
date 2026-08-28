---
description: >-
  Les fondations de l'architecture informatique responsable : 6 piliers, matrice architecte, équation de Kaya appliquée au SI, alignement ODD, boîte à outils et glossaire.
---

# Guide — les fondations

*Partie théorique du document de synthèse du GT AIR. La partie pratique est éclatée en [fiches](index.md#les-fiches-par-theme).*

---

## 1. Introduction et posture

Le numérique et la transition écologique puisent dans les mêmes stocks : énergie,
eau, métaux, et le temps humain qui va avec. Chaque fois que vous étendez le SI,
vous prélevez sur ces réserves. La plupart de ces arbitrages se prennent en revue
d'architecture, sans que personne ne les nomme ainsi.

### Les chiffres et leur périmètre

L'ADEME et l'Arcep ont réévalué l'empreinte du numérique en France en novembre 2024.
Elle atteint **4,4 % de l'empreinte carbone nationale** (29,5 MtCO₂e pour 2022),
contre 2,5 % estimé en 2020, et **11 % de la consommation électrique** du pays
(51,5 TWh, jusqu'à 65 TWh en comptant les datacenters installés à l'étranger qui
servent des usages français). Sans inflexion, l'ADEME projette un **triplement de
l'empreinte carbone entre 2020 et 2050**
([ADEME / Arcep](https://www.arcep.fr/la-regulation/grands-dossiers-thematiques-transverses/lempreinte-environnementale-du-numerique.html)).

Avant de comparer les chiffres, vérifiez leur méthode de calcul et leur périmètre.
L'écart entre 2,5 % et 4,4 % en quatre ans tient à la méthode : les évaluateurs ont
élargi le périmètre et affiné le comptage des équipements utilisateurs. L'impact
n'a pas doublé, mais sa mesure s'est améliorée.

À l'échelle mondiale, les estimations divergent selon le périmètre retenu, les
sources de données et le traitement des terminaux. L'AIE et les travaux
académiques situent le numérique à **quelques pour cent des émissions mondiales**,
avec une croissance plus rapide que la moyenne des secteurs. Indiquez toujours la
source, l'année et le périmètre d'un chiffre afin de permettre sa vérification.

### Là où se concentre l'empreinte

**80 % de l'empreinte d'un équipement est figée dès sa fabrication**, avant la
première mise sous tension. Le **Scope 3**, la chaîne de valeur, porte jusqu'à
**80 % de l'empreinte globale** d'une organisation.

Vous en tirez deux conséquences. Allonger la durée de vie du parc pèse plus lourd
que toute optimisation de code, ce qui déplace le sujet du développeur vers l'acheteur
([I2](fiches/I2-achats-responsables.md)). Et l'essentiel de votre empreinte se
décide chez vos fournisseurs, donc votre chaîne de valeur devient un terrain
d'architecture ([V1](fiches/V1-maturite-parties-prenantes.md)).

### Le périmètre a changé d'échelle

Les premières démarches de numérique responsable se concentraient souvent sur la
qualité du code et le choix des outils. Vous optimisez une application, et le gain se dilue
dans les flux qui l'entourent, dans les copies de données qu'elle alimente, dans les
serveurs qu'elle maintient allumés. **Le NR se joue à l'échelle du Système
d'Information dans son ensemble.**

Trois évolutions ont suivi les premiers travaux du GT.

**La réglementation fixe des dates.** AI Act, CSRD, loi REEN, RGESN, European
Accessibility Act : les obligations sont datées et opposables. Une direction arbitre
et budgète un chantier daté là où elle reporte une bonne intention
([D1](fiches/D1-conformite.md)).

**La contrainte matérielle est revenue.** Tension sur les composants, prix de
l'électricité, datacenters qui refusent des raccordements faute d'alimentation. La
sobriété rejoint la latence et la disponibilité dans la liste des contraintes
d'ingénierie ([§2.9](#29-le-retour-de-la-contrainte-physique)).

**L'IA déplace les coûts.** Le calcul accéléré concentre la rareté, et l'inférence
en production pèse plus lourd que l'entraînement sur la durée de vie d'un service
([C3](fiches/C3-ia-sobre.md)).

### Le constat

Les organisations multiplient les initiatives ponctuelles : un Digital Cleanup Day
par an, un bilan carbone tous les trois ans, un audit d'accessibilité isolé. Chacune
a sa valeur. Mises bout à bout, elles ne dessinent aucune trajectoire, et au bout de
trois ans personne ne sait dire si l'empreinte a baissé. Ce guide vise le passage de
l'action ponctuelle à **une stratégie intégrée, pilotée et pérenne**.

### La posture

Le Numérique Responsable produit de la performance économique, opérationnelle,
sociale et environnementale. Quand vous rationalisez un SI, la facture baisse avant
l'empreinte, et les deux suivent la même pente. Cet alignement rend la démarche
défendable devant un comité qui ne juge que sur le coût.

L'architecte SI porte cet arbitrage. Il traduit les enjeux de l'entreprise en choix
techniques, et rend visibles les contraintes physiques que ces choix engagent, au
moment où l'organisation peut encore décider autrement.

> **Fil rouge.** Les **fondations** (pourquoi et où agir), les **fiches**
> (comment agir, chantier par chantier), puis une **matrice de synthèse** et une
> **boîte à outils** pour outiller la démarche.

---

## 2. Partie théorique : les fondations

!!! note "Sur les chiffres cités"
    Chaque ordre de grandeur porte sa source et son année. Certains proviennent
    d'études d'éditeurs ou de travaux anciens, signalés comme tels : reprenez-les
    comme repères de discussion, pas comme mesures de votre système. Les chiffres qui
    engagent une décision doivent venir de votre propre diagnostic
    ([M1](fiches/M1-diagnostic.md)).


### 2.1 Un contexte instable et des ressources sous tension

Les organisations évoluent dans un monde dit **VUCA** — *Volatile, Uncertain, Complex, Ambiguous* (Bennis et Nanus, 1987). Crises économiques, sanitaires, énergétiques, raréfaction des matières premières : les règles du jeu ont changé.

Les directions des systèmes d'information doivent désormais justifier leurs investissements et mieux maîtriser leurs ressources. La sobriété répond à cette contrainte. L'**urbanisation du SI** aide à rationaliser l'existant et à faire mieux avec moins.

<figure markdown>
  ![VUCA : un monde volatile, incertain, complexe et ambigu](assets/img/vuca.svg)
  <figcaption>VUCA : un monde devenu volatile, incertain, complexe et ambigu.</figcaption>
</figure>

### 2.2 Pilier 1 — Gouvernance et alignement stratégique

Toutes les organisations partagent un besoin structurel : **bien gérer des ressources finies (financières, matérielles, humaines) au service de leurs objectifs.** C'est l'**alignement stratégique**. La stratégie de l'entreprise se retrouve dans chacune des briques numériques :

- un numérique **source d'impacts** environnementaux et sociétaux ;
- un numérique **levier** de réduction des émissions et de sobriété ;
- un numérique **catalyseur** de nouveaux modèles d'affaires.

**Un principe fondateur : on ne gouverne bien qu'à plusieurs.** Le NR exige une attente « ascendante » (terrain) et un soutien « descendant » (direction). Sans mandat clair, les exigences non-fonctionnelles (performance énergétique, accessibilité, durabilité) sont perçues comme des *nice-to-have* et sacrifiées.

<figure markdown>
  ![L'alignement stratégique : de la stratégie métier aux ressources logiques et physiques](assets/img/alignement-strategique.webp)
  <figcaption>L'alignement stratégique : la stratégie métier irrigue les ressources logiques puis physiques du SI.</figcaption>
</figure>

> **Maturité ≠ performance.** Une organisation est *performante* si ses équipements portent un écolabel (ex. TCO). Elle est *mature* si elle a **explicitement exigé** cet écolabel à l'appel d'offres. On peut être performant par chance ; on n'est mature que par intention et par méthode.

### 2.3 Pilier 2 — Urbanisation et architecture en couches

L'urbanisation organise et **rationalise** le SI. Si deux outils font la même chose, n'en garder qu'un : simplification, économies de licences, de maintenance, de machines, d'énergie. Une cartographie à jour permet de **réduire de 20 à 30 % les coûts d'exploitation**
(Forrester, 2021).

| Couche | Question | Ce qu'on y trouve |
|---|---|---|
| **Stratégie et métier** | Le « Quoi » | Vision, gouvernance, réglementation, parties prenantes |
| **Métier** | Les savoir-faire | Processus → opérations → tâches |
| **Fonctionnelle** | L'organisation des fonctions | Zones, quartiers, îlots, blocs |
| **Applicative** | L'incarnation logicielle | Blocs applicatifs, sous-systèmes, données |
| **Technique** | Les services techniques communs | Middleware, services d'infrastructure |
| **Matérielle** | L'hébergement physique | Serveurs, postes, terminaux, réseau |

> **Rendre explicite ce que le modèle oublie.** Chaque couche génère des impacts sur deux dimensions invisibles : les **ressources environnementales** (énergie, eau, matières) et les **impacts sociaux/sociétaux**. Le GT AIR recommande d'ajouter une « couche ressources » au modèle.

<figure markdown>
  ![Triptyque des ressources à disposition de l'organisation](assets/img/ressourcesi.svg)
  <figcaption>Triptyque des ressources à disposition de l'organisation : financières, humaines et matérielles.</figcaption>
</figure>

### 2.4 Pilier 3 — Cycle de vie (architecture, services, données)

Comprendre les cycles de vie, c'est savoir **où se cachent les impacts** et donc **quoi mesurer**.

**Cycle de vie d'un service numérique.** Tout service naît d'une **demande**, qui doit répondre à un **besoin** (pas une envie), créer de la **valeur mesurable**, servir la stratégie, et **ne pas déjà exister**. À l'usage : appliquer la **règle des 3U** — un service est-il **U**tile ? **U**tilisé ? **U**tilisable ?

<figure markdown>
  ![Le cycle de vie du SI piloté par la gouvernance](assets/img/cycle-de-vie.webp)
  <figcaption>Le cycle de vie du SI piloté par la gouvernance : Design (vision, processus, architecture), Build (achats, construction), Run (usage), jusqu'à la fin de vie.</figcaption>
</figure>

**Le cycle de vie des données reste encore peu pris en compte.**

- **52 % des données** d'un SI sont des **dark data**, stockées sans création de
  valeur, et **33 %** sont des données **ROT**, pour **R**edondantes, **O**bsolètes
  ou **T**riviales (Veritas, *Databerg Report*, 2015 ; étude d'éditeur, à considérer
  comme un ordre de grandeur et non comme une mesure de votre SI).

La parade : une **gouvernance de la donnée** (catalogue, registre, qualification chaud/froid). Attention : une donnée sans valeur *aujourd'hui* peut en créer demain — décommissionner avec discernement.

### 2.5 Pilier 4 — Cycle de vie du matériel et économie circulaire

**80 % de l'empreinte carbone d'un équipement provient de sa fabrication**
(ordre de grandeur retenu par l'ADEME pour les terminaux utilisateurs ; la part varie
selon le type d'équipement et l'intensité carbone du réseau électrique d'usage). Le seul levier vraiment puissant : **l'allongement de la durée de vie** et la **circularité**. Trois axes :

1. **Réduction à la source** — réutiliser, réparer, reconditionner, prolonger *avant* d'acheter.
2. **Critères environnementaux (Green IT)** — durables, réparables (Indice de Réparabilité, TCO / EPEAT).
3. **Responsabilité sociale** — droits humains dans la chaîne, inclusion (ESAT).

En aval, gestion des **DEEE** et **économie circulaire locale** au-delà de la simple conformité.

<figure markdown>
  ![Les couches du SI croisées avec le cycle de vie et la couche ressources](assets/img/couches-cycle-vie-ressources.webp)
  <figcaption>Les couches (Entreprise → Hardware) croisées avec le cycle de vie (fabrication, utilisation, fin de vie) et la « couche ressources » (eau, énergie, matériaux, CO₂).</figcaption>
</figure>

### 2.6 Pilier 5 — Architecture logicielle sobre (éco-conception)

L'éco-conception est la plus efficace quand **intégrée dès la conception**. Quatre familles de leviers :

- **Sobriété fonctionnelle** : règle des 3U et standards ouverts (REST, JSON, ODF,
  CSV). Le chiffre souvent cité de 45 % de fonctionnalités jamais utilisées vient du
  Standish Group (*CHAOS Report*, 2002), dont la méthode est discutée et l'âge
  considérable. Mesurez l'usage réel de vos propres fonctionnalités plutôt que de
  reprendre ce pourcentage.
- **Sobriété technique** — poids des pages (EcoIndex), nombre de requêtes (YellowLab), poids des médias, audits statiques (EcoCode).
- **Durabilité** — rétrocompatibilité, ajustement automatique des ressources, hébergeurs engagés.
- **Hygiène des environnements** : 25 à 30 % des serveurs tournent sans usage, un
  ordre de grandeur stable depuis les travaux de l'Uptime Institute et d'Anthesis sur
  les serveurs comateux. Un serveur sous 15 % de charge consomme jusqu'à 60 % de son
  énergie nominale, la consommation d'un processeur au repos restant élevée.
  Consolidation : de 30 à 60 % de gain.

### 2.7 Pilier 6 — Mesure et pilotage (l'équation de Kaya appliquée au SI)

> *« On ne pilote que ce que l'on mesure. »*

L'**équation de Kaya** (1993) transposée au SI relie population des utilisateurs, volume de services, valeur produite, consommation d'énergie, intensité carbone. Axes de pilotage : **intensité carbone, efficience énergétique, efficacité du SI, sobriété**.

<figure markdown>
  ![L'équation de Kaya appliquée au SI](assets/img/kaya.webp)
  <figcaption>L'équation de Kaya appliquée au SI : quatre leviers d'action — intensité carbone, efficience énergétique, efficacité et sobriété du SI.</figcaption>
</figure>

Un bon **KPI NR** croise quatre dimensions : les **5 axes du NR**, le **cycle de vie**, le **découpage en couches**, le triptyque **People / Planet / Profit**.

<figure markdown>
  ![Les axes du NR](assets/img/nr.svg)
  <figcaption>Les axes du NR.</figcaption>
</figure>

| Couche | Optimiser les impacts | Inclusion et durabilité | Éthique et responsabilité | Résilience |
|---|---|---|---|---|
| **Fonctionnelle** | Taux d'usage des fonctionnalités | Taux d'utilisateurs capables | Données perso à but lucratif | Unicité des fonctions |
| **Applicative / Data** | Données utilisées ; qualité | Applications accessibles (WCAG) | Respect RGPD | Unicité de la donnée |
| **Technique** | Applications open source | API/frameworks accessibles | Sécurisation des données | Technos orphelines |
| **Matérielle** | Usage réel (CPU, RAM, I/O) | Terminaux accessibles | Écolabels ; % renouvelable | Serveurs à fonction identifiée |
| **Business** | Services / population | % mécénat de compétences | % femmes IT et turnover | Turnover équipes projet |

> **Les 5 axes du Numérique Responsable**
> 1. Un outil aux impacts et consommations limités.
> 2. Des offres de services accessibles, inclusives, durables.
> 3. Des pratiques éthiques et responsables.
> 4. Un numérique mesurable, transparent, lisible.
> 5. L'émergence de nouveaux comportements et valeurs.

<figure markdown>
  ![Les 5 axes du NR croisés avec les couches d'architecture et les dimensions spatiale et temporelle](assets/img/sphere-5-axes.webp)
  <figcaption>Vue d'ensemble : les 5 axes du NR enveloppent les couches d'architecture (Business → Infrastructure), selon les dimensions spatiale et temporelle.</figcaption>
</figure>

### 2.8 Le SI au service des ODD

<figure markdown>
  ![Les 17 Objectifs de Développement Durable de l'ONU](assets/img/odd-17.webp)
  <figcaption>Les 17 Objectifs de Développement Durable de l'ONU. Le SI peut en adresser directement une partie (voir tableau).</figcaption>
</figure>

| ODD | Contribution du SI |
|---|---|
| **3** Santé et bien-être | Lutte contre dark patterns, temps d'écran ; substances dangereuses |
| **4** Éducation | Apprentissage continu, montée en compétences |
| **5** Égalité F/H | Lutte contre discriminations, accès aux directions |
| **6** Eau | Consommation des datacenters et de la fabrication |
| **7** Énergie durable | Efficience, renouvelables |
| **8** Travail décent | Conditions dans les centres de services sous-traités |
| **9** Infrastructure et innovation | Architecture résiliente et sobre |
| **10** Réduction des inégalités | Équité salariale |
| **12** Consommation responsable | Mesure des 3U, quotas |
| **13** Climat | Empreinte carbone par service |
| **17** Partenariats | Coopération public / privé / société civile |

### 2.9 Le retour de la contrainte physique

Pendant vingt ans, l'architecte a pu raisonner en abstractions. La capacité suivait,
l'énergie n'apparaissait pas sur sa facture, le matériel arrivait en quelques
semaines. Trois évolutions ont refermé cette parenthèse : la tension sur les
composants, le prix de l'électricité, et les limites d'alimentation des datacenters,
qui refusent aujourd'hui des raccordements dans plusieurs régions européennes.

La sobriété change alors de statut. Elle cesse d'être une exigence morale qu'on
arbitre en dernier, pour devenir une contrainte d'ingénierie du même ordre que la
latence, la disponibilité ou la sécurité. Un architecte ne discute pas l'existence
d'une contrainte de latence : il conçoit avec.

Trois conséquences pratiques.

**Le logiciel se paie en matériel.** Une réplication nocturne maintient allumés un
serveur, une baie de stockage et un lien réseau. Un cluster de haute disponibilité,
ce sont trois machines pour un service. Un découpage en microservices multiplie les
planchers de ressources réservées. Ces choix se prennent sur un tableau blanc et se
règlent en équipements ([C4](fiches/C4-dette-integration.md)).

**L'empreinte est engagée avant la mise en service.** 80 % de l'empreinte d'un
équipement est figée dès sa fabrication. Un serveur ajouté arrive avec sa dette
environnementale constituée, avant d'avoir traité la première requête. Reporter un
achat vaut mieux qu'optimiser la consommation de la machine achetée.

**La ressource rare se déplace.** Le calcul accéléré concentre désormais la tension,
sur l'approvisionnement comme sur l'alimentation électrique. Un GPU réservé et
inoccupé coûte davantage, en euros comme en carbone, que le serveur comateux
d'hier ([C3](fiches/C3-ia-sobre.md)).

---

## 4. Synthèse : la matrice architecte

Croise chaque fiche avec les couches d'architecture qu'elle mobilise. Une fiche qui
n'active qu'une colonne se traite dans une équipe ; une fiche qui en active cinq
demande un arbitrage transverse.

| Fiche | Stratégie et Gouvernance | Métier | Application | Données | Techno / Infra |
|---|:---:|:---:|:---:|:---:|:---:|
| **G1** Initialiser la démarche | ● | ○ | | | |
| **G2** Embarquer les parties prenantes | ○ | ● | | | |
| **G3** Identifier et prioriser les objectifs | ● | ● | | | |
| **G4** Feuille de route | ● | ● | ○ | ○ | ○ |
| **M1** État des lieux | ○ | ○ | ● | ● | ● |
| **M2** Pilotage et KPI | ● | ○ | ○ | ● | ● |
| **C1** Éco-concevoir les services | | ○ | ● | ○ | ○ |
| **C2** Cycle de vie des données | ○ | ○ | ○ | ● | ○ |
| **C3** Services d'IA sobres | ○ | ○ | ● | ● | ● |
| **C4** Dette d'intégration | ○ | ○ | ● | ● | ● |
| **C5** Accessibilité | ○ | ● | ● | | |
| **I1** Infrastructures et environnements | | | ○ | ○ | ● |
| **I2** Achats responsables | ● | ○ | | | ● |
| **I3** Résilience et sobriété | ● | ○ | ○ | ○ | ● |
| **V1** Maturité des parties prenantes | ● | ● | ○ | ○ | ○ |
| **V2** Souveraineté et réversibilité | ● | ○ | ● | ● | ● |
| **D1** Conformité | ● | ○ | ● | ● | ○ |
| **D2** Communiquer et valoriser | ○ | ● | | | |

**Légende.** **●** Impact primaire · **○** Impact secondaire.

### Par où commencer

Les dix-sept fiches ne se traitent pas de front. Trois séquences possibles selon
votre point de départ.

**Sans mandat.** G1, puis G3 et G2. Obtenir l'arbitrage avant d'engager la mesure,
faute de quoi le diagnostic produit des chiffres que personne ne reprend.

**Avec un mandat, sans chiffres.** M1, puis G4 et M2. Le diagnostic donne la base de
référence, la feuille de route en découle, le pilotage la tient dans le temps.

**Avec un mandat et des chiffres.** Attaquer par la couche où votre diagnostic
signale le plus d'écart : I1 et I3 pour l'infrastructure, C1 et C5 pour les services,
C2 et C4 pour les données et les flux, C3 si l'IA monte en charge, I2 et V1 pour la
chaîne de valeur. D1 et V2 encadrent l'ensemble, D2 le valorise.

> **L'architecte, ambassadeur du Numérique Responsable.** Au terme du parcours, il
> devient le promoteur actif d'un numérique sobre, inclusif et résilient.

---

## 5. Boîte à outils et ressources

!!! tip "Le catalogue de référence"
    L'INR maintient une **[Boîte à outils du Numérique Responsable](https://sustainableit-tools.isit-europe.org/)**
    : 355 ressources (outils de mesure, référentiels, guides, MOOC et textes de loi)
    classées en 15 thèmes, avec recherche, filtres et vérification active des liens.

    La sélection ci-dessous en est un extrait commenté : les outils que le GT AIR
    tient pour structurants dans une démarche d'architecture. Pour un besoin pointu
    ou une veille, allez au catalogue. L'INR le met à jour en continu, quand cette
    page suit le rythme des relectures du GT.

*🟢 = outil open source ; les outils sans pastille ne le sont pas (ou partiellement).*

### Mesure et maturité
| Outil | Usage | Lien |
|---|---|---|
| 🟢 **WeNR** | Empreinte GES + maturité NR du SI (ACV simplifiée + questionnaire DINUM) | <https://wenr.isit-europe.org/> |
| 🟢 **MyImpact** (INR/ISIT) | Calculateur de l'empreinte numérique individuelle (sensibilisation) | <https://myimpact.isit-europe.org/fr/> |
| 🟢 **NumEcoEval** | Évaluation environnementale des SI | — |
| 🟢 **DataVizta** (Boavizta) | Impact fabrication/usage des équipements | <https://dataviz.boavizta.org/> |
| 🟢 **Guide Maturité PP (INR/ISIT)** | 47 questions, 10 familles | <https://institutnr.org/guide-maturite-parties-prenantes> |
| 🟢 **GPC-ONR** (INR) | Évaluation participative, priorisation et consolidation des Objectifs Numérique Responsable (ONR) | <https://github.com/Institut-du-Numerique-Responsable/GPC-ONR> |

### Éco-conception et accessibilité
| Outil | Usage | Lien |
|---|---|---|
| 🟢 **EcoIndex CLI** | Poids des pages, intégrable CI/CD | <https://github.com/cnumr/EcoIndex_python> |
| 🟢 **Lighthouse plugin EcoIndex** | Audit éco-conception | <https://github.com/cnumr/lighthouse-plugin-ecoindex> |
| 🟢 **YellowLab Tools** | Requêtes, poids, perfs front | <https://yellowlab.tools/> |
| **RequestMap** | Cartographie des requêtes | <https://requestmap.webperf.tools/> |
| 🟢 **Tanaguru** | Accessibilité (RGAA / WCAG) | — |
| 🟢 **Skill Accessibilité** (INR) | Génère une déclaration d'accessibilité RGAA conforme au modèle officiel | [Présentation](https://institut-du-numerique-responsable.github.io/claude_skill_accessibilite/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/claude_skill_accessibilite) |
| 🟢 **GR491 (INR)** | Référentiel d'éco-conception | <https://gr491.isit-europe.org/> |
| **RGESN (ARCEP/ARCOM)** | Référentiel général d'éco-conception | <https://ecoresponsable.numerique.gouv.fr/publications/referentiel-general-ecoconception/> |
| 🟢 **Green Claude** (INR) | Skill d'éco-conception pour Claude Code : audit RGESN/GR491/GSF et sobriété IA dans l'IDE | [Présentation](https://institut-du-numerique-responsable.github.io/green-claude/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/green-claude) |
| 🟢 **Skill NR** (INR) | Règles d'éco-conception (RGESN, GR491, Opquast, RGAA) pour 11 assistants IA de code, en 13 langues | [Présentation](https://institut-du-numerique-responsable.github.io/skill-nr/) · [dépôt](https://github.com/Institut-du-Numerique-Responsable/skill-nr) |

### Achats et gouvernance
| Ressource | Usage | Lien |
|---|---|---|
| 🟢 **Clausier NR (INR)** | Clauses types CCTP/CCAP | <https://institutnr.org/clausier-numerique-ecoresponsable> |
| **Dispositif RFAR** | Charte + Label d'État (ISO 20400) | <https://www.economie.gouv.fr/mediateur-des-entreprises> |
| 🟢 **Guide bonnes pratiques NR (INR)** | Référentiel | <https://institutnr.org/guide-bonnes-pratiques-nr> |
| **Guide achats responsables (DINUM)** | Achats | <https://ecoresponsable.numerique.gouv.fr/publications/guide-pratique-achats-numeriques-responsables/> |
| **Label Numérique Responsable** de l'INR et de France IT, opéré par l'Agence LUCIE | Démarche d'amélioration continue proposée en deux niveaux | <https://label-nr.fr/> |
| **ICDSC** | Référentiel international commun utilisé par des organismes labellisateurs indépendants | <https://www.icdsc.eu/> |
| **Charte IA Responsable** (INR) | Cadre d'engagement pour une IA éthique, inclusive, éco-responsable et de confiance ; complète l'AI Act, qui impose des obligations sans dire comment faire | <https://charter.isit-europe.org/charte-ia/?lang=fr_FR> |

### Formation et sensibilisation
| Ressource | Usage | Lien |
|---|---|---|
| 🟢 **MOOC Numérique Responsable** (Académie NR) | Montée en compétences NR (voir la fiche [G2](fiches/G2-parties-prenantes.md)) | <https://www.academie-nr.org/mooc-nr/fr/index.html> |
| 🟢 **MOOC IA Responsable** (Académie NR) | Comprendre et encadrer l'IA responsable | <https://www.academie-nr.org/mooc-ia/fr/index.html> |
| 🟢 **MyImpact** (INR/ISIT) | Calculateur d'empreinte individuelle, support d'ateliers | <https://myimpact.isit-europe.org/fr/> |

### Communication responsable (ADEME)
- ImpactCO₂ : <https://impactco2.fr/outils/numerique>
- Communication responsable : <https://communication-responsable.ademe.fr/>
- Guide anti-greenwashing (2025) : <https://librairie.ademe.fr/>

---

## 6. Glossaire

<figure markdown>
  ![Les trois scopes d'émissions de GES (GHG Protocol / ISO 14064)](assets/img/arbre-ges-scopes.webp)
  <figcaption>Les trois scopes du Bilan GES (GHG Protocol / ISO 14064) : émissions directes (Scope 1), indirectes liées à l'énergie (Scope 2), et indirectes de la chaîne de valeur (Scope 3, jusqu'à 80 %).</figcaption>
</figure>

| Terme | Définition |
|---|---|
| **ACV** | Analyse du Cycle de Vie — impacts sur toutes les phases (fabrication, distribution, usage, fin de vie). |
| **Dark data** | Données conservées sans création de valeur (~52 % d'un SI). |
| **DEEE** | Déchets d'Équipements Électriques et Électroniques. |
| **Éco-conception** | Intégration des critères environnementaux dès la conception. |
| **ESN** | Entreprise de Services du Numérique. |
| **GES / GHG** | Gaz à Effet de Serre / Greenhouse Gas Protocol (Scopes 1, 2, 3). |
| **Maturité (vs performance)** | Capacité à connaître et faire respecter les meilleures pratiques. |
| **NR** | Numérique Responsable. |
| **ODD** | Objectifs de Développement Durable (ONU, 17). |
| **ONR** | Objectifs Numérique Responsable, déclinaison des ambitions NR en objectifs pilotables. |
| **OKR** | *Objectives and Key Results* — objectifs et résultats clés. |
| **PUE** | Power Usage Effectiveness — efficacité énergétique d'un datacenter. |
| **RFI / RFP** | Request For Information (maturité) / Request For Proposal (performance, contractuel). |
| **RGAA / WCAG** | Référentiels d'accessibilité (français / international). |
| **RGESN** | Référentiel Général d'Écoconception des Services Numériques. |
| **ROT** | Données Redondantes, Obsolètes ou Triviales (~33 % d'un SI). |
| **Règle des 3U** | Un service est-il **U**tile, **U**tilisé, **U**tilisable ? |
| **Scope 3** | Émissions indirectes de la chaîne de valeur (jusqu'à 80 %). |
| **TTL** | Time To Live — durée de vie programmée d'un environnement. |
| **VUCA** | Volatile, Uncertain, Complex, Ambiguous. |

---

*Document fusionnant le Livre Blanc AIR (INR, 2024), le Guide des Bonnes Pratiques AIR (2026) et le Guide d'évaluation de la maturité NR des parties prenantes (INR/ISIT, 2024).*

!!! quote "Crédits et licence des illustrations"
    Schémas et illustrations issus des publications du GT AIR de l'**Institut du Numérique Responsable (INR / ISIT)**, diffusés sous licence **[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr)**. Toute réutilisation doit créditer l'INR/ISIT et conserver la même licence.
