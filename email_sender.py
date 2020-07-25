import smtplib
from email.message import EmailMessage

class EmailSender:
    email = EmailMessage()
    email['from'] = 'DollarHoy'
    email['to'] = ', '.join(['jeronimodeiros@gmail.com', 'de.simone.mj@gmail.com'])
    email['subject'] = 'Cotización Actual del dolar en Argentina.'
    def __init__(self, content):
        self.email.set_content(content)

    def send(self):
        # para hacer esto tuve que configurar la cuenta de google que cree
        # https://myaccount.google.com/lesssecureapps
        # Permitir el acceso de apps menos seguras: SÍ
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.login('dolar.info.message.news@gmail.com', 'Radnica01')
            smtp.send_message(self.email)

