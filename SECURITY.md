# Politique de sécurité

Ce dépôt héberge un site de documentation statique : ni backend, ni base de
données, ni données personnelles. La surface d'attaque se limite à la chaîne de
publication (GitHub Actions, GitHub Pages) et aux dépendances de build.

## Signaler une vulnérabilité

N'ouvrez pas d'issue publique pour une vulnérabilité.

Écrivez à **contact@institutnr.org** en décrivant le problème, les étapes de
reproduction et l'impact estimé. Nous accusons réception sous 5 jours ouvrés.

## Périmètre

Sont dans le périmètre : la configuration des workflows, les dépendances de
build (`requirements.txt`), les surcharges de thème (`overrides/`) et le hook de
génération (`hooks/`).

Sont hors périmètre : les sites tiers cités dans les fiches, et les signalements
portant sur l'exactitude du contenu — qui relèvent d'une
[issue](https://github.com/Institut-du-Numerique-Responsable/BP-AIR/issues).
