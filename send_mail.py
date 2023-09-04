from email.mime.application import MIMEApplication
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from dotenv import load_dotenv
import os
load_dotenv()
smtp_username = os.environ['EMAIL_ID']
smtp_password = os.environ['PASSWORD']

def send_mail(name="Cosmonauts",receiver_email="dassamratkumar772@gmail.com"):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587 
    sender_email = smtp_username
    subject = 'Test Email'
    html = f'''
    <html>
        <body>
            <h1>Congratulations You have selected!!!</h1>
            <p>Congratulations again for being selected {name} <br>
                We expected you know about the necessary details and information about this event.<br>
                If not we attaching the necessary files again with the mail.
            </p>
            <p>
                We also attaching your unique barcode id with the mail. Save it carefully, It will be needed during the entry on the event.
            </p>
            <p>
                So,see you soon buddy lets rock on the event!!!
            </p>
        <body>
    <html>
    '''
    def attach_file_to_email(email_message, filename):
        with open(filename, "rb") as f:
            file_attachment = MIMEApplication(f.read())
        file_attachment.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        email_message.attach(file_attachment)
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(html, 'html'))
    file=os.path.join('barcode.jpg')
    attach_file_to_email(msg,file)
    msg_str=msg.as_string()

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(smtp_username, smtp_password)
            server.sendmail(sender_email,receiver_email,msg_str)
            print(f'Email sent successfully to : {receiver_email}')
    except Exception as e:
        print(f"There is an error when we trying to send email to {receiver_email}")
        pass
