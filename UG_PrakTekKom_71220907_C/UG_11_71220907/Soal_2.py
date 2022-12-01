print("Pemerikasa kelipatan 9")      
hakehokya = int(input("Masukkan kelipatan 9 yang ingin diperiksa: "))
def kelipatan_sembilan():
    jawab = (hakehokya%9)
    return jawab

if kelipatan_sembilan()==0:
    print("Benar")
else:
    print("Salah")
