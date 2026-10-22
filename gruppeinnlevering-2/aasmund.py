##Defs som gjør ting litt enklere
#Mellomrom def
def M ():
 print ("")

#Poeng def 
def Poeng ():
    print ("Tillit:", Tillit)
    print ("Fremdrift:", Fremdrift)

#Avslutt spillet def
def Avslutt ():
    print ("Ugyldig svar, spillet avsluttes.")
    M()
    M()
    print ("Om du ønsker å starte spillet på nytt, vennligst start programmet på nytt.")
    raise SystemExit   

#Trykk enter for forsettelse
def enter (): 
   input () 

#Sum av Tillit og Fremdrift
def tf ():
   return (Tillit + Fremdrift)

##Poengsystem fra begynnelsen av: 
Tillit = 50
Fremdrift = 50



# Introduksjon til historie
M()
M()
print("Du er Erling, prosjektleder for kommunens nye medborgerportal.")
print("Det har gått seks uker, og samarbeidet møter utfordringer.")
print("Prototypen skal være klar om tre uker.")
print("Valgene dine vil påvirke tilliten og fremdriften i gruppen.")
M()
M()
print("Du får poeng for hvert valg du tar, i slutten av spillet vil din poengsum avgjøre hvordan proisjektet går videre.")
M()
M()



#Start besluttning 1:
print("Trykk enter for å starte spillet.")
enter()



#Besluttning 1 (Beskrivelse)
M()
M()
print("--Veke 6--")
print("Konflikten mellom Silje og Elias")
print("Silje ønsker en brukervennlig og innovativ løsning for portalen.")
print("Elias mener forslaget hennes er for kostbart og usikkert.")
print("Det som startet som faglig uenighet, har blitt en personlig konflikt.")
print("Diskusjonene blir stadig mer følelsesladde, og begge søker støtte hos andre i teamet.")
print("Som prosjektleder må du velge hvordan du vil håndtere situasjonen.")
M()
M()
print("Du får 4 forskjellige besluttninger")
M() 
M()
print("1: Ha en-til-en-samtaler med Silje og Elias.")
print("2: Be HR om å hjelpe som nøytral mekler.")
print("3: Ta opp konflikten i et felles plenumsmøte.")
print("4: Overstyre diskusjonen og bestemme løsningen selv.")
M() 
M()



#Besluttnings 1 (Valg)
valg_1 = input("Hva vil du gjøre? Skriv inn tallet du mener er riktig: ")

M()
M()

if valg_1 == "1":
    print("Du velger å ha en en-til-en-samtale med Silje og Elias")
    print("Dette hjelper med å forstå hverandres perspektiver og finne en løsning som er god for begge parter.")
    print("Samtidig blir konflikten løst på en rask måte som gjør at prosjektet kan forsette")
    Tillit += 20
    Fremdrift += 15
elif valg_1 == "2":
    print ("Du ber HR om å hjelpe som ernøytral hjelper")
    print ("Dette løser konflikten på en profesjonell måte, men tar for lang tid og forsinker prosjektet")
    Tillit += 10
    Fremdrift -= 10
elif valg_1 =="3":
    print("Du tar opp konflikten i et felles plenumsmøte")
    print("Dette gir alle i prosjektet til å si sin mening, men fører til eskalering av konflikten hvor diskusjonene ikke blir løst på en strukturert måte")
    print("Dette fører til at prosjektet blir forsinket og tilliten i gruppen synker")
    Tillit -= 15
    Fremdrift -= 20
elif valg_1 == "4" :
   print("Du velger å overstyre diskusjonene og bestemme løsningen selv")
   print("Dette fører til at Silje og Elias føler at deres meninger ikke blir hørt, dermed synker tilliten i gruppen, men prosjektets fremdrift blir midlertidig oprettholdt")
   Tillit -= 25 
   Fremdrift += 10

else :   
   Avslutt()


M()
M()
M()
M()


#Beslutning 2 (Start)
print("Trykk enter for å forsette.")
enter()


#Beslutning 2 (Beskrivelse)
M()
M()
print("--Uke 7--")
print("Uenigheten mellom Hamdi og Hallgeir")
print("Hamdi ønsker digitale folkemøter på kommunens eksisterende plattform.")
print("Hallgeir ønsker et åpent system med rom for spontane innspill.")
print("Uenigheten er foreløpig lavmælt, men frustrasjonen vokser.")
print("Det er nå to uker til prototypen skal være klar.")
print("Som prosjektleder må du velge hvordan du vil håndtere situasjonen.")
M()
M()
print("Du får 3 forskjellige alternativer")
M()
M()
print("1: Arrangere et felles avklaringsmøte.")
print("2: Gjennomføre en brukertest av begge løsningene.")
print("3: Avvente og la partene forsøke å finne en løsning selv.")
M()
M()



#Besluttnings 2 (Valg)
valg_2 = input("Hva vil du gjøre? Skriv inn tallet du mener er riktig: ")

M()
M()

if valg_2 == "1": 
    print("Du velger å arrangere et felles avklaringsmøte")
    print("Dette gir mulighet for at alle i prosjektet kan si sin mening om saken, men fører til eskalering av konflikten hvor diskusjonene ikke blir løst på en strukturert måte")
    print("Dette fører til at prosjektet blir forsinket og tilliten i gruppen synker")
    Tillit -= 10
    Fremdrift -= 10 
