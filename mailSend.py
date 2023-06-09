import smtplib


EMailOwner = input("Enter your E-Mail: ")
EMailOwnerPassword = input("Enter your E-Mail App-Specified Password: ")


def MailSend(sender, receiver):
    # Set the server and port
    server = smtplib.SMTP('smtp.gmail.com', 587)

    # Start the server connection
    server.starttls()

    # Login to the server using your email and password
    server.login(EMailOwner, EMailOwnerPassword)

    # Set the recipient and subject of the email
    subject = "Amigo/Amiga Secredo"

    # Create the body of the message
    body = f"Sender: {sender} >> Receiver: {receiver}"

    # Format the message as an email
    msg = f"Subject: {subject}\n\n{body}"

    # Send the email
    server.sendmail(EMailOwner, sender, msg)

    # Close the server connection
    server.quit()
