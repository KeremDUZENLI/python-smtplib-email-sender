from rowApp import *


def ReadFile(filename):
    File = open(filename, 'r')
    Lines = File.readlines()

    liste1 = []
    liste2 = []

    for line in Lines:
        liste1.append(line.strip())
        liste2.append(line.strip())

    RowApp(liste1, liste2)
