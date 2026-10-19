import datetime as dt
import os
import smtplib
import ssl
from email.message import EmailMessage
from random import randint
import pandas as pd


THIS_DAY = dt.datetime.now().day
THIS_MONTH = dt.datetime.now().month


def send_mail(letter, mail_to_send):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls(context=ssl.create_default_context())
        connection.login(user= os.getenv('email'), password=os.getenv('pass'))
        message = EmailMessage()
        message["Subject"] = "Happy Birthday"
        message["From"] = os.getenv('email')
        message["To"] = mail_to_send
        message.set_content(letter)
        connection.send_message(message)

def check_birthday():
    for person in all_birthday:
        month = int(person.get('month'))
        day = int(person.get('day'))
        if month == THIS_MONTH:
            if day == THIS_DAY:
                name = person.get('name').title()
                with open(f"./letter_templates/letter_{randint(1, 3)}.txt", encoding="utf-8") as letter_file:
                    letter_to_send = letter_file.read()
                    letter_to_send = letter_to_send.replace("[NAME]", name)
                mail = person.get('email')
                send_mail(letter_to_send, mail)


with open("birthdays.csv", "r", encoding="utf-8") as data_file:
    all_birthday = pd.read_csv(data_file).to_dict(orient="records")


check_birthday()