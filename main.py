def hitung():
        print("Program Persegi Panjang Menghitung Luas dan Keliling Bangun Datar")
        print("1. Hitung keliling")
        print("2. Hitung luas")

        pilihan = input("Masukkan pilihan: ")
        if pilihan == "1":
            panjang = int(input("Masukkan panjang: "))
            lebar = int(input("Masukkan lebar: "))
            keliling = 2 * (panjang + lebar)
            print("Keliling persegi panjang adalah", keliling)  

        elif pilihan == "2":
            panjang = int(input("Masukkan panjang: "))
            lebar = int(input("Masukkan lebar: "))
            luas = panjang * lebar
            print("Luas persegi panjang adalah", luas)

        else:
            print("Tidak ada pilihan")

hitung()