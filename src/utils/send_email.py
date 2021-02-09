import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from socket import gethostname

from src.settings import EMAIL, EMAIL_PASSWORD


def send_email(token, email):

    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(EMAIL, EMAIL_PASSWORD)

    try:
        message = f"Olá, Este email foi enviado pelo HOST: {gethostname()}. \n " \
                  f"Segue abaixo seu código de recuperação de login! \n" \
                  f"Token: {token} \n" \
                  f"Atenção! Ele irá expirar em 5 minutos."

        msg = MIMEMultipart()
        msg['Subject'] = 'Recuperação de Senha'
        msg['From'] = EMAIL
        msg['To'] = email
        msg.attach(MIMEText(message))

        smtpObj.send_message(msg)
        print("Email enviado com sucesso")
        return True

    except:
        print("Error sending email")
        return False

