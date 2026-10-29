tillit = 0
fremdrift = 0


print("Hei! Du skal spille Erling som er en prosjektleder.")
print("Erling og teamet skal levere et prosjekt til en kunde. Du skal ta valg som påvirker prosjektet og teamet.")
print("Du starter med 0 tillit og 0 fremdrift. Målet er å få bygget opp tillit og fremdrift for å vinn spillet.")
print("Du vil få valg som påvirker tillit og fremdrift. Hvert valg vil enten øke eller redusere tillit og fremdrift.")
print("Lykke til!")
print("")
svar = input("Vil du starte spillet? (ja/nei): ")
print("")
if svar.lower() == "ja":
    print("==== Uke 6: Storming ====")
    print("Prosjektet er i uke 6 og skal være ferdig innen uke 8. Silje og Elias har hatt en diskusjon over en periode om hvilket rettning teknologivalg brukere kan gjøre.")
    print("Silje mener at Elias sitt forslag vil låse brukeropplevelsen og hindre innovasjon")
    print("Elias mener at Silje sin løsning er totalt urealistisk og vil føre til at prosjektet ikke blir ferdig i tide.")
    print("")
print("Over den siste tiden har diskusjonen mellom Silje og Elias eskalert og de har begynt å krangle foran teamet. Dette har ført til at teamet er splittet i to leire.")
print("Som prosjektleder må du ta et valg for å løse konflikten mellom Silje og Elias")
print("")
print("Hva vil du gjøre?")
print("")
print("1) Én-til-én-samtaler")
print("2) HR som nøytral mekler")
print("3) Fasilitert plenumsmøte")
print("4) Erling overstyrer")
valg = input("Velg 1-4: ")
while valg not in ["1", "2", "3", "4"]:
    valg = input("Ugyldig. Velg 1-4: ")
print("")
if valg == "1":
    tillit += 1
    scenario = "2A"
    print("Tonen blir roligere, men saken er ikke avklart.")
elif valg == "2":
    tillit += 1
    fremdrift -= 1
    scenario = "2A"
    print("HR tar over. Det er trygt, men tar tid.")
elif valg == "3":
    tillit += 2
    fremdrift -= 1
    scenario = "2B"
    print("Møtet er tøft, men teamet lager en felles kravliste.")
elif valg == "4":
    tillit -= 2
    fremdrift += 2
    scenario = "2C"
    print("Elias' løsning velges. Silje trekker seg unna.")
print("")
print("Tillit:", tillit)
print("Fremdrift:", fremdrift)
print("")
if scenario == "2A":
    print("====Uke 7- Dempet, men uløst====")
    print("Tonen er roligere, men saken er ikke avklart")
elif scenario == "2B":
    print("==== Uke 7 - Ny forståelse ====")
    print("Silje og Elias har dannet en felles kravliste")
elif scenario == "2C":
    print("===== Uke 7 - Kald front ====")
    print("Silje trekker seg unna og teamet er splittet i to leire")
print("")
print("Hamdi og Hallgeir er uenige om hvordan digitale folkemøter skal fungere.")
print("Hamdi vil ha kontrollerte folkemøter i kommunens eksisterende plattform. Hallgeir derimot ønsker å ha et åpent dialogbasert system")
print("Uenigheten er fortsatt veldig lavmælt og saklig, men du ønsker ikke å la den bli eskalert.")
print("")
print("BESLUTNING 2: Hvordan hindrer du at konflikten blusser opp?")
print("1) Felles avklaringsmøte")
print("2) Brukertest av begge løsningene")
print("3) Avvente")
print("")
valg = input("Velg 1-3: ")

while valg not in ["1", "2", "3"]:
    valg = input("Ugyldig. Velg 1-3: ")
if valg == "1":
    if scenario == "2C":
        tillit += 2
    else:
        tillit += 1
    scenario = "3A"
    print("Møtet er tøft, men teamet lager en felles kravliste.")
elif valg == "2":
    if scenario == "2B":
        tillit += 2
    else:
        tillit += 1
    fremdrift -= 1
    scenario = "3A"
    print("Brukertesten viser at begge løsningene har svakheter. Teamet lager en felles kravliste.")
elif valg == "3":
    if scenario == "2C":
        tillit -= 2
    else:
        tillit -= 1
    fremdrift += 1
    scenario = "3B"
    print("Teamet fortsetter å jobbe med sine egne løsninger. Konflikten er ikke løst, men fremdriften går fremover.")
 
print("Tillit:", tillit, " Fremdrift:", fremdrift)
print("")
if scenario == "3A":
    print("==== Uke 8 - Avklart ====")
    print("Konflikten er avklart og teamet har en felles forståelse")
elif scenario == "3B":
    print("==== Uke 8 - Eskalering ====")
    print ("Bystyret har hørt ryktene om konflikten, og teamet er på defensiven")

print("Prototypen skal fullføres denne uken. Teamet er preget av konfliktene som har vært og motivasjonen er lav")
print("Hva gjør du for å få teamet til å levere prototypen hel og fin?")
print("")
print("Beslutning 3: Hvordan motiverer du teamet?")
print("1)Relasjonsbygging")
print("2)Fokus på fremdrift")
print("3) Retrospektiv og delmål")
valg = input("Velg 1-3: ")
while valg not in ["1", "2", "3"]:
    valg = input("Ugyldig. Velg 1-3: ")

print("")
if valg == "1":
    tillit += 2
    fremdrift -= 1
    print("Teamet føler seg sett og hørt, men fremdriften går sakte")
elif valg == "2":
    if scenario == "3B":
        tillit -= 2
    else:
        tillit -= 1
    fremdrift += 2
    print("Teamet leverer prototypen, men relasjonene er fortsatt sårbare")
elif valg == "3":
    tillit += 1
    fremdrift += 1
    print("Teamet har en felles forståelse og leverer prototypen i tide")
 
print("Tillit:", tillit, " Fremdrift:", fremdrift)
print("")
if tillit >= 4 and fremdrift >= -1:
    print("Utfall: Norming")
    print ("Teamet har gjenopprattet tilliten og går videre til normingfasen.")
elif tillit <= 0 or fremdrift <= -2:
    print("Utfall: Tapt Samhold")
    print("Teamet har mistet samholdet, og prosjektet blir forsinket")
else:
    print("Utfall: Skjør balanse")
    print("Konflikten er delvis løst, men relasjonene er fortsatt sårbare")