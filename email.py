import csv
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
import time


sender_email = "your_email@mail.com"
csv_file = "your/file/path"
password = "Your Google App Password"
email_body_file = 'file/path/to/emailbody.txt'

with open(email_body_file, "r") as body_file:
    email_body = body_file.read()
    
    
def get_recipient_emails(csv_file):
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row['email'] for row in reader]

def send_email():
    subject = "Subject of the email"
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = ", ".join(get_recipient_emails(csv_file))  
    message["Subject"] = subject
    message.attach(MIMEText(email_body, "plain"))


    file_path = "file/path/to/recipientsemail.csv"
    with open(file_path, "rb") as attachment:
        part = MIMEApplication(attachment.read(), Name="file.txt")
        part['Content-Disposition'] = 'ClassList.csv'
        message.attach(part)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)


        server.sendmail(sender_email, message["To"], message.as_string())  

    print("Email sent successfully!")



scheduled_time = datetime.datetime(2024, 1, 27, 7, 0) 


while datetime.datetime.now() < scheduled_time:
    time.sleep(1)

send_email()
