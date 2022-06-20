data = [["42130093", "Dewa Kadek Arie Yudha", "Teknologi Informasi"], ["42130102", "Putu Vina Junia Antarista Gunawan", "Teknologi Informasi"],
        ["42130125", "Ida Bagus Pandu Wijaya Pidada", "Teknologi Informasi"]]
x = 0
print("Silahkan Pilih nama mahasiswa berikut : ")
for i in data:
    print(f"{x+1}. {data[x][1]}")
    x = x + 1

user = int(input("Pilihan anda : "))

if user == 1:
    print(data[0])
elif user == 2:
    print(data[1])
elif user == 3:
    print(data[2])
