import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Jagadees.as07@gmail.com'
email['to'] = 'Jagadees.as07@gmail.com'
email['subject'] = 'You loser'
email.set_content('You are dumb ass')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as s:
    s.ehlo()
    s.starttls()
    s.login('Jagadees.as07@gmail.com', 'Jaggu@5512')
    s.send_message(email)
    print('You maniac')


