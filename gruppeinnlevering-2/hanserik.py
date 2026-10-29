##Defs gjør at koden blir lettere å lese 
from ast import Return

#Mellomrom def: Definerer mellomrom med bruk av m-(), da printes det en tekslinje uten tekst, da for å lage et mellomrom 
def m ():
    print ("")


#poeng def: definerer hva som er poeng
def p ():
    print ("Teamets tillit:", Teamtillit)
    print ("Prosjektets Fremdrift:", Prosjektfremdrift)
    
    m()

#Avslutt spillet def: definerer om spillet avslutter ut fra om noe annet enn forventet svar kommer inn
def avslutt ():
    print ("Svaret var ugyldig, spillet avsluttes.")
    m()
    print ("om du øsnker å spille på nytt, vennligst start konsollen på nytt")
    raise SystemExit

#def trykk enter for å fortsette spillet: definerer at man må trykke enter for å fortsette spillet ved varsel om trykk enter.
def enter ():
    input ()

#Sum av poeng
def sum ():
    return (Teamtillit+Prosjektfremdrift)

#poengsum ved begynnelse av spill: antall poeng du har ved begynnelsen
Teamtillit = 40
Prosjektfremdrift = 40

##Introduksjonen til spillets historie
m()
m()
print (" Du er prosjektleder Erling, og har ansvar for kommunens nye prosjekt som går ut på å lage en ny medborger portal.")
m()
print (" Seks uker har passert, og samarbeidet i teamet har møtt på en del utfordringer.")
m()
print (" Teamet har tre uker igjen på å ferdigstille prototypen")
m()
print (" Erlings valg vil påvirke både teamets tillit og prosjektets fremgang")
m()
m()
m()

#Første beslutning
print ("for å spille spillet, må du trykke enter")
enter()

m()

#Andre beslutning
m()
print (" Uke 6: Silje og Elias har havnet i en konflikt")
m()
print (" Silje ønsker å lage en brukervennlig og innovativ løsning for portalen.")
m()
print (" Elias mener at forslaget til Silje er for kostbart og urealistisk.")
m()
print(" Diskusjonen mellom dem blir stadig mer emosjonelle, og nå har begge begynt å trekke støtte fra sine nærmeste i gruppen.")
m()
m()

#Beskrivelse av beslutninger du kan ta

print (" Du har fire valg muligheter, disse er:")
m()
print ("1. Du kan ta saken opp i plenum for å skape åpenhet.")
m()
print ("2. Ta individuelle samtaler med Silje og Elias for å finne roten til årsaken.")
m()
print ("3. La HR bistå for å få en nøytral håndtering av konflikten")
m()
print ("4. Du kan ignorere konflikten og satse på at den løser seg av seg selv")

m()
m()

#Andre beslutning: valg 1
valg1 = input (" Hva vil du gjøre? (1 eller 2, 3 eller 4?) Skriv tallet som representerer valget du ønsker å ta: ")

m()
m()

if valg1 == "1":
    print (" Du velger å ta saken opp i plenum for å skape åpenhet mellom partene.")
    print (" Flere i teamet gir sine perspektiver, men diskusjonen blir raskt preget av sterke meninger og følelser")
    print (" Teamets tillit og motivasjon synker, og prosjektets fremdrift blir satt tilbake")
    Teamtillit -= 25
    Prosjektfremdrift -= 35
    m()
elif valg1 == "2":
    print (" Du velger å ta individuelle samtaler med silje og Elias for å finne roten til årsaken.")
    print (" Samtalene går bra, og Erling får en god forståelse av hva som har skjedd. Han finner en løsning som begge partene kan akseptere.")
    print (" Teamets tillit og motivasjon øker, og prosektets fremdrift får en god boost")
    Teamtillit += 30
    Prosjektfremdrift += 30
    m()
elif valg1 == "3":
    print (" Du velger å la HR bistå for å få en nøytral håndtering av konflikten")
    print (" HR tar opp konfliketen med partene, og finner en halveis løsning som begge parter kan akseptere, men som ikke er optimal for prosjektets fremdrift")
    print (" Teamets tillit og motivasjon øker, men prosjektets fremgang forblir uendret")
    Teamtillit +=10
    Prosjektfremdrift +=0
    m()
elif valg1 == "4":
    print (" Du ignorer konflikten totalt og satser på at den løser seg av seg selv")
    print (" Dessverre eskalerer konflikten seg, og silje og elias trekker seg fra prosjektet.")
    print (" prosjektets fremdrift synker dramatisk og teamets tillit og motivasjon går i stykker")
    Teamtillit -=45
    Prosjektfremdrift -=40
