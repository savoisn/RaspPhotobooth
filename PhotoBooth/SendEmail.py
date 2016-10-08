# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def sendMail(stream, email_adress):
# Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['Subject'] = 'Photo from Raspberry'
# me == the sender's email address
# family = the list of all recipients' email addresses
    msg['From'] = 'nicolas.savois@free.fr'
    msg['To'] = email_adress
    msg.preamble = 'Photo from Raspberry'

    if stream :
        stream.seek(0)
        img = MIMEImage(stream.read())
        msg.attach(img)

# Send the email via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

