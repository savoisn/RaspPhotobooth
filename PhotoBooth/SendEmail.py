# Import smtplib for the actual sending function
import smtplib
import hug

# Import the email modules we'll need
from email.mime.text import MIMEText

@hug.cli()
def sendMail():
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
    # Create a text/plain message
    msg = MIMEText("Coucouc de nico")

# me == the sender's email address
# you == the recipient's email address
    msg['Subject'] = 'The contents of mon test'
    msg['From'] = 'nicolassavois@yahoo.fr'
    msg['To'] = 'nicolas.savois@gmail.com'

# Send the message via our own SMTP server.
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

if __name__ == '__main__':
    sendMail.interface.cli()
