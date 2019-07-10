# Home Pod

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

### Sample

{
  "tracks": {
    "href": "https://api.spotify.com/v1/search?query=Hysteria&type=track&market=DE&offset=0&limit=20",
    "items": [
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
              },
              "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
              "id": "6H1RjVyNruCmrBEWRbD0VZ",
              "name": "Def Leppard",
              "type": "artist",
              "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/31oeDyCOLhgeZyktfxo0pE"
          },
          "href": "https://api.spotify.com/v1/albums/31oeDyCOLhgeZyktfxo0pE",
          "id": "31oeDyCOLhgeZyktfxo0pE",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5eaab55c9b02be0a4db4ac99ff6da395ddd8bd97",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/42557657129c133bb91e332d61e4b234fccf4aef",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/21fd6d0c0deb3d32710070b125629199f5752c95",
              "width": 64
            }
          ],
          "name": "Hysteria (Super Deluxe)",
          "release_date": "1987-08-03",
          "release_date_precision": "day",
          "total_tracks": 47,
          "type": "album",
          "uri": "spotify:album:31oeDyCOLhgeZyktfxo0pE"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
            },
            "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
            "id": "6H1RjVyNruCmrBEWRbD0VZ",
            "name": "Def Leppard",
            "type": "artist",
            "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 267306,
        "explicit": false,
        "external_ids": {
          "isrc": "GBUM71701307"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0PdM2a6oIjqepoEfcJo0RO"
        },
        "href": "https://api.spotify.com/v1/tracks/0PdM2a6oIjqepoEfcJo0RO",
        "id": "0PdM2a6oIjqepoEfcJo0RO",
        "is_local": false,
        "is_playable": true,
        "name": "Pour Some Sugar On Me - Remastered 2017",
        "popularity": 75,
        "preview_url": null,
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:0PdM2a6oIjqepoEfcJo0RO"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
              },
              "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
              "id": "12Chz98pHFMPJEknJQMWvI",
              "name": "Muse",
              "type": "artist",
              "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0HcHPBu9aaF1MxOiZmUQTl"
          },
          "href": "https://api.spotify.com/v1/albums/0HcHPBu9aaF1MxOiZmUQTl",
          "id": "0HcHPBu9aaF1MxOiZmUQTl",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ae61915fc3f4b3019200ba6ee58a2a85866461bf",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/523194c8f4f32d0d091a7686fea8fda0411b25a5",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/700cdaab602da14c4f007ad2f9cefcbd9292ac24",
              "width": 64
            }
          ],
          "name": "Absolution",
          "release_date": "2004-03-23",
          "release_date_precision": "day",
          "total_tracks": 15,
          "type": "album",
          "uri": "spotify:album:0HcHPBu9aaF1MxOiZmUQTl"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
            },
            "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
            "id": "12Chz98pHFMPJEknJQMWvI",
            "name": "Muse",
            "type": "artist",
            "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
          }
        ],
        "disc_number": 1,
        "duration_ms": 227440,
        "explicit": false,
        "external_ids": {
          "isrc": "GBCVT0300083"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7xyYsOvq5Ec3P4fr6mM9fD"
        },
        "href": "https://api.spotify.com/v1/tracks/7xyYsOvq5Ec3P4fr6mM9fD",
        "id": "7xyYsOvq5Ec3P4fr6mM9fD",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria",
        "popularity": 68,
        "preview_url": "https://p.scdn.co/mp3-preview/ff29ded2c1aa87ed04cb15ea9b1819dc4db95ad7?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 8,
        "type": "track",
        "uri": "spotify:track:7xyYsOvq5Ec3P4fr6mM9fD"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
              },
              "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
              "id": "6H1RjVyNruCmrBEWRbD0VZ",
              "name": "Def Leppard",
              "type": "artist",
              "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1ja2qzCrh6bZykcojbZs82"
          },
          "href": "https://api.spotify.com/v1/albums/1ja2qzCrh6bZykcojbZs82",
          "id": "1ja2qzCrh6bZykcojbZs82",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5eaab55c9b02be0a4db4ac99ff6da395ddd8bd97",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/42557657129c133bb91e332d61e4b234fccf4aef",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/21fd6d0c0deb3d32710070b125629199f5752c95",
              "width": 64
            }
          ],
          "name": "Hysteria",
          "release_date": "1987-08-03",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:1ja2qzCrh6bZykcojbZs82"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
            },
            "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
            "id": "6H1RjVyNruCmrBEWRbD0VZ",
            "name": "Def Leppard",
            "type": "artist",
            "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 354636,
        "explicit": false,
        "external_ids": {
          "isrc": "GBF088700612"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2PFIZFcGry0po3ZfRZkzKc"
        },
        "href": "https://api.spotify.com/v1/tracks/2PFIZFcGry0po3ZfRZkzKc",
        "id": "2PFIZFcGry0po3ZfRZkzKc",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria",
        "popularity": 68,
        "preview_url": null,
        "track_number": 10,
        "type": "track",
        "uri": "spotify:track:2PFIZFcGry0po3ZfRZkzKc"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6swnqiL41Bd4gO2fnAXXrf"
              },
              "href": "https://api.spotify.com/v1/artists/6swnqiL41Bd4gO2fnAXXrf",
              "id": "6swnqiL41Bd4gO2fnAXXrf",
              "name": "Beyond The Black",
              "type": "artist",
              "uri": "spotify:artist:6swnqiL41Bd4gO2fnAXXrf"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/4uu5OSVHvZSh1nXzYPY6YL"
          },
          "href": "https://api.spotify.com/v1/albums/4uu5OSVHvZSh1nXzYPY6YL",
          "id": "4uu5OSVHvZSh1nXzYPY6YL",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/9b9aae2d7d42734963908076367d7fe7a8b9212f",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/98d55f4ae2a51b2064286da664e9dc5d9df5a5ce",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/8b6f5c9534b0a62b4d03fc3e2019c8ce063434bd",
              "width": 64
            }
          ],
          "name": "Heart Of The Hurricane (Black Edition)",
          "release_date": "2019-05-03",
          "release_date_precision": "day",
          "total_tracks": 18,
          "type": "album",
          "uri": "spotify:album:4uu5OSVHvZSh1nXzYPY6YL"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6swnqiL41Bd4gO2fnAXXrf"
            },
            "href": "https://api.spotify.com/v1/artists/6swnqiL41Bd4gO2fnAXXrf",
            "id": "6swnqiL41Bd4gO2fnAXXrf",
            "name": "Beyond The Black",
            "type": "artist",
            "uri": "spotify:artist:6swnqiL41Bd4gO2fnAXXrf"
          }
        ],
        "disc_number": 1,
        "duration_ms": 277200,
        "explicit": false,
        "external_ids": {
          "isrc": "DEUM71801888"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4eSwvKtbxU9fKVVVidtrNG"
        },
        "href": "https://api.spotify.com/v1/tracks/4eSwvKtbxU9fKVVVidtrNG",
        "id": "4eSwvKtbxU9fKVVVidtrNG",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria",
        "popularity": 39,
        "preview_url": null,
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:4eSwvKtbxU9fKVVVidtrNG"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4OPaH4YIqua9DUnI7t0fOQ"
              },
              "href": "https://api.spotify.com/v1/artists/4OPaH4YIqua9DUnI7t0fOQ",
              "id": "4OPaH4YIqua9DUnI7t0fOQ",
              "name": "Mark With a K",
              "type": "artist",
              "uri": "spotify:artist:4OPaH4YIqua9DUnI7t0fOQ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/7iFeEo0FIZahyA9bLETCEK"
          },
          "href": "https://api.spotify.com/v1/albums/7iFeEo0FIZahyA9bLETCEK",
          "id": "7iFeEo0FIZahyA9bLETCEK",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/2fc77f627c2d7c549abe4ae47f179d1ac6b7f7e0",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/d7f7b68aedc3a0f61ad2f1376448062c228950ba",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/379bc64709b8a34b3fcb91d0c7eaf762032fa363",
              "width": 64
            }
          ],
          "name": "Mass Hysteria",
          "release_date": "2018-01-20",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:7iFeEo0FIZahyA9bLETCEK"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4OPaH4YIqua9DUnI7t0fOQ"
            },
            "href": "https://api.spotify.com/v1/artists/4OPaH4YIqua9DUnI7t0fOQ",
            "id": "4OPaH4YIqua9DUnI7t0fOQ",
            "name": "Mark With a K",
            "type": "artist",
            "uri": "spotify:artist:4OPaH4YIqua9DUnI7t0fOQ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 86000,
        "explicit": false,
        "external_ids": {
          "isrc": "BEB681800001"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2luhMkNTkkvCCtcmlqw9IJ"
        },
        "href": "https://api.spotify.com/v1/tracks/2luhMkNTkkvCCtcmlqw9IJ",
        "id": "2luhMkNTkkvCCtcmlqw9IJ",
        "is_local": false,
        "is_playable": true,
        "name": "Bombs Away (Intro)",
        "popularity": 40,
        "preview_url": "https://p.scdn.co/mp3-preview/4a2782a4ac76b4051f061888aa65e7101688c8d3?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:2luhMkNTkkvCCtcmlqw9IJ"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
              },
              "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
              "id": "6H1RjVyNruCmrBEWRbD0VZ",
              "name": "Def Leppard",
              "type": "artist",
              "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/31oeDyCOLhgeZyktfxo0pE"
          },
          "href": "https://api.spotify.com/v1/albums/31oeDyCOLhgeZyktfxo0pE",
          "id": "31oeDyCOLhgeZyktfxo0pE",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5eaab55c9b02be0a4db4ac99ff6da395ddd8bd97",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/42557657129c133bb91e332d61e4b234fccf4aef",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/21fd6d0c0deb3d32710070b125629199f5752c95",
              "width": 64
            }
          ],
          "name": "Hysteria (Super Deluxe)",
          "release_date": "1987-08-03",
          "release_date_precision": "day",
          "total_tracks": 47,
          "type": "album",
          "uri": "spotify:album:31oeDyCOLhgeZyktfxo0pE"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
            },
            "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
            "id": "6H1RjVyNruCmrBEWRbD0VZ",
            "name": "Def Leppard",
            "type": "artist",
            "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 346960,
        "explicit": false,
        "external_ids": {
          "isrc": "GBUM71701306"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/3Dfy8YIxq89i84t108TvMi"
        },
        "href": "https://api.spotify.com/v1/tracks/3Dfy8YIxq89i84t108TvMi",
        "id": "3Dfy8YIxq89i84t108TvMi",
        "is_local": false,
        "is_playable": true,
        "name": "Love Bites - Remastered 2017",
        "popularity": 63,
        "preview_url": null,
        "track_number": 4,
        "type": "track",
        "uri": "spotify:track:3Dfy8YIxq89i84t108TvMi"
      },
      {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4bazJLWIv8CuqmgxJRiGqo"
              },
              "href": "https://api.spotify.com/v1/artists/4bazJLWIv8CuqmgxJRiGqo",
              "id": "4bazJLWIv8CuqmgxJRiGqo",
              "name": "Just Kiddin",
              "type": "artist",
              "uri": "spotify:artist:4bazJLWIv8CuqmgxJRiGqo"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1Xi2SGir1ScYoV9dfRAW8t"
          },
          "href": "https://api.spotify.com/v1/albums/1Xi2SGir1ScYoV9dfRAW8t",
          "id": "1Xi2SGir1ScYoV9dfRAW8t",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/d4e64e514ff2c8e2ca2a8688162561a087f0a29b",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/bbac132922fb3cb0624975dc933c142b702ec410",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/1a0174dafcfb7d638862e0619bb2783b806fe28a",
              "width": 64
            }
          ],
          "name": "Hysteria",
          "release_date": "2018-10-05",
          "release_date_precision": "day",
          "total_tracks": 1,
          "type": "album",
          "uri": "spotify:album:1Xi2SGir1ScYoV9dfRAW8t"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4bazJLWIv8CuqmgxJRiGqo"
            },
            "href": "https://api.spotify.com/v1/artists/4bazJLWIv8CuqmgxJRiGqo",
            "id": "4bazJLWIv8CuqmgxJRiGqo",
            "name": "Just Kiddin",
            "type": "artist",
            "uri": "spotify:artist:4bazJLWIv8CuqmgxJRiGqo"
          }
        ],
        "disc_number": 1,
        "duration_ms": 194150,
        "explicit": false,
        "external_ids": {
          "isrc": "GBARL1801367"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5iLaZsbuWFSnyoY6BJ6JmB"
        },
        "href": "https://api.spotify.com/v1/tracks/5iLaZsbuWFSnyoY6BJ6JmB",
        "id": "5iLaZsbuWFSnyoY6BJ6JmB",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria",
        "popularity": 50,
        "preview_url": "https://p.scdn.co/mp3-preview/939fd74336469c1bf1ddab6aad37167b9c8c0b59?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 1,
        "type": "track",
        "uri": "spotify:track:5iLaZsbuWFSnyoY6BJ6JmB"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4OPaH4YIqua9DUnI7t0fOQ"
              },
              "href": "https://api.spotify.com/v1/artists/4OPaH4YIqua9DUnI7t0fOQ",
              "id": "4OPaH4YIqua9DUnI7t0fOQ",
              "name": "Mark With a K",
              "type": "artist",
              "uri": "spotify:artist:4OPaH4YIqua9DUnI7t0fOQ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/7iFeEo0FIZahyA9bLETCEK"
          },
          "href": "https://api.spotify.com/v1/albums/7iFeEo0FIZahyA9bLETCEK",
          "id": "7iFeEo0FIZahyA9bLETCEK",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/2fc77f627c2d7c549abe4ae47f179d1ac6b7f7e0",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/d7f7b68aedc3a0f61ad2f1376448062c228950ba",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/379bc64709b8a34b3fcb91d0c7eaf762032fa363",
              "width": 64
            }
          ],
          "name": "Mass Hysteria",
          "release_date": "2018-01-20",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:7iFeEo0FIZahyA9bLETCEK"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4OPaH4YIqua9DUnI7t0fOQ"
            },
            "href": "https://api.spotify.com/v1/artists/4OPaH4YIqua9DUnI7t0fOQ",
            "id": "4OPaH4YIqua9DUnI7t0fOQ",
            "name": "Mark With a K",
            "type": "artist",
            "uri": "spotify:artist:4OPaH4YIqua9DUnI7t0fOQ"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5CVwY7MrkxGF1aM4f1u6Xk"
            },
            "href": "https://api.spotify.com/v1/artists/5CVwY7MrkxGF1aM4f1u6Xk",
            "id": "5CVwY7MrkxGF1aM4f1u6Xk",
            "name": "Robert Falcon",
            "type": "artist",
            "uri": "spotify:artist:5CVwY7MrkxGF1aM4f1u6Xk"
          }
        ],
        "disc_number": 1,
        "duration_ms": 218322,
        "explicit": false,
        "external_ids": {
          "isrc": "BEB681700232"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/7eDCoOxaczn7Uwoqtogu70"
        },
        "href": "https://api.spotify.com/v1/tracks/7eDCoOxaczn7Uwoqtogu70",
        "id": "7eDCoOxaczn7Uwoqtogu70",
        "is_local": false,
        "is_playable": true,
        "name": "Warrior - Extended Version",
        "popularity": 42,
        "preview_url": "https://p.scdn.co/mp3-preview/316f78ad13e4c1e095ec76e2b9f713755fc1d195?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 4,
        "type": "track",
        "uri": "spotify:track:7eDCoOxaczn7Uwoqtogu70"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
              },
              "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
              "id": "6H1RjVyNruCmrBEWRbD0VZ",
              "name": "Def Leppard",
              "type": "artist",
              "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1ja2qzCrh6bZykcojbZs82"
          },
          "href": "https://api.spotify.com/v1/albums/1ja2qzCrh6bZykcojbZs82",
          "id": "1ja2qzCrh6bZykcojbZs82",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5eaab55c9b02be0a4db4ac99ff6da395ddd8bd97",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/42557657129c133bb91e332d61e4b234fccf4aef",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/21fd6d0c0deb3d32710070b125629199f5752c95",
              "width": 64
            }
          ],
          "name": "Hysteria",
          "release_date": "1987-08-03",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:1ja2qzCrh6bZykcojbZs82"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
            },
            "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
            "id": "6H1RjVyNruCmrBEWRbD0VZ",
            "name": "Def Leppard",
            "type": "artist",
            "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 244560,
        "explicit": false,
        "external_ids": {
          "isrc": "GBF088700196"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4qjscZh4jfhkpcQG4ZQfi2"
        },
        "href": "https://api.spotify.com/v1/tracks/4qjscZh4jfhkpcQG4ZQfi2",
        "id": "4qjscZh4jfhkpcQG4ZQfi2",
        "is_local": false,
        "is_playable": true,
        "name": "Animal",
        "popularity": 60,
        "preview_url": null,
        "track_number": 3,
        "type": "track",
        "uri": "spotify:track:4qjscZh4jfhkpcQG4ZQfi2"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/4OPaH4YIqua9DUnI7t0fOQ"
              },
              "href": "https://api.spotify.com/v1/artists/4OPaH4YIqua9DUnI7t0fOQ",
              "id": "4OPaH4YIqua9DUnI7t0fOQ",
              "name": "Mark With a K",
              "type": "artist",
              "uri": "spotify:artist:4OPaH4YIqua9DUnI7t0fOQ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/7iFeEo0FIZahyA9bLETCEK"
          },
          "href": "https://api.spotify.com/v1/albums/7iFeEo0FIZahyA9bLETCEK",
          "id": "7iFeEo0FIZahyA9bLETCEK",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/2fc77f627c2d7c549abe4ae47f179d1ac6b7f7e0",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/d7f7b68aedc3a0f61ad2f1376448062c228950ba",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/379bc64709b8a34b3fcb91d0c7eaf762032fa363",
              "width": 64
            }
          ],
          "name": "Mass Hysteria",
          "release_date": "2018-01-20",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:7iFeEo0FIZahyA9bLETCEK"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4OPaH4YIqua9DUnI7t0fOQ"
            },
            "href": "https://api.spotify.com/v1/artists/4OPaH4YIqua9DUnI7t0fOQ",
            "id": "4OPaH4YIqua9DUnI7t0fOQ",
            "name": "Mark With a K",
            "type": "artist",
            "uri": "spotify:artist:4OPaH4YIqua9DUnI7t0fOQ"
          },
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/4FApejrnKXgmvrVmBMRO2l"
            },
            "href": "https://api.spotify.com/v1/artists/4FApejrnKXgmvrVmBMRO2l",
            "id": "4FApejrnKXgmvrVmBMRO2l",
            "name": "Sub Sonik",
            "type": "artist",
            "uri": "spotify:artist:4FApejrnKXgmvrVmBMRO2l"
          }
        ],
        "disc_number": 1,
        "duration_ms": 200800,
        "explicit": false,
        "external_ids": {
          "isrc": "BEB681800008"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/4lIsk1P3Kjh9p5p8BIf0sH"
        },
        "href": "https://api.spotify.com/v1/tracks/4lIsk1P3Kjh9p5p8BIf0sH",
        "id": "4lIsk1P3Kjh9p5p8BIf0sH",
        "is_local": false,
        "is_playable": true,
        "name": "MoneyShaker (Sub Sonik remix)",
        "popularity": 41,
        "preview_url": "https://p.scdn.co/mp3-preview/842cc8a9bf5eb3a2856b620aa644366fcd6de8b0?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 12,
        "type": "track",
        "uri": "spotify:track:4lIsk1P3Kjh9p5p8BIf0sH"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
              },
              "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
              "id": "6H1RjVyNruCmrBEWRbD0VZ",
              "name": "Def Leppard",
              "type": "artist",
              "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/31oeDyCOLhgeZyktfxo0pE"
          },
          "href": "https://api.spotify.com/v1/albums/31oeDyCOLhgeZyktfxo0pE",
          "id": "31oeDyCOLhgeZyktfxo0pE",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5eaab55c9b02be0a4db4ac99ff6da395ddd8bd97",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/42557657129c133bb91e332d61e4b234fccf4aef",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/21fd6d0c0deb3d32710070b125629199f5752c95",
              "width": 64
            }
          ],
          "name": "Hysteria (Super Deluxe)",
          "release_date": "1987-08-03",
          "release_date_precision": "day",
          "total_tracks": 47,
          "type": "album",
          "uri": "spotify:album:31oeDyCOLhgeZyktfxo0pE"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
            },
            "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
            "id": "6H1RjVyNruCmrBEWRbD0VZ",
            "name": "Def Leppard",
            "type": "artist",
            "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 354636,
        "explicit": false,
        "external_ids": {
          "isrc": "GBUM71701313"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/6EzSduIPnAmO3o41HY5V9d"
        },
        "href": "https://api.spotify.com/v1/tracks/6EzSduIPnAmO3o41HY5V9d",
        "id": "6EzSduIPnAmO3o41HY5V9d",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria - Remastered 2017",
        "popularity": 54,
        "preview_url": null,
        "track_number": 10,
        "type": "track",
        "uri": "spotify:track:6EzSduIPnAmO3o41HY5V9d"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/5gspAQIAH8nJUrMYgXjCJ2"
              },
              "href": "https://api.spotify.com/v1/artists/5gspAQIAH8nJUrMYgXjCJ2",
              "id": "5gspAQIAH8nJUrMYgXjCJ2",
              "name": "Kurt Vile",
              "type": "artist",
              "uri": "spotify:artist:5gspAQIAH8nJUrMYgXjCJ2"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/7lXj7neMWuwD4PTYkaToes"
          },
          "href": "https://api.spotify.com/v1/albums/7lXj7neMWuwD4PTYkaToes",
          "id": "7lXj7neMWuwD4PTYkaToes",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/9250eed9f36bd1db7b2d6ed6df8c4ec9b60f9f07",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/01ec7e0fb6fe4aeb4e42b66bedf521d13d3ff24f",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/4a6c3ae8626045e2d5ebcd63e4280906e1a20c31",
              "width": 64
            }
          ],
          "name": "Bottle It In",
          "release_date": "2018-10-12",
          "release_date_precision": "day",
          "total_tracks": 13,
          "type": "album",
          "uri": "spotify:album:7lXj7neMWuwD4PTYkaToes"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/5gspAQIAH8nJUrMYgXjCJ2"
            },
            "href": "https://api.spotify.com/v1/artists/5gspAQIAH8nJUrMYgXjCJ2",
            "id": "5gspAQIAH8nJUrMYgXjCJ2",
            "name": "Kurt Vile",
            "type": "artist",
            "uri": "spotify:artist:5gspAQIAH8nJUrMYgXjCJ2"
          }
        ],
        "disc_number": 1,
        "duration_ms": 322813,
        "explicit": false,
        "external_ids": {
          "isrc": "USMTD1811826"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1oRu9aGmEgnzxrtyz601j7"
        },
        "href": "https://api.spotify.com/v1/tracks/1oRu9aGmEgnzxrtyz601j7",
        "id": "1oRu9aGmEgnzxrtyz601j7",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria",
        "popularity": 43,
        "preview_url": "https://p.scdn.co/mp3-preview/5cde479eb9fd6317aeed3d8b988f4c2d6282d921?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:1oRu9aGmEgnzxrtyz601j7"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/1aX2dmV8XoHYCOQRxjPESG"
              },
              "href": "https://api.spotify.com/v1/artists/1aX2dmV8XoHYCOQRxjPESG",
              "id": "1aX2dmV8XoHYCOQRxjPESG",
              "name": "The Human League",
              "type": "artist",
              "uri": "spotify:artist:1aX2dmV8XoHYCOQRxjPESG"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0Jst3a86SKc0inDa2AKhXf"
          },
          "href": "https://api.spotify.com/v1/albums/0Jst3a86SKc0inDa2AKhXf",
          "id": "0Jst3a86SKc0inDa2AKhXf",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/e718abfe684c1e430a3d62e9af035dd8c50620d0",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/6b645b513602c7fb96d33ff822924aea64376c89",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/abd7c87d180d267922540724bd1daff63acbf39f",
              "width": 64
            }
          ],
          "name": "Hysteria",
          "release_date": "1984-01-01",
          "release_date_precision": "day",
          "total_tracks": 10,
          "type": "album",
          "uri": "spotify:album:0Jst3a86SKc0inDa2AKhXf"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/1aX2dmV8XoHYCOQRxjPESG"
            },
            "href": "https://api.spotify.com/v1/artists/1aX2dmV8XoHYCOQRxjPESG",
            "id": "1aX2dmV8XoHYCOQRxjPESG",
            "name": "The Human League",
            "type": "artist",
            "uri": "spotify:artist:1aX2dmV8XoHYCOQRxjPESG"
          }
        ],
        "disc_number": 1,
        "duration_ms": 304906,
        "explicit": false,
        "external_ids": {
          "isrc": "GBAAA8400225"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5d4ZCmvSLvjMOSdIKkCyQ5"
        },
        "href": "https://api.spotify.com/v1/tracks/5d4ZCmvSLvjMOSdIKkCyQ5",
        "id": "5d4ZCmvSLvjMOSdIKkCyQ5",
        "is_local": false,
        "is_playable": true,
        "name": "The Lebanon",
        "popularity": 47,
        "preview_url": null,
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:5d4ZCmvSLvjMOSdIKkCyQ5"
      },
      {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/37YzpfBeFju8QRZ3g0Ha1Q"
              },
              "href": "https://api.spotify.com/v1/artists/37YzpfBeFju8QRZ3g0Ha1Q",
              "id": "37YzpfBeFju8QRZ3g0Ha1Q",
              "name": "DJ Seinfeld",
              "type": "artist",
              "uri": "spotify:artist:37YzpfBeFju8QRZ3g0Ha1Q"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0THSg7Bjuj72dVntvDtXPG"
          },
          "href": "https://api.spotify.com/v1/albums/0THSg7Bjuj72dVntvDtXPG",
          "id": "0THSg7Bjuj72dVntvDtXPG",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/cbf800b43f8f33c04f6ae9de22bdcffe9ab87412",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/63ffff700146a058f73a60180ba1ca955015c530",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/618efee957b8c59991df56202834542b03564b45",
              "width": 64
            }
          ],
          "name": "Ruff Hysteria",
          "release_date": "2017-11-17",
          "release_date_precision": "day",
          "total_tracks": 4,
          "type": "album",
          "uri": "spotify:album:0THSg7Bjuj72dVntvDtXPG"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/37YzpfBeFju8QRZ3g0Ha1Q"
            },
            "href": "https://api.spotify.com/v1/artists/37YzpfBeFju8QRZ3g0Ha1Q",
            "id": "37YzpfBeFju8QRZ3g0Ha1Q",
            "name": "DJ Seinfeld",
            "type": "artist",
            "uri": "spotify:artist:37YzpfBeFju8QRZ3g0Ha1Q"
          }
        ],
        "disc_number": 1,
        "duration_ms": 360000,
        "explicit": false,
        "external_ids": {
          "isrc": "GBQLP1700339"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/5cJnjUiWhTTBwT4Fo2J7rM"
        },
        "href": "https://api.spotify.com/v1/tracks/5cJnjUiWhTTBwT4Fo2J7rM",
        "id": "5cJnjUiWhTTBwT4Fo2J7rM",
        "is_local": false,
        "is_playable": true,
        "name": "Ruff Hysteria",
        "popularity": 41,
        "preview_url": "https://p.scdn.co/mp3-preview/b78edc725f1e26f19b3a75d3d4eb2c3a32072b14?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:5cJnjUiWhTTBwT4Fo2J7rM"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
              },
              "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
              "id": "12Chz98pHFMPJEknJQMWvI",
              "name": "Muse",
              "type": "artist",
              "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/2m7L60M210ABzrY9GLyBPZ"
          },
          "href": "https://api.spotify.com/v1/albums/2m7L60M210ABzrY9GLyBPZ",
          "id": "2m7L60M210ABzrY9GLyBPZ",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/05c049956ed66d6dd3451d9ac06e0f30ff1693b3",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/71a45fc4b9d8f4f5e0998751f7c29a97f5f0fdd3",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/680b385164b970b271365f2da1271bc642b77fb7",
              "width": 64
            }
          ],
          "name": "Live At Rome Olympic Stadium",
          "release_date": "2013-11-25",
          "release_date_precision": "day",
          "total_tracks": 13,
          "type": "album",
          "uri": "spotify:album:2m7L60M210ABzrY9GLyBPZ"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
            },
            "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
            "id": "12Chz98pHFMPJEknJQMWvI",
            "name": "Muse",
            "type": "artist",
            "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
          }
        ],
        "disc_number": 1,
        "duration_ms": 306146,
        "explicit": false,
        "external_ids": {
          "isrc": "GBAHT1326111"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/57IRQzhQiU3RHYFxofASv1"
        },
        "href": "https://api.spotify.com/v1/tracks/57IRQzhQiU3RHYFxofASv1",
        "id": "57IRQzhQiU3RHYFxofASv1",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria - Live at Rome Olympic Stadium",
        "popularity": 45,
        "preview_url": "https://p.scdn.co/mp3-preview/8799760591ada0579dce55f408b157ce8974c391?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 4,
        "type": "track",
        "uri": "spotify:track:57IRQzhQiU3RHYFxofASv1"
      },
      {
        "album": {
          "album_type": "single",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
              },
              "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
              "id": "12Chz98pHFMPJEknJQMWvI",
              "name": "Muse",
              "type": "artist",
              "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/16rRWuAQcgHUNYs7u0hLTr"
          },
          "href": "https://api.spotify.com/v1/albums/16rRWuAQcgHUNYs7u0hLTr",
          "id": "16rRWuAQcgHUNYs7u0hLTr",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/e757c4ddc322b554fc98ab6c4172fc1a74b6ef62",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/7a4b10da62095d2ed26e37a296b95f7c577a4718",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/65584d1c25e8fc21abc788124adef15251f795b4",
              "width": 64
            }
          ],
          "name": "Hysteria",
          "release_date": "2003",
          "release_date_precision": "year",
          "total_tracks": 2,
          "type": "album",
          "uri": "spotify:album:16rRWuAQcgHUNYs7u0hLTr"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/12Chz98pHFMPJEknJQMWvI"
            },
            "href": "https://api.spotify.com/v1/artists/12Chz98pHFMPJEknJQMWvI",
            "id": "12Chz98pHFMPJEknJQMWvI",
            "name": "Muse",
            "type": "artist",
            "uri": "spotify:artist:12Chz98pHFMPJEknJQMWvI"
          }
        ],
        "disc_number": 1,
        "duration_ms": 366866,
        "explicit": false,
        "external_ids": {
          "isrc": "GBCVT0300111"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/00Qum7j2nKb2wKo8floWBy"
        },
        "href": "https://api.spotify.com/v1/tracks/00Qum7j2nKb2wKo8floWBy",
        "id": "00Qum7j2nKb2wKo8floWBy",
        "is_local": false,
        "is_playable": true,
        "name": "Eternally Missed",
        "popularity": 49,
        "preview_url": "https://p.scdn.co/mp3-preview/56de2273fdd6e17cac1d90947c09e058801c8dfc?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:00Qum7j2nKb2wKo8floWBy"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/7oPftvlwr6VrsViSDV7fJY"
              },
              "href": "https://api.spotify.com/v1/artists/7oPftvlwr6VrsViSDV7fJY",
              "id": "7oPftvlwr6VrsViSDV7fJY",
              "name": "Green Day",
              "type": "artist",
              "uri": "spotify:artist:7oPftvlwr6VrsViSDV7fJY"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1AHZd3C3S8m8fFrhFxyk79"
          },
          "href": "https://api.spotify.com/v1/albums/1AHZd3C3S8m8fFrhFxyk79",
          "id": "1AHZd3C3S8m8fFrhFxyk79",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/674099a68b30a3188ee213cd8ca260fa1daf00e9",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/b732ba0c7488b4ff6582ff0b44b4c9b166495048",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/c56af2618d8d9d8680c4b7484984f1bace6feb4d",
              "width": 64
            }
          ],
          "name": "21st Century Breakdown",
          "release_date": "2009-05-15",
          "release_date_precision": "day",
          "total_tracks": 18,
          "type": "album",
          "uri": "spotify:album:1AHZd3C3S8m8fFrhFxyk79"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/7oPftvlwr6VrsViSDV7fJY"
            },
            "href": "https://api.spotify.com/v1/artists/7oPftvlwr6VrsViSDV7fJY",
            "id": "7oPftvlwr6VrsViSDV7fJY",
            "name": "Green Day",
            "type": "artist",
            "uri": "spotify:artist:7oPftvlwr6VrsViSDV7fJY"
          }
        ],
        "disc_number": 1,
        "duration_ms": 266106,
        "explicit": true,
        "external_ids": {
          "isrc": "USRE10900680"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/2DSgsIY3ZCjx7DhMNRzsSS"
        },
        "href": "https://api.spotify.com/v1/tracks/2DSgsIY3ZCjx7DhMNRzsSS",
        "id": "2DSgsIY3ZCjx7DhMNRzsSS",
        "is_local": false,
        "is_playable": true,
        "name": "American Eulogy: Mass Hysteria / Modern World",
        "popularity": 44,
        "preview_url": "https://p.scdn.co/mp3-preview/f29d3bb1ae8f063bb25c79ae11c48e73f2dfc2e6?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 17,
        "type": "track",
        "uri": "spotify:track:2DSgsIY3ZCjx7DhMNRzsSS"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
              },
              "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
              "id": "6H1RjVyNruCmrBEWRbD0VZ",
              "name": "Def Leppard",
              "type": "artist",
              "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/0IXPDVnECWSt6NFLDlgpoC"
          },
          "href": "https://api.spotify.com/v1/albums/0IXPDVnECWSt6NFLDlgpoC",
          "id": "0IXPDVnECWSt6NFLDlgpoC",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/2debd96dfa4f16c73a796f5b97effc2800906be8",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/3e071554160ad3536e86346d7fa9da74fd7b76ea",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/80cd6c8b8a5d81f18325f22ee7019dd36f8680ee",
              "width": 64
            }
          ],
          "name": "Viva! Hysteria (Original Soundtrack)",
          "release_date": "2013-10-18",
          "release_date_precision": "day",
          "total_tracks": 29,
          "type": "album",
          "uri": "spotify:album:0IXPDVnECWSt6NFLDlgpoC"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
            },
            "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
            "id": "6H1RjVyNruCmrBEWRbD0VZ",
            "name": "Def Leppard",
            "type": "artist",
            "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 272173,
        "explicit": false,
        "external_ids": {
          "isrc": "ITG271300491"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0pKGbgGzZ4yLydQvcgI8HN"
        },
        "href": "https://api.spotify.com/v1/tracks/0pKGbgGzZ4yLydQvcgI8HN",
        "id": "0pKGbgGzZ4yLydQvcgI8HN",
        "is_local": false,
        "is_playable": true,
        "name": "Pour Some Sugar on Me",
        "popularity": 45,
        "preview_url": "https://p.scdn.co/mp3-preview/9722e601b1112f7c47bfa9ff59fb55ced5709b49?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:0pKGbgGzZ4yLydQvcgI8HN"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6Fi8CHfO8WGtu3yO8c2Mc4"
              },
              "href": "https://api.spotify.com/v1/artists/6Fi8CHfO8WGtu3yO8c2Mc4",
              "id": "6Fi8CHfO8WGtu3yO8c2Mc4",
              "name": "2CELLOS",
              "type": "artist",
              "uri": "spotify:artist:6Fi8CHfO8WGtu3yO8c2Mc4"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/5YBY91ePHZWzgsLRrDK8DI"
          },
          "href": "https://api.spotify.com/v1/albums/5YBY91ePHZWzgsLRrDK8DI",
          "id": "5YBY91ePHZWzgsLRrDK8DI",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/4e3a2c94ed3e0daf2514f08bae2d1896c6b673ff",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/3b9a0f9a6d294208c48adc33345188aad7fad15c",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/9dec3f7b32def7a53f6512bfef1391ec8c98434a",
              "width": 64
            }
          ],
          "name": "Celloverse",
          "release_date": "2015-01-09",
          "release_date_precision": "day",
          "total_tracks": 13,
          "type": "album",
          "uri": "spotify:album:5YBY91ePHZWzgsLRrDK8DI"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6Fi8CHfO8WGtu3yO8c2Mc4"
            },
            "href": "https://api.spotify.com/v1/artists/6Fi8CHfO8WGtu3yO8c2Mc4",
            "id": "6Fi8CHfO8WGtu3yO8c2Mc4",
            "name": "2CELLOS",
            "type": "artist",
            "uri": "spotify:artist:6Fi8CHfO8WGtu3yO8c2Mc4"
          }
        ],
        "disc_number": 1,
        "duration_ms": 170773,
        "explicit": false,
        "external_ids": {
          "isrc": "USSM11400338"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/1SXS3Ea9CVCoRIC8aKKQEJ"
        },
        "href": "https://api.spotify.com/v1/tracks/1SXS3Ea9CVCoRIC8aKKQEJ",
        "id": "1SXS3Ea9CVCoRIC8aKKQEJ",
        "is_local": false,
        "is_playable": true,
        "name": "Hysteria",
        "popularity": 41,
        "preview_url": "https://p.scdn.co/mp3-preview/a157d3491ec66e7e5a039091fb7d8f3eaacd5f22?cid=774b29d4f13844c495f206cafdad9c86",
        "track_number": 5,
        "type": "track",
        "uri": "spotify:track:1SXS3Ea9CVCoRIC8aKKQEJ"
      },
      {
        "album": {
          "album_type": "album",
          "artists": [
            {
              "external_urls": {
                "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
              },
              "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
              "id": "6H1RjVyNruCmrBEWRbD0VZ",
              "name": "Def Leppard",
              "type": "artist",
              "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
            }
          ],
          "external_urls": {
            "spotify": "https://open.spotify.com/album/1ja2qzCrh6bZykcojbZs82"
          },
          "href": "https://api.spotify.com/v1/albums/1ja2qzCrh6bZykcojbZs82",
          "id": "1ja2qzCrh6bZykcojbZs82",
          "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/5eaab55c9b02be0a4db4ac99ff6da395ddd8bd97",
              "width": 640
            },
            {
              "height": 300,
              "url": "https://i.scdn.co/image/42557657129c133bb91e332d61e4b234fccf4aef",
              "width": 300
            },
            {
              "height": 64,
              "url": "https://i.scdn.co/image/21fd6d0c0deb3d32710070b125629199f5752c95",
              "width": 64
            }
          ],
          "name": "Hysteria",
          "release_date": "1987-08-03",
          "release_date_precision": "day",
          "total_tracks": 12,
          "type": "album",
          "uri": "spotify:album:1ja2qzCrh6bZykcojbZs82"
        },
        "artists": [
          {
            "external_urls": {
              "spotify": "https://open.spotify.com/artist/6H1RjVyNruCmrBEWRbD0VZ"
            },
            "href": "https://api.spotify.com/v1/artists/6H1RjVyNruCmrBEWRbD0VZ",
            "id": "6H1RjVyNruCmrBEWRbD0VZ",
            "name": "Def Leppard",
            "type": "artist",
            "uri": "spotify:artist:6H1RjVyNruCmrBEWRbD0VZ"
          }
        ],
        "disc_number": 1,
        "duration_ms": 396823,
        "explicit": false,
        "external_ids": {
          "isrc": "GBF088790002"
        },
        "external_urls": {
          "spotify": "https://open.spotify.com/track/0RVeadY2MbHz4Pe4MreLNw"
        },
        "href": "https://api.spotify.com/v1/tracks/0RVeadY2MbHz4Pe4MreLNw",
        "id": "0RVeadY2MbHz4Pe4MreLNw",
        "is_local": false,
        "is_playable": true,
        "name": "Rocket",
        "popularity": 53,
        "preview_url": null,
        "track_number": 2,
        "type": "track",
        "uri": "spotify:track:0RVeadY2MbHz4Pe4MreLNw"
      }
    ],
    "limit": 20,
    "next": "https://api.spotify.com/v1/search?query=Hysteria&type=track&market=DE&offset=20&limit=20",
    "offset": 0,
    "previous": null,
    "total": 3726
  }
}