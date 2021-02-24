import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Reiner Krieg'
email['to'] = 'email'
email['subject'] = 'Is this working now?'

email.set_content('I am a Python Master!!!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
    print('All good boss!')
