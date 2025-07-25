import csv
from presentatie import *
from helper import *

inkomsten = {
    "Aardbeien-ijs-totaal" : 1000,
    "Vanille-ijs=totaal" : 2000,
    "Chocolade-ijs-totaal" : 1500,
    "Waterijsjes-totaal" : 750
}
 
totaal_inkomsten = som(inkomsten)

for k, v in inkomsten.items():
        print(f"{k} : {v} euro")

totaal = som(inkomsten)

regels = onderstreep("totaal : " + str(totaal) + " euro")
print(regels[1])
print(regels[0])

with open('boekhouding.csv', 'w',newline='') as csvfile:
    for key,value in inkomsten.items():
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow([key,value])


