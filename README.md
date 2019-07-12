# Home Pod

## About
Home Pod ist eine Web Applikation für den eigenen Heimgebrauch.
Der User kann sich registerieren und danach einloggen. Dort stehen dem User, je nach Rolle, verschiedene Services zur Verfügung.

Momentan verfügbare Dienste:
1. Recorder: Der User kann beim Recorder nach Liedern suchen (Spotify Api) und bekommt eine Auswahl von verschiedenen Liedern mit dem Suchparameter zurück. Die Lieder in der Liste können in eine andere Liste per Drag and Drop überführt werden und an eine Message Queue weiter gegeben werden für die weitere bearbeitung.
2. Wetter: In Planung
3. Finanzen: In Planung
4. Admin kann die System Einstellungen verändern.

## Tech Stack
1. Frontend: Vue.js
2. Backend:
  1. Flask + Flask-Restful + JWT (REST API)
  2. PostgreSQL (DB)
  3. SQLAlchemy
  4. Task Queue (Celery)
  5. Redis

## todo

[ ] Recorder Api verändern und Verbindung zu rabbitMQ
[ ] Code dokumentieren
[ ] Tests weiter schreiben

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

## Notizen
https://github.com/corydolphin/flask-cors/issues/212

https://medium.com/@niveditha.itengineer/learn-how-to-setup-portaudio-and-pyaudio-in-ubuntu-to-play-with-speech-recognition-8d2fff660e94

https://selenium-python.readthedocs.io/navigating.html?highlight=click

https://spotipy.readthedocs.io/en/latest/#authorized-requests


https://developer.spotify.com/console/get-search-item/?q=Hysteria%2CMuse&type=track%2Cartist&market=DE&limit=&offset=

https://stackoverflow.com/questions/46753393/how-to-make-firefox-headless-programmatically-in-selenium-with-python

https://realpython.com/playing-and-recording-sound-python/#python-sounddevice_1

https://stackoverflow.com/questions/10287683/python-convert-wav-to-mp3

https://stackoverflow.com/questions/18599339/python-watchdog-monitoring-file-for-changes

https://www.michaelcho.me/article/using-pythons-watchdog-to-monitor-changes-to-a-directory

https://blog.magrathealabs.com/filesystem-events-monitoring-with-python-9f5329b651c3

https://linuxconfig.org/install-ffmpeg-on-ubuntu-18-04-bionic-beaver-linux
