import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def send_mes(msg: str):
    sender = "codered-it@coderedit.ru"
    password = "Stas-2001"

    server = smtplib.SMTP("smtp.beget.com", 2525)
    server.starttls()

    user_from = 'stanislavd491@gmail.com'
    try:
        server.login(sender, password)
        msg = MIMEText(f"{msg}", "html", "utf-8")

        msg["From"] = formataddr((str(Header("CodeRed", "utf-8")), sender))
        msg["To"] = 'stanislavd491@gmail.com'

        msg["Subject"] = 'CodeRed - IT team'
        server.sendmail(sender, user_from, msg.as_string())

    except Exception as e:
        print(f"{e} Check your login or password please!")
