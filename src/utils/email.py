import smtplib
import re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gethostname

from src.settings import EMAIL, EMAIL_PASSWORD


def is_valid_email(email) -> bool:
    return True if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email) else False


def send_email(token, email):

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    message = f"Olá, Este email foi enviado pelo HOST: {gethostname()}. \n " \
              f"Segue abaixo seu código de recuperação de login! \n" \
              f"Token: {token} \n" \
              f"Atenção! Ele irá expirar em 5 minutos."

    try:
        smtpObj.login(EMAIL, EMAIL_PASSWORD)
        msg = MIMEMultipart()
        msg['Subject'] = 'Recuperação de Senha'
        msg['From'] = EMAIL
        msg['To'] = email
        msg.attach(MIMEText(message))

        smtpObj.send_message(msg)

    except Exception as e:
        print("Error sending email")
        raise e.__repr__()

