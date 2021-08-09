# Support de démonstration pour la présentation Tahiti DevOps du 04/08/2021

Ce dépôt contient les recettes permettant de lancer chaque plateforme de logs séparement avec une application générant des logs.
Ces recettes ont été faites pour des besoins de démonstration uniquement. Elles ne doivent pas être utiliser en production directement (pas de TLS, mot de passe par défaut, etc...).

# Installation de la plateforme de logs

- Initialiser Swarm sur votre machine

`
docker swarm init
`
- Lancer votre pile logicielle en utilisant le script **start**.

`
./start [loki,elastic,graylog]
`

- Arrêter votre pile logicielle en utilisant le script **stop**.

`
./stop [loki,elastic,graylog]
`