else: avslutt()

m()
m()
m()

#Tredje beslutning (Start)
print (" Trykk på enter for å fortsette spillet")
enter()

#Beskrivelse av tredje beslutning
m()
print (" Uke 7: Uengihet mellom Hamdi og Hallgeir")
m()
print (" Hamdi og Hallgeir har blitt uenige om hvordan innbyggerne i kommunen skal kunne delta i de digitale folkemøtene")
m()
print (" Hamdi ønsker at de digitale folkemøtene føres gjennom en kontrollert løsning på kommunens allerede eksisternede platform")
print (" Hallgeir derimot ønsker et mer åpent og dialogbasert system, der innbyggerne kan komme med spontane innspill.")
m()
print (" Uenigheten mellom dem er foreløpig lavmælt, men frustrasjonen vokser og kommunikasjonen er dårlig. Dette kan føre til at prosjektets fremdrift blir sinket")

m()
m()

#Beskrivelse av beslutninger du kan ta

print (" Du har fire valg muligheter, disse er:")
m()
print ("1. Et felles avklarings møte med Hamdi og Hallgeir, slik at man kan finne en løsning som begge kan være enige i.")
m()
print ("2. Avvente å se om problemet fikses av seg selv.")
m()
print ("3. Gjør en brukertest av begge løsninger for å se hvilken som er best.")
m()
print ("4. Overstyr arbeidet til Hamdi og Hallgeir for og få prosjektet videre.")

m()
#Tredje beslutning (valg)
valg2 = input (" Hvilket valg vil du ta? (Velg mellom 1, 2, 3 eller 4.) ")
m()

if valg2 == "1":
    print ("Du holder et felles møte med Hamdi og Hallgeir")
    print (" Både Hamdi og Hallgeir virker positive, men fremgangen i møtet går sakte.")
    m()
    print (" Til slutt kommer dere fram til en løsning der Hamdi og Hallgeir er fornøyde.")
    print (" Tilliten og motivasjonen til teamet går opp, og fremdriften skyter i været.")
    Teamtillit +=10
    Prosjektfremdrift +=20
    m()
elif valg2 == "2":
    print ("Du avventer å ser om problemet løser seg av seg selv.")
    print (" I begynnelsen ser det ut til at ting ordner seg av seg selv, men så har Hamdi og Hallgeir fått nokk")
    print (" Spenningen mellom Hamdi og Hallgeir har eksplodert, konflikten har nå begynt å gå utover resten av prosjekt teamet.")
    m()
    print (" Teamets tillit og motivasjon har blitt nedsatt, og med dette har også prosjektets fremdrift sakket ned.")
    Teamtillit -=25
    Prosjektfremdrift -=35
    m()
elif valg2 =="3":
    print (" Det utføres en brukertest av begge løsningene.")
    print (" Et utvalg av brukere blir satt til å teste hver av løsningene.")
    print (" Når testingen er over ser Hamdi og Hallgeir at en kombinasjon av løsningene deres kan fungere godt.")
    print (" Teamets motivasjon og tillit øker, mens prosjektet får skikkelig fremdrift.")
    Teamtillit +=25
    Prosjektfremdrift +=35
    m()
elif valg2 =="4":
    print (" Du velger å overstyre arbeidet til Hamdi og Hallgeir")
    print (" Du bestemmer at Hamdi's løsning er bedre, da den ikke krever så mye arbeid som Hallgeirs løsning.")
    print (" Hamdi er delvis fornøyd med at du tar hans side, men både Hamdi og Hallgeir er sjokkert over at du har valgt og overstyre dem")
    print (" Teamet mister tillit og motivasjon senkes. Prosjektet går litt fremover.")
    Teamtillit -=15
    Prosjektfremdrift +=15
else: avslutt
m()
#Fjerde beslutning start
print ("Trykk enter for å spille videre")
enter()

#Beskrivelse av fjerde beslutning
m()
print ("Uke 8: Teamets motivasjon og moral")
print (" På grunn av konflikter og hendelser i ukene før, har teamts motivasjon og moral falt")
print (" Erling må nå finne en måte å få opp motivasjon og holde teamets moral oppe.")
m()

