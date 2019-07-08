# Home Pod

## Notizen
https://developer.spotify.com/console/get-search-item/?q=Hysteria%2CMuse&type=track%2Cartist&market=DE&limit=&offset=

https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python

https://realpython.com/playing-and-recording-sound-python/#python-sounddevice_1

## todo


## Installation

1. Linux Server (vorzugsweise Ubuntu)
    1. Docker installieren
    2. Docker-Compose installieren
2. Backend-Repository klonen
`git clone https://github.com/WagnerJM/home_pod.git`
3. In das Verzeichnis wechseln
`cd quality`
4. Client-Repo klonen
`git clone https://github.com/WagnerJM/home_pod_client.git client`
5. .env Datei erstellen
    `python start.py`
    Dabei werden verschiedene Daten abgefragt die für die App notwendig sind und eine .env Datei erstellt
6. Container bauen und starten
`docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d`

7. Erstelle die Datenbank schemas
Zweites Terminalfenster öffnen und  dort folgendes eingeben.

```docker

docker-compose exec server flask db init

docker-compose exec server flask db migrate

docker-compose exec server flask db upgrade

```

Nachdem das fertig ist, kann mit der App gearbeitet werden.

Der Dienst ist über die <http://Server-IP:8080> erreichbar.
