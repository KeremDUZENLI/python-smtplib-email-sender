import random
import smtplib


EMailOwner = input("Enter your E-Mail: ")
EMailOwnerPassword = input("Enter your E-Mail App-Specified Password: ")


####################     E-MAIL     ####################
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


####################     ALGORITHM     ####################
file1 = open('names_email.txt', 'r')
Lines = file1.readlines()

count = 0

liste1 = []
liste2 = []

for line in Lines:
    count += 1
    liste1.append(line.strip())
    liste2.append(line.strip())


limit = len(liste1) - 1


while len(liste1) > 1:
    randomNumber1 = random.randint(0, limit)
    randomNumber2 = random.randint(0, limit)

    while True:
        if randomNumber1 == randomNumber2:
            randomNumber2 = random.randint(0, limit)
        else:
            break

    print(
        f"Sender: {liste1[randomNumber1]} >> Receiver: {liste2[randomNumber2]}"
    )

    GiftSender = liste1[randomNumber1]
    GiftReceiver = liste2[randomNumber2]
    MailSend(GiftSender, GiftReceiver)

    liste1.remove(liste1[randomNumber1])

    liste2.remove(liste2[randomNumber2])

    limit -= 1


print(f"Sender: {liste1[0]} >> Receiver: {liste2[0]}")
MailSend(liste1[0], liste2[0])
