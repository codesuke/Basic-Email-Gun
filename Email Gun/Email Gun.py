#Imported Libraries That Will be Used
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    #This is for setting up the SMTP server and make sure u don't fuck around this if u don't know shit 
    smtp_server = "smtp.gmail.com" #change if you using a different Email Service like Hotmail and BS
    smpt_port = 587  # For starttls change according to the Email Service this is default for Gmail as per rn

    try:
        # For Creating or Establishing a connection to the SMTP server
        server = smtplib.SMTP(smtp_server,smpt_port)
        server.starttls() # Secure the connection
        server.login(sender_email, sender_password)

        # Create the email message
        email_message = MIMEMultipart()
        email_message["From"] = sender_email
        email_message["To"] = recipient_email
        email_message["Subject"] = subject
        email_message["message"] = message
        email_message.attach(MIMEText(message, "plain"))

        #Send the email part 
        server.sendmail(sender_email, sender_password, recipient_email, email_message.as_string())
        print("Email Sent Successfully o7!!")

    except Exception as e:
        print(f"An error occurred while sending the mail: {str(e)}")
    
    finally:
        # Close the connection nigga
        server.quit()

# Example on usage
sender_email = input("xyz_email@gmail.com": )
sender_password = input("your_password": )
recipient_email = input("recipent_email@whatevermailservice.com": )

subject = input("Enter the subject: ")
message = input("Enter the message for the Email: ")     


send_email(sender_email, sender_password, recipient_email, subject, message)