# Detta programet beräknar hur mycket pengar du har sparat efter ett visst antal månader, med en given ränta.
# Hade problemt i början med att få den att räkna ut självaste räntan, så jag la till float + int på variablerna och sedan la jag till uträkningen av räntan så fungerade det efteråt.

# Variablar och inputs där du skriver dinna svar
try:
    name = (input("Vad är ditt namn?: "))
    månadsbelopp = float(input("Vad är ditt månadsbelopp?: "))
    antal_månader = int(input("Hur många månader?: "))
    ränta_i_procent = float(input("Vad är räntan i procent?: "))

except ValueError:
    print("Felaktig inmatning. Vänligen ange siffror för belopp, månader och ränta.")
    exit()  # Avslutar programmet om det är en ogiltig inmatning

# Här sker uträkningen av det beloppet.
total = månadsbelopp * antal_månader
ränta = total * (ränta_i_procent / 100)
summa = total + ränta

# Här får du tillbaka ditt svar utfrån det du skrev in i början.
print(f" Totala insatta beloppet: {total:.0f}kr")
print(f" {name} ditt totala belopp efter {antal_månader} månader med ränta, så har du sparat {summa:.0f}kr")

# Fungerade programmet direkt som du tänkte? Nej det gjorde det inte, jag hade problem med att få den att räkna ut räntan, så jag la till float + int på variablerna och sedan la jag till uträkningen av räntan så fungerade det efteråt.
# Uppstod något problem? Svårt att förstår exakt hur jag skulle göra iträkninken av räntan, men efter jag la till några flera variabler (total och ränta) så blev det enkelt att räkna ut det.
# Vad ändrade du i koden för att lösa det? Jag la till total och ränta + int och float på variablerna så att det skulle kunna räkna ut det.
# Finns det något du skulle kunna förbättra i programmet? Säkerligen uträkningen av räntan, men utöver det så är jag nöjd med programmet.

# Normal världen fungerar (siffror)
# Gränsnit värde som 0 fungerar och hög tal fungerar
# Programet crachar vid text