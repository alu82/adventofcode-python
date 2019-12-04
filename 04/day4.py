def pruefeZunahme(zahl):
    alteZahl=0
    for i in range (len(str(zahl))):
        aktuelleZahl=int(str(zahl)[i])

        if aktuelleZahl<alteZahl:
            return False
        alteZahl=aktuelleZahl
    return True

def pruefeSchnaps(zahl):
    alteZahl=0
    for i in range (len(str(zahl))):
        aktuelleZahl=int(str(zahl)[i])

        if aktuelleZahl==alteZahl:
            return True
        alteZahl=aktuelleZahl
    return False


def pruefeSchnapsDoppel(zahl):
    for i in range (10):
        anzahl_i=0
        for j in range (len(str(zahl))):
            if i==int(str(zahl)[j]):
                anzahl_i=anzahl_i+1
        if anzahl_i==2:
            return True
    return False    
    
    
#Part 1    

anzahl1=0
for zahl in range (245318, 765747, 1):
    if pruefeZunahme(zahl) and pruefeSchnaps(zahl):
        anzahl1=anzahl1+1

#print(anzahl1)
    
#Part 2

anzahl2=0
for zahl in range (245318, 765747, 1):
    if pruefeZunahme(zahl) and pruefeSchnapsDoppel(zahl):
        anzahl2=anzahl2+1

print(anzahl2)    