# importiere die daten aus einer csv datei

import csv

filename = "persons.csv"

with open(filename, "w", newline="") as csvfile:
    filewriter = csv.writer(csvfile, delimiter=",")
    filewriter.writerow(["Name", "Beruf"])
    filewriter.writerow(["Peter", "Buchalter"])