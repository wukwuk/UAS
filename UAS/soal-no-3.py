data = []
x = 0
while True:
    user = input("Masukan Angka : ")
    if user == 'n':
        break
    x += 1
    data.append(user)

rata2 = 0
for nilai in data:
    rata2 += int(nilai)
rata2 /= x
print(f"Rata - rata nilai : {rata2}")
