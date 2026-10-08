## Tipe Data = Intteger, Float, String, Boolean
"""
data_integer = 10
print(type(data_integer))
print("Data : ", data_integer, ". Tipe : ",type(data_integer))

print("=====================================")

data_float = 15.5
print(type(data_float))
print("Data : ", data_float, "Tipe : ", type(data_float))

print("=====================================")

data_string = "Hello Dog"
print(type(data_string))
print("Data : ", data_string, ". Tipe : ", type(data_string))

print("=====================================")

data_boolean = True
print(type(data_boolean))
print("Data : ", data_boolean, ". Tipe : ", type(data_boolean))

print("=====================================")

data_boolean = False
print(type(data_boolean))
print("Data : ", data_boolean, ". Tipe : ", type(data_boolean))

print("=====================================")
"""

## CASTING TIPE DATA

## DATA INTEGER
"""
print("====Data Integer====")

data_A = 110
data_B = 0

data_int = int(data_A)
print("Data : ", data_int, ". Tipe : ", type(data_int))

data_float = float(data_A)
print("Data : ", data_float, ". Tipe : ", type(data_float))

data_str = str(data_A)
print("Data : ", data_str, ". Tipe : ", type(data_str))

data_bool = bool(data_A)
print("Data : ", data_bool, ". Tipe : ", type(data_bool))

data_bool = bool(data_B)
print("Data : ", data_bool, ". Tipe : ", type(data_bool))
"""
## DATA FLOAT
"""
print("====Data Float====")

data_C = 15.5
data_D = 0.0

data_int = int(data_C)
print("Data : ", data_int, ". Tipe : ", type(data_int))

data_float = float(data_C)
print("Data : ", data_float, ". Tipe : ", type(data_float))

data_str = str(data_C)
print("Data : ", data_str, ". Tipe : ", type(data_str))

data_bool = bool(data_C)
print("Data : ", data_bool, ". Tipe : ", type(data_bool))

data_bool = bool(data_D)
print("Data : ", data_bool, ". Tipe : ", type(data_bool))
"""
## DATA BOOLEAN
"""
print("===Data Boolean====")

data_E = True
data_F = False

data_int = int(data_E)
data_int2 = int(data_F)
print("Data : ", data_int, ". Tipe : ", type(data_int))
print("Data : ", data_int2, ". Tipe : ", type(data_int2))

data_float = float(data_E)
data_float2 = float(data_F)
print("Data : ", data_float, ". Tipe : ", type(data_float))
print("Data : ", data_float2, ". Tipe : ", type(data_float2))

data_str = str(data_E)
data_str2 = str(data_F)
print("Data : ", data_str, ". Tipe : ", type(data_str))
print("Data : ", data_str2, ". Tipe : ", type(data_str2))

data_bool = bool(data_E)
data_bool2 = bool(data_F)
print("Data : ", data_bool, ". Tipe : ", type(data_bool))
print("Data : ", data_bool2, ". Tipe : ", type(data_bool2))
"""

## DATA STRING (Untuk int dan float harus angka)
"""
print("===Data String====")

data_G = "100"
data_H = ""

data_int = int(data_G)
print("Data : ", data_int, ". Tipe : ", type(data_int))

data_float = float(data_G)
print("Data : ", data_float, ". Tipe : ", type(data_float))

data_str = str(data_G)
data_str2 = str(data_H)
print("Data : ", data_str, ". Tipe : ", type(data_str))
print("Data : ", data_str2, ". Tipe : ", type(data_str2))

data_bool = bool(data_G)
data_bool2 = bool(data_H)
print("Data : ", data_bool, ". Tipe : ", type(data_bool))
print("Data : ", data_bool2, ". Tipe : ", type(data_bool2))
"""

## INPUT DATA DARI USER
"""
data_nama = (input("Masukan nama : "))
data_umur = (int(input("Masukan umur : ")))
biner_nama = bool(data_nama)
biner_umur = bool(data_umur)

print("Nama : ", data_nama, f"({biner_nama})", ". Umur : ", data_umur, f"({biner_umur})")
"""

## IF, ELSE, ELIF STATEMENT
"""
id_nama = input("Masukan nama : ")
id_nomor = int(input("Masukan nomor : "))

if id_nama == "Jet" and id_nomor == 123:
    print(f"Selamat datang admin {id_nama}")
elif id_nama == "" and id_nomor == 0:
    id_nama_baru = input("Masukan nama baru : ")
    id_nomor_baru = int(input("Masukan nomor baru : "))
    print(f"Selamat datang {id_nama_baru}, nomor anda adalah {id_nomor_baru}")
else:
    print("Program selesai, silahkan coba lagi")
"""

## PERCABANGAN (Kalkulator sederhana)
"""
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=", "\n")

angka_1 = float(input("Masukan angka pertama : "))
operator = input("Masukan operator (+, -, x, /) : ")
angka_2 = float(input("Masukan angka kedua : "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"Hasilnya {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"Hasilnya {hasil}")
elif operator == "x" or operator == "*":
    hasil = angka_1 * angka_2
    print(f"Hasilnya {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"Hasilnya {hasil}")
else:
    print("Kalo negtik yang bener mas")

print("Program selesai Terimagajih udah make kalkulator ini")
"""

## PERULANGAN (For Loop)
"""
angka = range(1, 11)
for i in angka:
    print(f"Perulangan ke-{i}")
print("Perulangan selesai")
"""

## PERULANGAN (While Loop)
"""
angka = 0
print(f"Angka sekarang : {angka}")

while angka < 10:
    angka += 1
    print(f"Angka sekarang : {angka}")
    print("Gugugaga")

print("Udah")
"""

## ARRAY / LIST
"""
data_range = range(0, 11)
print(list(data_range))
"""

## FUNCTION
"""
nama = "Jet"
id_nomor = 123
alamat = "Jl. Raya No. 123"

def biodata():
    print("Biodata telah di temukan")
    print(f"Nama : {nama}")
    print(f"Nomor : {id_nomor}")
    print(f"Alamat : {alamat}")
    print("Scraping selesai, berikan biodata lagi jika ingin menggunakan program ini")

biodata()
"""