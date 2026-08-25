print("=== PROGRAM KASIR KANTIN ===") 

harga = int(input("Masukkan harga makanan: ")) 
jumlah = int(input("Masukkan jumlah porsi: ")) 

total_bayar = harga * jumlah 

if total_bayar > 20000: 
    potongan = total_bayar * 0.1  # Diskon 10%
    total_bayar = total_bayar - potongan
    print("Selamat! Anda mendapatkan diskon 10%") 
else: 
    print("Maaf, belum mencapai batas minimal diskon") 

print(f"Total yang harus dibayar: Rp{int(total_bayar)}")