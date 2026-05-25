# Skriv temperaturen i Celsius och den kommer sedan att konverteras till Fahrenheit
# Hade svårt att förstå hur jag skulle hantera ogiltiga inmatningar, så jag kollade på w3schools och hittade att om man skriver try och except så kan man hantera olaglia inmatningar som bokstäver eller specialtecken. Så nu om man skriver något fel så kommer den printa vad man gjorde fel och hur man ska göra.

# Detta rätnar ut temperaturen i Celsius och konverterar den till Fahrenheit
try:
    celsius = float(input("Ange temperaturen i Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:.1f}°C är lika med {fahrenheit:.1f}°F" )

# Detta hanterar ogiltiga inmatningar
except ValueError:
    print("Fel, du måste ange en siffra och inga bokstäver eller specialtecken")

# Fungerade programmet direkt som du tänkte? Det fungerade inte dirket. Behövde lägga till try och except för att få felhantering att fungera. Men i slutändan så fungerade det.
# Uppstod något problem? Ja, att förstå hur man skulle hantera ogiltiga inmatningar.
# Vad ändrade du i koden för att lösa det? Jag la till try och except för att hantera ogiltiga inmatningar.
# Finns det något du skulle kunna förbättra i programmet? Inget som jag kan komma på just nu.

# Normal världen fungerar (siffror)
# Gränsnit värde som 0 fungerar och höga siffror fungerar
# Programet crachar inte vid text eller specialtecken och ber en om att använda sig av siffror istället