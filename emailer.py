import smtplib

def send_email(sender_email, sender_password, receiver_email, subject, message):
    """
    Function to send an email.

    :param sender_email: Email address of the sender.
    :param sender_password: Password of the sender's email account.
    :param receiver_email: Email address of the receiver.
    :param subject: Subject of the email.
    :param message: Message of the email.
    :return: None
    """
    msg = f'Subject: {subject}\n\n{message}'
    with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.encode('utf-8'))
