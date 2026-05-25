print("Jag vill att du väljer 7 heltal mellan 1 och 50 och sedan skriver dem till mig")
print("Skriv in dina 7 heltal, skriv bara ett tal i taget: ")

# lista där alla talen sparas och sedan blir dom kallade igen när man har skrivit klart sinna 7 heltal
antal_tal = []

# Loopar igenom denna 7 gånger och ser till att man inte använder bokstäver, siffror utanför 1 och 50 eller att man använder samma tal 2 gånger
for number in range(7):
    while True:
        try:
            # Lägger på +1 number varje gång tills man kommer till 7 och sedan körs print funktionen längs ned
            siffra = input(f"Nummer {number + 1} av 7: ")
            antal = int(siffra)
            if 1 <= antal <= 50: # Accepterar bara siffror mellan 1 och 50

                # Denna del hanterar så att man inte skriver samma tal 2 gånger
                if antal in antal_tal: # om den ser att siffran redan finns i listand kommer den neka ditt svar
                    print("Du har redan valt det talet, välj ett annat")
                else:
                    antal_tal.append(antal) # append lägger till de nya talen i slutet av listan "antal_tal"
                    break
            else:
                print("Fel, ange ett heltal mellan 1 och 50")

        except ValueError:
            print("Fel, du får inte använda bokstäver använd dig av siffror mellan 1 och 50")

print(f"Dina heltal du valde: {antal_tal}")

# Den kan hantera felmedelanden som felaktiga siffror, bokstäver och samma siffror 2 gånger
# Det var väldigt svårt att göra detta, just att få uträkningen att fungera. Jag använde mig av w3 school och stackoverflow för att hitta lösningar och inspiration på hur man kunde göra och tänka