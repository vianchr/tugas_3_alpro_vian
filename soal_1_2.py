suiii = input("Masukkan suatu bilangan: ")
try:
    bilangan = int(suiii)
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except :
    print("anda memasukan inputan yang salah, cobalah memasukan angka")