elif valg_2 == "2":
    print("Du velger å gjennomføre en brukertest av begge løsningene")
    print("Dette gir alle i prosjektet til å si sin mening, dette gir innsikt i hva som fungerer best for brukerene, tar litt tid, men gir en god sluttløsning")
    print("Dette fører til at prosjektet detta tar noe tid, men samtidig øker tilliten og fremdriften i gruppen når løsningen blir valgt basert på fakta og ikke personlige meninger")
    Tillit += 15
    Fremdrift += 10 
elif valg_2 == "3" :    
    print("Du velger å avvente og la partene forsøke å finne en løsning selv")
    print("Dette gir partene mulighet til å løse konflikten selv, men det er en risiko for at konflikten eskalerer og prosjektet blir forsinket")
    Tillit -= 10
    Fremdrift -= 15
else :
   Avslutt()


M()
M()
M()
M()


#Beslutning 3 (Start) 

print("Bra jobba! Du er nå ved siste beslutningspunkt! Trykk enter for å forsette.")
enter ()


#Beslutning 3 (Beskrivelse) 
M()
M()
print("--Uke 8--")
print("Denne delen handler om motivasjon og samarbeid i gruppen")
print("Det er én uke til prototypen skal være klar.")
print("Konfliktene har påvirket samarbeidet og motivasjonen i gruppen.")
print("Samtidig gjenstår det viktige oppgaver før prototypen er ferdig.")
print("Som prosjektleder må du velge hvordan gruppen skal bruke tiden som er igjen.")
M()
M()
print("Du får 3 forskjellige alternativer")
M()
M()
print("1: Prioritere relasjonsbygging gjennom samtaler og en felles aktivitet.")
print("2: Prioritere fremdrift og arbeidet med prototypen.")
print("3: Evaluere samarbeidet og sette tydelige delmål.")
M()
M()

#Beslutning 3 (Valg) 

valg_3 = input ("Hva vil du gjøre? Skriv inn tallet du mener er riktig: ")

if valg_3 == "1" :
    print("Du velger å prioritere relasjonsbygging gjennom samtaler og en felles aktivitet.")
    print("Dette gir gruppen bedre relasjoner og økt motivasjon for å samarbeide, det tar tid i begynnelsen. Men gjør slik at gruppen får gjennomført prototypen til slutt")
    print("Samtidig gir dette bedre tillit til videre arbeid i prosjektet")
    Tillit += 20
    Fremdrift += 10
elif valg_3 == "2" :
   print("Du velger å prioritere fremdrift og arbeidet med prototypen.")
   print("Dette gir gruppen god motivasjon og økt fremdrift i begynnelsen men dabber av mot slutten")
   print("Dette resulterer i at tilliten svkkes, samtidig er det er spørsmålet om kvaliteten på prototypen holder")
   Tillit -= 15
   Fremdrift += 0
elif valg_3 == "3" :
   print("Du velger å prioritere evaluering av samarbeidet og deretter sette opp delmål")
   print("Prosessen tar litt lang tid, men når teamet endelig har blitt enige om tydelige delmål og fordeler oppgavene, ser målet om å bli ferdig med prototypen innen friwsten lovende ut")
   print("Samtidig blir tilliten styrket med at alle medlemmer har vært med underveis å vurdert hvordan det skulle gjennomføres")
   Tillit += 20
   Fremdrift += 25
else :
   Avslutt()



##Avsluttning (Sum av poeng)
M()
M()
M()
M()

print ("Gratulerer du er ferdig med spillet, ønsker du å se ditt resultat? Trykk enter.")
enter ()

M()
M()

total = tf()

if total < 80:
    print("TAPT SAMHOLD OG FORSINKELSE")
    M()
    M()
    print(" Du har nådd lavest rangering i spillet!")
    M()
    M()
    print("Utfordringene har blitt for store, og gruppen mister samhold.")
    print("Uavklarte konflikter gjør det vanskelig å samarbeide om oppgavene.")
    print("Prototypen blir forsinket, og Erling må gjenoppbygge tilliten")
    print("og avklare hvordan gruppen skal arbeide videre.")



elif total <= 120:
    print("SKJØR BALANSE")
    M()
    M()
    print("Bra jobba! Du har nådd middels rangering i spillet!")
    M()
    M()
    print("Teamet har kommet videre, men konfliktene er bare delvis håndtert.")
    print("Samarbeidet er fortsatt sårbart, og nye uenigheter kan skape problemer.")
    print("Prototypen ble lever til slutt, men om leveransen var god nok er usikkert.")
    print("Teamet har liten eierfølelse til det ferdigstillte produktet, og motivasjonen er lav for prosjektet videre.")





else:
    print("NORMING")
    M()
    M()
    print("Gratullerer du har nådd høyeste rangering i spillet!")
    M()
    M()
    print("Teamet har funnet en bedre måte å samarbeide på.")
    print("Medlemmene viser større respekt for hverandres perspektiver")
    print("og har tydeligere forventninger til ansvar og arbeidsfordeling.")
    print("Uenigheter finnes fortsatt, men håndteres mer saklig.")
    print("Teamet beveger seg mot norming, og fikk ferdigstillt prototypen til tilstrekkelig tid.")
    print("Den ferdigtillte protoypen ser også ut til å gi en eierfølelse fra alle medlemmer fra teamet, med sammensatt")
    print("kompetanse fra de forskjellige fag-feltene. Motivasjonen er medvarende videre til de neste fasene av prosjektet har å gi.")



