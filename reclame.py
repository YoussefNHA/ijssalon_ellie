from algemene_functies import mijn_functie_2

def aanbieding_1(smaak, prijs, korting):
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {prijs - (prijs * korting)} euro."
    return uitvoer
print(aanbieding_1("aardbei", 4, 0.1))

def inkomsten_totaal(inkomsten, btw):
    inkomsten = sum(inkomsten)
    bedrag = inkomsten * (btw/100)
    teruggeefwaarde3 = f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {bedrag} euro btw betaald dient te worden."
    return teruggeefwaarde3
print(inkomsten_totaal((220, 430, 125, 160, 205, 90, 345), 9))

def laag_en_hoog(mijn_lijst):
    mijn_lijst = max(mijn_lijst), min(mijn_lijst)
    return mijn_lijst
print(laag_en_hoog([220, 430, 125, 160, 205, 90, 345]))

def gemiddelde(mijn_lijst):
    mijn_lijst = sum(mijn_lijst)/len(mijn_lijst)
    teruggeefwaarde4 = f"De gemiddelde inkomsten deze week zijn {mijn_lijst} euro."
    return teruggeefwaarde4
print(gemiddelde([220, 430, 125, 160, 205, 90, 345]))

def meervoudig(invoer_lijst):
    invoer_lijst = laag_en_hoog(invoer_lijst)
    return invoer_lijst
print(meervoudig([10, 5, 3, 2, 1, 2, 9]))

def combinatie(invoer_lijst2):
    korte_lijst = laag_en_hoog(invoer_lijst2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer