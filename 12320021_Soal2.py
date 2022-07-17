n = int(input())

if n % 2 == 0:
    if 1 < n < 5:
        print("Benar")

    elif 6 < n < 15:
        print("Salah")

    elif n > 15:
        print("Benar")
else:
    print("Salah")