import time

def pertambahan(a, b):
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        hasil = a + b
        print(f"Hasil pertambahan: {hasil}")
        time.sleep(2)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def pengurangan(a,b):
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        hasil = a - b
        print(f"Hasil pertambahan: {hasil}")
        time.sleep(2)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def perkalian(a, b):
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        hasil = a * b
        print(f"Hasil pertambahan: {hasil}")
        time.sleep(2)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def pembagian(a, b):
    try:
        a = int(input("Masukkan angka pertama: "))
        b = int(input("Masukkan angka kedua: "))
        hasil = a / b
        print(f"Hasil pertambahan: {hasil}")
        time.sleep(2)
    except ZeroDivisionError:
        print("Input ERROR: Jagan membagi dengan angka 0")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

opsi = ["1.Pertambahan","2.Pengurangan","3.Perkalian","4.Pembagian","5.Keluar"]

while True:
    print("\n",5*"=","BASIC CLI CALC PYTHON",5*"=")
    for i in opsi:
        print(i)
    
    try:
        pilihOpsi = int(input("\nPilih Opsi: "))
        
        if (pilihOpsi >= 1) and (pilihOpsi <= 5):
            if pilihOpsi == 1:
                pertambahan(0,0)
            elif pilihOpsi == 2:
                pengurangan(0,0)
            elif pilihOpsi == 3:
                perkalian(0,0)
            elif pilihOpsi == 4:
                pembagian(0,0)
            elif pilihOpsi == 5:
                break
        else:
            print(f"ERROR: Pilihan {pilihOpsi} tidak di temuka")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")


