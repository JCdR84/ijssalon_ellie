from helper import onderstreep
from helper import som

def presenteer():
    inkomsten = {
    "vis" : 10, 
    "vlees" : 25, 
    "overig" : 15
    }
    
    totaal = som(inkomsten)
    for k, v in inkomsten.items():
        print(f"{k} : {v} euro")

    regels = onderstreep("totaal : " + str(totaal) + "euro")
    print(regels[1])

    print(f"totaal : {totaal}  euro")