#Beskrivelse av beslutninger du kan ta
print ("1. Du kan gå for relasjonsbygging gjennom en sosial sammenkomst.")
print ("2. Holde et møte hvor medlemmene blir orientert om fokus på leveranse.")
print ("3. Du kan ha et møte på slutten av uken, her diskuteres hva som har gått bra, og ting som kan bli bedre med å sette delmål. ")
print ("4. Du velger å gjøre ingenting")
m()


#Fjerde beslutning (valg)
valg3 = input ("Hva velger du? (Velg mellom 1, 2, 3 eller 4.) ")
if valg3 == "1":
    print ("Du valgte å gå for relasjonsbygging")
    print ("Erling setter av tid for en sosial kveld, prosjektteamet hygger seg og stemmningen er god.")
    print (" I løpet av dagene etter sammenkomsten legger du merke til at motivasjon til teamet har steget.")
    Teamtillit +=15
    Prosjektfremdrift +=15
elif valg3 =="2":
 print (" Du kaller inn til møte for å orientere teamet om viktigheten av å holde fokuset på leveransen av prosjektet.")
 print (" Alle møter opp til møtet, første halvdel går meget bra.")
 print (" Andre halvdel av møtet begynner teamet å bli rastløse, og du merker fort at motivasjon faller mer.")
 Teamtillit -=5
 Prosjektfremdrift -=5
elif valg3 =="3":
    print (" Holde et møte på slutten av uken, slik at teamet kan diskutere hva som gikk bra eller ting som kan forbedres.")
    print (" Møtet begynner å det er mye engasjement, teamet kommer med mange ting som de synes har vært bra.")
    print (" I møtet vises det også mye engasjememt til forbedringer.")
    print (" Teamets motivasjon og tillit går opp, og prosjektets fremdrift skyter opp.")
    Teamtillit +=15
    Prosjektfremdrift +=25
elif valg3 =="4":
    print (" Du valgte ingen av delene")
    print (" Teamets motivasjon og tillit fortsetter ned, det samme gjør prosjektets framdrift.")
    print (" Skulle tatt pizzakveld med teamet!")
    Teamtillit -=20
    Prosjektfremdrift -=30
else : avslutt



#Spill credits og poengsum
m()
m()
m()
m()

print ( "Gratulerer med ett fullført spill!")
m()
print ("Om du vil se din poengsum, trykk enter!")
enter ()
m()
m()
m()

total = sum ()

if total < 40:
    print ("Tapt samhold og ingen leveranse")
    m()
    m()
    print (" Teamet gikk i oppløsning, fremdriften stoppet og leveransen av prototypen og selve produktet skjedde ikke.")
    print (" Mange konflikter forble ulføste, og motivasjon kom seg aldri opp igjen")
    print (" Noen uker etter må Erling trekke seg som prosjektleder for prosjektet.")
    m()
    m()
elif total <=80:
    print (" Hårfin balanse")
    m()
    m()
    print (" Reddet, men så vidt! Gratulerer!")
    m()
    m()
    print (" Teamet kommer seg videre men bare så vidt!")
    print (" Mange av konfliktene ble håndert, men ikke på den beste måten.")
    print (" Da tilliten og motivasjon er i en hårfin balanse, kan nye uenigheter kan dukke opp når som helst")
    print (" Det er usikkert om leveransen var av beste kvalitet, men levert ble den iallefall.")
    m()
    print (" Teamet sitter igjen med lite eierfølelse til produket de har ferdigstilt, og motivasjon fremover ligger lavt.")
else:
    print ("En super suksess, teamet går videre til NORMING!")
    m()
    m()
    m()
    print (" Du har nådd spillets høyeste poengsum, gratulerer!")
    m()
    print (" Teamets samhold og respekt for hverandre har økt.")
    print (" I tillegg har Samarbeidet blitt bedre enn det var ved start, og teamet har fått tettere bånd.")
    print (" Noe som igjen har ført til at hvert medlem er mer bevvist deres ansvar og rolle i prosjektet.")
    m()
    print (" Det er fortsatt uenigheter, men teamet har funnet bedre måter for å håndtere disse saklig.")
    print (" Dette har ført til at teamet beveger seg mot norming, og leveransen av prototypen.")
    m()
    print (" Teamet ser også ut til å ha fått en større eierfølelse til prosjektet,-")
    print (" da deres samldede kompetanse førte til at ferdigstillelse og leveranse av prototypen ble gjort")
    print (" Teamets motivasjon og tillit ser ut til å medvare i den resterende perioden av prosjektet.")
    m()
    m()
    print (" for å starte spillet på nytt, start programmet på nytt!")



