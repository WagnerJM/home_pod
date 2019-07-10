import os
from celery import Celery, current_task
from celery.result import AsyncResult
from selenium import webdriver
import smtplib
from email.message import EmailMessage

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




