Nama = input("Masukkan Nama Mahasiswa: ")
Nilai = int(input("Masukkan Nilainya: "))

if (Nilai < 0 or Nilai > 100) : 
        print(f"Nilai {Nama} tidak valid")
elif(Nilai >=90) : 
        print(f"Grade {Nama} adalah A")
elif(Nilai >=80) : 
        print(f"Grade {Nama} adalah B")
elif(Nilai >=70) : 
        print(f"Grade {Nama} adalah C")
elif(Nilai >=60) : 
        print(f"Grade {Nama} adalah D")
elif(Nilai < 60) : 
        print(f"Grade {Nama} adalah E")
