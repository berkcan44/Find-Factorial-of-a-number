def faktoriyel(n):
   
    if n < 0:
        return "Negatif sayıların faktöriyeli tanımsızdır."
    elif n == 0 or n == 1:
        return 1
    else:
        sonuc = 1
        for i in range(2, n + 1):
            sonuc *= i
        return sonuc


sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı girin: "))
print(f"{sayi}! = {faktoriyel(sayi)}")
