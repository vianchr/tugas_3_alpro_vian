# input a, b dan c
prtm = input("Masukkan bilangan pertama: ")
kdua = input("Masukkan bilangan kedua: ")
tga = input("Masukkan bilangan ketiga: ")
 # secara berurutan tulis kriteria untuk a, b, dan c
try : 
    a = int(prtm)
    b = int(kdua)
    c = int(tga)
    if a > b and a > c:
        print("Terbesar: ", a)
    elif b > a and b > c:
        print("Terbesar: ", b)
    elif c > a and c > b:
        print("Terbesar: ", c)
except :
    print("terdapat kesalahan input,cobalah input ulang")