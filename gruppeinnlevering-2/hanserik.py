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
print ("for å spille spillet, må du trykke enter")
enter()

m()

#Andre beslutning
m()
print ("Uke 6: Silje og Elias har havnet i en konflikt")
m()
print ("Silje ønsker å lage en brukervennlig og innovativ løsning for portalen.")
m()
print ("Elias mener at forslaget til Silje er for kostbart og urealistisk.")
m()
print("Diskusjonen mellom dem blir stadig mer emosjonelle, og nå har begge begynt å trekke støtte fra sine nærmeste i gruppen.")
m()
m()
print ("Du har fire valg muligheter, disse er:")
m()
print ("1. Du kan ta saken opp i plenum for å skape åpenhet.")
m()
print ("2.Ta individuelle samtaler med Silje og Elias for å finne roten til årsaken.")
m()
print ("3. La HR bistå for å få en nøytral håndtering av konflikten")
m()
print ("4. Du kan ignorere konflikten og satse på at den løser seg av seg selv")
m()

#Første beslutning: valg 1
valg1 = input ("hva vil du gjøre? (1 eller 2, 3 eller 4?) Skriv tallet for valget du vil ta")
m()
m()

if valg1 == "1":