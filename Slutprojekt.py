
# Listorna där namnen och telefonnumren kommer att sparas i programmet
namn = []
telefonnummer = []

# Hittade en Youtube video som visade hur man gjorde denna meny och tog lite inspiration från den
# Denna delen av programmet går igenom 5 olika alternativ som man kan välja mellan och sedan utföra den funktion som man valde
input("Välkommen till Registerprogrammet. Tryck ENTER för att fortsätta: \n")
def menu():
    print("[1] Lägg till en kontakt")
    print("[2] Visa alla kontakter")
    print("[3] Sök efter kontakt")
    print("[4] Ta bort kontakt")
    print("[5] Visa statistik")
    print("[6] Avsluta programmet \n")

# Definerar hur "alternativ 1" fungerar. Simple program som lägger till namn och telefonnummer i listorna
def lägg_till_kontakt():
    n = input("Ange kontaktens namn: \n")
    nummer = input("Ange kontaktens telefonnummer: \n")
    namn.append(n)
    telefonnummer.append(nummer)
    print("Kontakt tillagd!\n")

# Definerar hur "alternativ 2" fungerar, hittade denna "lösningen" på w3schools.com under avsnittet "Python Lists"
def visa_kontakter():
    print("Visa kontakter: \n")
    for namn_och_nummer in range(len(namn)): # går igenom alla namn i listan och skriver ut det tillsammans med det telefonnummer som hör ihop
        print(f"{namn[namn_och_nummer]} - {telefonnummer[namn_och_nummer]} \n") # namn_och_nummer = skriver ut namnet och telefonnumret som hör ihop

# Definerat hur "alternativ 3" fungerar. Söker efter namn inom listan, stödjer delvis matchning
def sök_efter_kontakt():
    sök_kontakt = input("Sök efter kontakt personen: \n").lower()
    hittade = False                                  # antar att ingen kontakt finns från början, kommer crasha om den inte är med
    for inventroy in range(len(namn)):               # loopar igenom alla namn i listan
        if sök_kontakt in namn[inventroy].lower():   # kollar om sökordet finns inuti namnet
            print(f"{namn[inventroy]} - {telefonnummer[inventroy]} \n")
            hittade = True                           # felmeddelandet visas inte, så den behöver inte köra "if not hittade"
    if not hittade:
        print("Kontakten finns inte i listan.\n")

# Definerat hur "alternativ 4" fungerar. Tar bort kontakten från listorna som man skriver in
def ta_bort_kontakt():
    ta_bort = input("Vilken kontakt vill du ta bort? \n")
    if ta_bort in namn:
        borta = namn.index(ta_bort) # letar efter indexet som hör ihop med det sökta namnet
        print(f"{namn[borta]} - {telefonnummer[borta]}, blev borttagna \n")
        namn.pop(borta) # ta bort namnet
        telefonnummer.pop(borta) # ta bort telefonnumret som hör ihop med namnet
    else:
        print("Denna kontakt finns inte eller kunnde inte bli borttagen.\n")

# Definerat hur "alternativ 5" fungerar. Visar statistik om kontakterna i listan
def visa_statistik():
    
    # Räknar ut genomsnittet namn längd
    total = 0
    for n in namn:                  # går igenom varje namn
        total = total + len(n)      # lägger till längden på varje namn
    genomsnitt = total / len(namn)
    print(f"Genomsnittlig längd på namn: {genomsnitt:.1f} tecken \n")

    # Hittar det längsta namnet
    längsta = namn[0]               # börjar med första namnet
    for n in namn:                  # går igenom varje namn
        if len(n) > len(längsta):   # säger vilken namn som är längre
            längsta = n             # nyaste längsta namn
    print(f"Längsta namnet är: {längsta} \n")

# Denna kod delen låter en välja mellan de 6 olika alternativ ovan och sedan utföra den processen + fel medelande om man använder sig av bokstäver eller siffor utanför 1-6
while True:
    menu()
    try:
        alternativ = int(input("Välj ett alternativ:\n"))

    except ValueError:
        print("\nVänligen ange ett giltigt nummer.\n")
        continue

# Här är de 5 olika alternativen som kan väljas, de är kopplade till funktionerna som är definerade ovan
    if alternativ == 1:
        lägg_till_kontakt()

    elif alternativ == 2:
        visa_kontakter()

    elif alternativ == 3:
        sök_efter_kontakt()

    elif alternativ == 4:
        ta_bort_kontakt()

    elif alternativ == 5:
        visa_statistik()

    elif alternativ == 6:
        print("Du valde att avsluta programmet. Tack för att du använde det\n")
        break
    else:
        print("Vänligen välj ett giltigt alternativ mellan 1-6.\n")


# Testning:

#Test 1: Lägga till en kontakt
# Steg: Välj alternativ 1, ange namn och nummer
# Resultat: kontakten blev tillagd i listorna

# Test 2: Visa alla kontakter
# Steg: Lägg till två kontakter, välj sedan alternativ 2
# Resultat: Båda kontakterna skrivs ut med namn och nummer

# Test 3: Söka efter en kontakt som finns
# Steg: Lägg till "Lukas", välj alternativ 3, sök på "Lukas"
# Resultat: "Lukas - 123-456789" skrivs ut

# Test 4: Söka efter en kontakt som inte finns
# Steg: Välj alternativ 3, sök på "Erik"
# Resultat: "Kontakten finns inte i listan."

# Test 5: Ta bort en kontakt
# Steg: Välj alternativ 4, skriv in "Lukas"
# Resultat: "Lukas - 123-456789, blev borttagen"

# Kort dokumentation:

# Jag har gjort ett registerprogram som har 6 olika funktioner:
# "Lägg till en kontakt"
# "Visa alla kontakter"
# "Sök efter kontakt"
# "Ta bort kontakt"
# "Visa statistik"
# "Avsluta programmet"
# Dessa fem olika funktionerna gör som namnet säger att dem gör. Informationen man skriver in blir sparande i list [namn] och [telefonnummer]

# Reflektioner:

# Programmet fungerar väll. Har lyckats få "delvis matching" att fungera när man söker efter ett namn, men lycakdes med hel machning. Men utöver det så gick detmesta bra. Fick ta lite hjälp fårn w3schools när jag skulle lista ut hur man går igenom alla namn i en lista samt hur man gör en meny

# Etik och integritet:

# Programmet sparar namn och telefonnummer i RAM-minnet (datorns arbetsminne), alltså inget sparas på din dator eller hårddisk

# I nuläget uppstår inga GDPR-problem eftersom all data bara finns i minnet