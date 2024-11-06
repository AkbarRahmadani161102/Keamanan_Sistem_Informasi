import hashlib  # Mengimpor pustaka hashlib untuk menghasilkan hash menggunakan algoritma seperti MD5

# Fungsi untuk menghasilkan hash MD5 dari string yang diberikan
def generate_md5_hash(input_string):
    # Membuat objek hash MD5
    md5_hash = hashlib.md5()
    # Memperbarui objek hash dengan byte dari string
    md5_hash.update(input_string.encode('utf-8'))  # Mengonversi string menjadi byte dan memperbarui objek hash
    # Mengembalikan representasi heksadesimal dari hash
    return md5_hash.hexdigest()  # Menghasilkan hash dalam format heksadesimal

# Contoh penggunaan
input_data = "Akbar Rahmdani_2141762"  # Ganti dengan Nama dan NIM Anda
md5_result = generate_md5_hash(input_data)  # Menghasilkan hash MD5 untuk input_data
print(f"MD5 Hash dari '{input_data}': {md5_result}")  # Menampilkan hasil hash MD5 dari input_data

# Menghitung hash MD5 secara langsung tanpa fungsi
result = hashlib.md5(b'Akbar Rahmdani_2141762')  # Ganti dengan Nama dan NIM Anda, input dalam format byte
print("Hash Value : ", end="")  # Menampilkan teks "Hash Value : " tanpa karakter newline di akhir
print(result)  # Menampilkan objek hash MD5 yang dihasilkan (bukan nilai hash itu sendiri)
print("Equivalent Byte : ", end="")  # Menampilkan teks "Equivalent Byte : " tanpa karakter newline di akhir
print(result.digest())  # Menampilkan nilai hash dalam format byte, hasil dari metode digest()

# Menghitung hash MD5 dengan format heksadesimal langsung
result = hashlib.md5('Akbar Rahmdani_2141762'.encode())  # Ganti dengan Nama dan NIM Anda, string dikonversi menjadi byte
print("Hash Value : ", end="")  # Menampilkan teks "Hash Value : " tanpa karakter newline di akhir
print(result)  # Menampilkan objek hash MD5 yang dihasilkan (bukan nilai hash itu sendiri)
print("Hexadecimal Equivalent : ", end="")  # Menampilkan teks "Hexadecimal Equivalent : " tanpa karakter newline di akhir
print(result.hexdigest())  # Menampilkan nilai hash dalam format heksadesimal, hasil dari metode hexdigest()
