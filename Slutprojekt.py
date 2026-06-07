
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
    print("[5] Avsluta programmet \n")

# Definerar hur "alternativ 1" fungerar
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

#def sök_efter_kontakt():

#def ta_bort_kontakt():

# Denna kod delen låter en välja mellan de 5 olika alternativ ovan och sedan utföra den processen + fel medelande om man använder sig av bokstäver eller siffor utanför 1-5
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
#        sök_efter_kontakt()
        pass


    elif alternativ == 4:
#        ta_bort_kontakt()
        pass

    elif alternativ == 5:
        print("Du valde att avsluta programmet. Tack för att du använde det\n")
        break
    else:
        print("Vänligen välj ett giltigt alternativ mellan 1-5.\n")
