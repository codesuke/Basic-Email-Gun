import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

def send_email():
    sender_email = sender_entry.get()
    sender_password = password_entry.get()
    receiver_email = receiver_entry.get()
    subject = subject_entry.get()
    message = message_text.get("1.0", "end-1c")

    if not (sender_email and sender_password and receiver_email and subject and message):
        messagebox.showwarning("Warning", "Please fill in all the fields.")
        return

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add body to email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create a secure SSL/TLS connection to the email server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        # Login to the email server
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())

        # Close the connection
        server.quit()

        messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while sending the email:\n{str(e)}")

# Create the GUI window
window = tk.Tk()
window.title("Email Sender")

# Create labels and entries for sender's email
sender_label = tk.Label(window, text="Sender's Email:")
sender_label.pack()
sender_entry = tk.Entry(window)
sender_entry.pack()

# Create labels and entries for sender's password
password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create labels and entries for receiver's email
receiver_label = tk.Label(window, text="Receiver's Email:")
receiver_label.pack()
receiver_entry = tk.Entry(window)
receiver_entry.pack()

# Create labels and entries for email subject
subject_label = tk.Label(window, text="Subject:")
subject_label.pack()
subject_entry = tk.Entry(window)
subject_entry.pack()

# Create label and text box for email message
message_label = tk.Label(window, text="Message:")
message_label.pack()
message_text = tk.Text(window, height=10, width=30)
message_text.pack()

# Create send button
send_button = tk.Button(window, text="Email Send Kro", command=send_email)
send_button.pack()

# Start the GUI event loop
window.mainloop()
