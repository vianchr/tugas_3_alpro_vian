#3 sisi segitiga
input_1= input("masukan sisi pertama segitiga:")
input_2= input("masukan sisi kedua segitiga:")
input_3= input("masukan sisi ketiga segitiga:")
try:
    s_1= int(input_1)
    s_2= int(input_2)
    s_3= int(input_3)
    if s_1+s_2>=s_3 and s_1+s_3>=s_2 and s_2+s_3>=s_1:
        print ("merupakan segitiga")
        if s_1 == s_2 and s_1 == s_3 and s_2 == s_3:
            print("dengan ketiga sisi yang sama")
        elif s_1 == s_2 and s_1 != s_3 or s_2 == s_3 and s_3 != s_1 or s_1==s_3 and s_2!=s_1:
            print("dengan dua sisi yang sama")
        else:
            print("tidak ada sisi yang sama")
    else:
         print("bukan segitiga")
except:
    print("terdapat salah inputan cobalah masukan input yang lain")