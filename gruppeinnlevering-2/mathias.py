
tillit = 0
fremdrift = 0
print("\nDet har gått seks uker siden prosjektleder Erling startet utviklingen av kommunens nye digitale medborgerportal. I starten var samarbeidet bra med høy motivasjon og fellesskap men nå etter seks uker har det blitt dårlig.\n\nProsjektet har gått inn i den klassiske storming-fasen der ulike faglige perspektiver og personlige preferanser begynner å kollidere. Silje og Elias er uenige om teknologi valg og design, og uenigheten har gradvis utviklet seg til en personkonflikt.\n")
Beslutning1 = input("1. En til en samtaler \n2. HR som nøytral mekler \n3. Fasilitert plenumsmøte \n4. Erling overstyrer \n")

if Beslutning1 == "1": # EN TIL EN
    tillit += 2
    fremdrift += 0
    utfall = ("1A")
elif Beslutning1 == "2": # HR MEKLERING
    tillit += 1
    fremdrift -= 1
    utfall = ("1A")
elif Beslutning1 == "3": # PRENIUM MØTE
    tillit -= 1
    fremdrift -= 1
    utfall = ("1B")
elif Beslutning1 == "4": # ERLING OVERSTYRER
    tillit -= 2
    fremdrift += 2
    utfall = ("1C")
else:
    print("Ugyldig valg. Du må skrive 1, 2, 3 eller 4.")
    Beslutning1 = input("1. En til en samtaler \n2. HR som nøytral mekler \n3. Fasilitert plenumsmøte \n4. Erling overstyrer \n")

print("\nHamdi og Hallgeir er uenige om hvordan innbyggerne skal delta i digitale folkemøter. Hva vil du gjøre?")
Beslutning2 = input("1.	Felles avklaringsmøte \n2.	Avvente \n3.	Brukertest av begge løsninger \n")

if Beslutning2 == "1": # MØTE
    tillit += 1
    fremdrift += 0
    if utfall == ("1C"):
        tillit += 2
    utfall = ("2A")
elif Beslutning2 == "2": # AVVENTE
    tillit -= 1
    fremdrift += 1
    if utfall == ("1C"):
        tillit -= 2
    utfall = ("2B")
elif Beslutning2 == "3": # BRUKERTEST
    tillit += 1
    fremdrift -= 1
    if utfall == ("1B"):
        tillit += 2
    utfall = ("2A")
else:
    print("Ugyldig valg. Du må skrive 1, 2 eller 3.")
    Beslutning2 = input("1.	Felles avklaringsmøte \n2.	Avvente \n 3.	Brukertest av begge løsninger \n")

print("\nFristen for prototypen nærmer seg, og Erling må bevare motivasjonen i teamet. Hva vil du prioritere?")
Beslutning3 = input("\n1.	Relasjonsbygging \n2.	Leveransefokus \n3.	Retrospektiv og delmål\n")

if Beslutning3 == "1": # RELASJON
    tillit += 2
    fremdrift -= 1
elif Beslutning3 == "2": # LEVERANSE
    tillit -= 1
    fremdrift += 2
    if utfall == ("2B"):
        tillit -= 2
elif Beslutning3 == "3": # RETROSPEKTIV
    tillit += 1
    fremdrift += 1
else:
    print("Ugyldig valg. Du må skrive 1, 2 eller 3.")
    Beslutning3 = input("\n1.	Relasjonsbygging \n2.	Leveransefokus \n3.	Retrospektiv og delmål\n")

totalpoeng = tillit + fremdrift

if totalpoeng >= 3:
    print("\nNorming: Teamet har fått bedre tillit til hverandre, men fremdriften har stoppet opp. Prototypen blir forsinket.")
elif totalpoeng >= 1:
    print("\nTapt samhold og forsinkelse enden er det som tilsvarer å tape spillet. Teamet til Erling er ikke fornøyd, har null tillit til Erling eller andre og progresjonen har ikke vært tilstrekkelig. Dette har ført til teamet har falt fra hverandre og en forsinkelse på levering av produktet.")
else:
    print("\nSkjør balanse: Erling har ikke gjort tilstrekkelig nok for å tilfredstille teamet eller gjort nok progresjon for å lage prototypen. Konfliktene har blitt ordnet opp i, men relasjonene har tatt seg en støyt. Erling har gjort flere ting korrekt, men Erling har i tillegg gjort feil valg gjennom spillet.")

