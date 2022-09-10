import random 
a = random.randint(1,20)
hak = 5
sayac = 0
while hak > 0:
    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))
    if a == tahmin:
        print("tahmininiz dogru")
        print(f"{sayac}.defada bildiniz puanınız: {100 - (20) * (sayac-1)}")
        break

    elif a > tahmin:
        print("yukarı")

    else:
        print("aşagi")
    if hak == 0:
        print("Kaybettiniz.")