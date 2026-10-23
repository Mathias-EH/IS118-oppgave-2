##Defs gjør at koden blir lettere å lese 
#mellomrom def
from ast import Return


def m ():
    print ("")


#poeng def
def p ():
    print ("Teamets tillit" , Teamtillit)
    print ("Prosjektets Fremdrift:" , Prosjektfremdrift)

    #Spillets avslutning def
    def avsluttning ():
        print ("Svaret er ugyldig. Spillet avsluttes ")
        m()    
        print ("Du kan spille på nytt ved å trykke enter")
        raise (SystemExit)

#def trykk enter for å fortsette spillet
def enter ():
    input ()

#Sum av poeng
def sum ():
    Return (Teamtillit+Prosjektfremdrift)

#poengsum ved begynnelse av spill
Teamtillit = 40
Prosjektfremdrift = 40

##Introduksjont til spillets historie
m()
m()
print ("Du er prosjektleder Erling, og har ansvar for kommunens nye prosjekt som går ut på å lage en ny medborger portal.")
m()
print ("Seks uker har passert, og samarbeidet i teamet har møtt på en del utfordringer.")
m()
print ("Teamet har tre uker igjen på å ferdigstille prototypen")
m()
print ("Erlings valg vil påvirke både teamets tillit og prosjektets fremgang")
m()
m()
m()

#Første beslutning
print ("for å spille spiller, må du trykke enter")

#Andre beslutning
m()
print ("Uke 6: Silje og Elias har havnet i en konflikt")
m()
print ("Silje ønsker å lage en brukervennlig og innovativ løsning for portalen")