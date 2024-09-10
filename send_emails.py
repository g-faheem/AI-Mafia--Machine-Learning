import smtplib
import getpass
from email.mime.text import MIMEText


def send_email():
    senders_address = 'faheem.h.shaikh@gmail.com'
    password = 'cbfr ijgs ppid zcdb'
    subject = 'AI Mafia - Machine Learning'
    msg = '''
    Hello Everyone,
    We are pleased to announce that we are starting a new batch of AI Mafia. Hope you will join.

    Thanks,
    Faheem Shaikh
    '''

    try:
        # Initialize server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Enable TLS encryption
        server.login(senders_address, password)  # Login to Gmail

        # Draft email
        email_msg = MIMEText(msg)
        email_msg['Subject'] = subject
        email_msg['From'] = senders_address
        email_msg['To'] = 'faheem.m.1303@gmail.com'
        recipients = ['faheem.m.1303@gmail.com']

        # Send email
        server.sendmail(senders_address, recipients, email_msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email: {e}")

    finally:
        server.quit()  # Close the connection


send_email()
