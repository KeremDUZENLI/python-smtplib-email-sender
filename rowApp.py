import random
from mailSend import *


def RowApp(liste1, liste2):
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

    else:
        print(f"Sender: {liste1[0]} >> Receiver: {liste2[0]}")
        MailSend(liste1[0], liste2[0])
