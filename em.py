#!/usr/bin/python3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, message, to_email, sender_email, sender_password):
    try:
        # Create an instance of MIMEMultipart
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the message to the email
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)

        # Send the email
        smtp_server.sendmail(sender_email, to_email, msg.as_string())

        # Close the SMTP server connection
        smtp_server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print("Error sending email:", str(e))

if __name__ == '__main__':
    # Input email details
    sender_email = "vsonya214@gmail.com"
    sender_password = "dzio mhtk xhky gajg"
    to_email = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")

    message = input("Enter the message text: ")

    send_email(subject, message, to_email, sender_email, sender_password)
