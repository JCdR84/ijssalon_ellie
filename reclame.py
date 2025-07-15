from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    prijs_na_korting = prijs * (1 - korting)
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs_na_korting} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten):
    totaal = 0
    for nr in inkomsten:
        totaal += nr
    return totaal
inkomsten = [220, 430, 125, 160, 205, 90, 345]
totaal = inkomsten_totaal(inkomsten)
btw = 0.09*totaal
print(f"Het totaal van alle inkomsten van deze week is {totaal} euro, waarover {btw} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    return [min(mijn_lijst), max(mijn_lijst)]

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
uitvoer = laag_en_hoog(mijn_lijst)
print(uitvoer)

def gemiddelde(mijn_lijst):
    return totaal/len(mijn_lijst)

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
uitvoer = gemiddelde(mijn_lijst)
print(f"De gemiddelde inkomsten van deze week zijn {uitvoer} euro.")

def meervoudig(invoer_lijst):
    return laag_en_hoog(mijn_lijst_2)

mijn_lijst_2 =  [19, 3, 8, 5, 7, 4, 12, 17]
uitvoer = (laag_en_hoog(mijn_lijst_2))
print(uitvoer)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
return uitvoer