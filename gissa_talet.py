import random # Behöver "random" bilbotekt för att kunna generera ett slumpmässigt tal

print("Jag har valt ett tal mellan 1 och 200 och du ska försöka gissa på vilket tal jag tänker på. Du har 10 försök på dig!")

# random.randint är "paketet" från "import random" som genererar ett nummer mellan 1 och 200, sedan sparas resultatet i variablen "slumpmässigt_number"
# försök är variable som börjar räkna från 0 och varje gång man gissar så läggs det till 1 i variablen tills man antingen gissar rätt tall eller man får slut på gissningar.
slumpmässigt_number = random.randint(1, 200)
försök = 0

# uträkningen som används för att gör sinna gissningar. Den kör igenom en for loop och fortsätter tills man antingen gissar rätt alltså "rad 19-20" eller man får slut på gissninar "rad 22-23"
# la till error hantering när man inte gissar på en siffra
for i in range(10):
    try:
        gissa = int(input("Gissa ett tal: "))
    except ValueError:
        print("Ange ett tal, inom 1-200.")
        continue # om man skriver en bokstav så kommer loopen att fortsätta ändå
    försök +=1

    if gissa < slumpmässigt_number:
        print("För lågt! Jag tänker på ett högre tal")
    elif gissa > slumpmässigt_number:
        print("För högt! Jag tänker på ett lägre tal")
    else:
        print(f"Grattis! Du gissade rätt talet {slumpmässigt_number} på {försök} försök!")
        break
else:
    print(f"Du lyckades inte gissa rätt. Det rätta talet var {slumpmässigt_number}.")

# förbättringar som jag skulle kunna göra:
# Gör så att den antingen inte crashar när man skriver bokstäver eller att den kan acceptera när man skriver siffor i bokstäver (löst)
# Den accepterar tal utanför 1 och 200, kan göra så att den säger att det inte är ett giltigt svar och ber en att gissa inom 1-200 ramen
# Hade kunnat göra så att "exept valueerror" hade skrivit ut 1-200 istället för att jag hardcodade det i printen