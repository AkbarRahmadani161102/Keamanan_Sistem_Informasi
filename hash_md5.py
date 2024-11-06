import hashlib

# Fungsi untuk menghasilkan hash MD5 dari string yang diberikan
def generate_md5_hash(input_string):
    # Membuat objek hash MD5
    md5_hash = hashlib.md5()
    # Memperbarui objek hash dengan byte dari string
    md5_hash.update(input_string.encode('utf-8'))
    # Mengembalikan representasi heksadesimal dari hash
    return md5_hash.hexdigest()

# Contoh penggunaan
input_data = "Akbar Rahmdani_2141762"  # Ganti dengan Nama dan NIM Anda
md5_result = generate_md5_hash(input_data)
print(f"MD5 Hash dari '{input_data}': {md5_result}")

result = hashlib.md5(b'Akbar Rahmdani_2141762')  # Ganti dengan Nama dan NIM Anda
print("Hash Value : ", end="")
print(result)
print("Equivalent Byte : ", end="")
print(result.digest())

result = hashlib.md5('Akbar Rahmdani_2141762'.encode())  # Ganti dengan Nama dan NIM Anda
print("Hash Value : ", end="")
print(result)
print("Hexadecimal Equivalent : ", end="")
print(result.hexdigest())