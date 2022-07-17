def perhitungan(nim):
    ans = 0
    for i in range(3):
        ans += int(nim[i])
   
    if ans < 20:
        return "Login Berhasil"
    else:
        return "Login Gagal"

nama = input()
nim = input()

print(perhitungan(nim))