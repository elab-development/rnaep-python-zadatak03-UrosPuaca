import random
import math

proizvodi = [
    "Laptop",
    "Telefon",
    "Tablet",
    "Slusalice",
    "Mis",
    "Tastatura",
    "Kamera",
    "Mikrofon"
]

cene_proizvoda = {
    "Laptop" : 1000,
    "Telefon" : 800,
    "Tablet" : 700,
    "Slusalice" : 100,
    "Mis" : 50,
    "Tastatura" : 75,
    "Kamera" :120,
    "Mikrofon" : 140
}

for proizvod, cena in cene_proizvoda.items():
    print(f"{proizvod} - {cena} €")



budzet = float(input("Unesite budzet u evrima: "))

for proizvod, cena in cene_proizvoda.items():
    if(cena <= budzet):
        print(f"Korisnik moze da kupi {proizvod} - {cena} €")



def najskuplji_proizvod(cene):
    return max(cene, key=cene.get)

najskuplji = najskuplji_proizvod(cene_proizvoda)
print(f"Najskuplji proizvod je {najskuplji} - {cene_proizvoda[najskuplji]} €")



nasumican_proizvod = random.choice(proizvodi)
print(f"Korisniku je privukao pažnju proizvod: {nasumican_proizvod}")



prosecna_cena = sum(cene_proizvoda.values()) / len(cene_proizvoda)
prosecna_cena_zaokruzena = math.floor(prosecna_cena * 100) / 100
print(f"Prosečna cena proizvoda je {prosecna_cena_zaokruzena} €")


kolicina_prodatih = [5, 8, 3, 20, 15, 10, 4, 6]
ukupan_prihod = 0
for i in range(len(proizvodi)):
    proizvod = proizvodi[i]
    prihod = cene_proizvoda[proizvod] * kolicina_prodatih[i]
    ukupan_prihod += prihod

print(f"Ukupan prihod od svih proizvoda je {ukupan_prihod} €")




novi_proizvod = "Televizor"
cena_novog = 1200
proizvodi.append(novi_proizvod)
cene_proizvoda[novi_proizvod] = cena_novog
kolicina_prodatih.append(7)

print("Ažurirana lista proizvoda:")
for proizvod, cena in cene_proizvoda.items():
    print(f"{proizvod} - {cena} €")



print("\nProizvodi sortirani od najjeftinijeg ka najskupljem:")
sortirani_proizvodi = sorted(cene_proizvoda.items(), key=lambda x: x[1])

for proizvod, cena in sortirani_proizvodi:
    print(f"{proizvod} - {cena} €")


