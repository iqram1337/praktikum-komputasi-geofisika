"""
Iqram Haris Fahromi
12320021 / Teknik Geofisika

Soal:
Buatlah program python untuk kasus sebagai berikut:

1.) Buatlah deret [1,2,3,4,…,1001]
2.) Hitunglah rata-rata dari semua bilangan genap

"""
data = [i for i in range (1,1002)]

temp = ans = 0

count = 0
for i in data:
    if i % 2 == 0:
        print(i)
        temp = temp + i
        count+=1    
ans = temp / count

print('hasil penjumlahan:', temp)
print('banyak bilangan:', count)
print('\nhasil akhir =', ans)

