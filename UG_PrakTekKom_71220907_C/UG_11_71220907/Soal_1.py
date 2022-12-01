print("=========================")
print("Operasi Matematika")
print("1. Jumlah         [+]")
print("2. Kurang         [-]")
print("3. Kali           [*]")
print("4. Bagi           [/]")
print("=========================")
pilop = int(input("Pilih Operasi (1/2/3/4): "))
print("=========================")
if pilop==1:
    def jumlah(pertama, kedua):
                hasil_jumlah = pertama+kedua
                return hasil_jumlah
if pilop==2:  
    def kurang(pertama, kedua):
                hasil_kurang = pertama-kedua
                return hasil_kurang
if pilop==3:
    def kali(pertama, kedua):
                hasil_kali = pertama*kedua
                return hasil_kali
if pilop==4:
    def bagi(pertama, kedua):
                hasil_bagi = pertama/kedua
                return hasil_bagi

pertama = int(input("Masukkan bilangan pertama: "))
kedua = int(input("Masukkan bilangan kedua: "))
if pilop==1:
    print("Hasil operasi dari",pertama,"+",kedua,"=",jumlah(pertama, kedua))
elif pilop==2:
    print("Hasil operasi dari",pertama,"-",kedua,"=",kurang(pertama, kedua))
elif pilop==3:
    print("Hasil operasi dari",pertama,"*",kedua,"=",kali(pertama, kedua))
elif pilop==4:
    print("Hasil operasi dari",pertama,"/",kedua,"=",bagi(pertama, kedua))
    


            
            
