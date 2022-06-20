data = []
x = 0
while True:
    user = input("Masukan Angka : ")
    if user == 'n':
        break
    data.append(user)

jumlah = 0
for nilai in data:
    jumlah += int(nilai)
print(jumlah)
