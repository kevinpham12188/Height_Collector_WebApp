import smtplib
from email.mine.text import MINEText


def send_email(email, height, average_height, count):
    from_email = 'aaa@gmail.com'
    from_password = "aaatest"
    to_email = email

    subject = "height data"
    message = " Hey there, your height is <strong>%s</strong>. Average height of all is <strong>%</strong>" \
              "and that is calculated out <strong>%</strong> of people" % (height, average_height, count)

    msg = MINEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 578)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
