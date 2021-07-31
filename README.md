# Support de démonstration pour la présentation Tahiti DevOps du 04/08/2021

# Installation de la plateforme de logs

- Initialiser Swarm sur votre machine

`
docker swarm init
`
- Launch your stack using the **start** script

`
./start [loki,elastic,graylog]
`

- Stop your stack when finished using the **stop** script

`
./stop [loki,elastic,graylog]
`
