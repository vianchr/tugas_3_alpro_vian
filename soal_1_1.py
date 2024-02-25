user = input("Masukkan suhu tubuh: ")
try :
    suhu = int(user)
    if suhu >= 38:
        print("Anda demam")

    else:
        print("Anda tidak demam")
except :
    print("Anda memasukan inputan yang salah")