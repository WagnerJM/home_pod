import os
from celery import Celery, current_task
from celery.result import AsyncResult
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sounddevice as sd
from scipy.io.wavfile import write
import smtplib
from email.message import EmailMessage
from pydub import AudioSegment

REDIS_URL = 'redis://:{pw}@redis:6379/0'.format(pw=os.getenv('REDIS_PW'))
BROKER_URL = 'redis://:{pw}@redis:6379/1'.format(pw=os.getenv('REDIS_PW'))



celery = Celery('tasks', backend=REDIS_URL, broker=BROKER_URL)


@celery.task(name="sendDoneEmail")
def send_email(user_email, settings):

    email = EmailMessage()

    email['Subject'] = "Home Pod Liederliste"
    email['To'] = user_email
    email['From'] = settings.system_email

    body = """
    Lieber Nutzer, \n
    deine Liste wurde vollständig erstellt und liegt im Netzwerkverzeichnis für dich bereit. \n
    \n
    \n
    Viel Spass.\n
    Dein Home Pod Recorder\n
     """
    email.set_content(body)

    s = smtplib.SMTP(host=settings.smtp_host, port=int(settings.smtp_port))
    if settings['email_tls']:
        s.starttls()
        s.login(settings.system_email, settings.email_password)
        s.send_message(email)
        s.quit()
    else:
        s.login(settings.system_email, settings.email_password)
        s.send_message(email)
        s.quit()

@celery.task(name="createRecord")
def create_record(track_name, duration_ms, track_id, settings):
    duration = duration_ms / 1000
    options = Options()
    options.headless = True
    profile = webdriver.FirefoxProfile(settings.profile_path)
    driver = webdriver.Firefox(
        options=options,
        firefox_profile=profile,
        executable_path=settings.driver_path
    )
    spotify_url = "https://open.spotify.com/track/{}".format(track_id)
    driver.get(spotify_url)
    driver.find_element_by_css_selector("button.btn.btn-green").click()
    recording = sd.rec(int(duration * settings.framesize), samplerate=settings.framesize, channels=2)
    sd.wait()
    driver.quit()
    write('/input/{}.wav'.format(track_name), settings.framesize, recording)
    AudioSegment.from_wav(
        '/input/{}.wav'.format(track_name)
        ).export(
            "/output/{}.mp3".format(track_name), format="mp3"
            )



