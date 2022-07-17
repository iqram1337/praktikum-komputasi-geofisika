def perhitungan(harga, jumlah):
    return harga*jumlah

harga = int(input())
jumlah = float(input())

print("Harga bayar: Rp", int(perhitungan(harga, jumlah)))
