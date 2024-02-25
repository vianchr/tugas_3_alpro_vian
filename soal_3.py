masukan=input("masukan bulan(1-12):")
try:
    bulan = int(masukan)
    if bulan == 1 or bulan == 3 or bulan==5 or bulan==8 or bulan==7 or bulan==10 or bulan==12:
        hari = 31
        print(f"jadi total hari : {hari}")
    elif bulan == 4 or bulan==6 or bulan==9 or bulan==11 :
        hari = 30
        print(f"jadi total hari : {hari}")
    elif bulan ==2:
        hari = 29
        print(f"jadi total hari : {hari}")
    else:
        print ("bulan tersebut tidak valid")
except:
    print("terdapat salah input, cobalah masukan input bulan dengan angka antara 1-12")