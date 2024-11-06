import math  # Mengimpor pustaka math untuk operasi matematika
import random  # Mengimpor pustaka random untuk menghasilkan bilangan acak

# --------Definisi Fungsi untuk Membuat Kunci RSA--------

# Fungsi untuk memeriksa apakah sebuah bilangan adalah bilangan prima
def is_prime(number):
    if number < 2:
        return False
    # Mengecek apakah number habis dibagi oleh angka antara 2 hingga akar number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Fungsi untuk membuat bilangan acak dalam interval tertentu
def randint(min_value, max_value):
    return random.randint(min_value, max_value)

# Fungsi untuk menghasilkan bilangan prima secara acak dalam interval tertentu
def generate_prime(min_value, max_value):
    prime = randint(min_value, max_value)
    # Mengulangi hingga bilangan acak yang dihasilkan adalah bilangan prima
    while not is_prime(prime):
        prime = randint(min_value, max_value)
    return prime

# Fungsi untuk menemukan nilai "d" yang memenuhi persamaan e * d ≡ 1 mod(totient_n)
def mod_inverse(e, totient_n):
    d = 3  # Memulai pencarian dari nilai d = 3
    # Mengulangi hingga menemukan d yang memenuhi (d * e) % totient_n == 1
    while (d * e) % totient_n != 1:
        d += 1
    return d

# --------Definisi Fungsi untuk Tanda Tangan Digital--------

# Fungsi untuk membagi pesan menjadi blok-blok
def split_into_blocks(message, block_size):
    # Membagi pesan ke dalam blok dengan ukuran yang ditentukan
    return [message[i : i + block_size] for i in range(0, len(message), block_size)]

# Fungsi untuk enkripsi blok dengan kunci pribadi
def encrypt_block(block, d, n):
    # Mengonversi blok teks menjadi integer
    block_int = int.from_bytes(block.encode("utf-8"), byteorder="big")
    # Mengenkripsi integer blok menggunakan kunci privat (d) dan modulus n
    encrypted_block_int = pow(block_int, d, n)
    return encrypted_block_int

# Fungsi untuk dekripsi blok dengan kunci publik
def decrypt_block(encrypted_block_int, e, n):
    # Mendekripsi integer blok menggunakan kunci publik (e) dan modulus n
    decrypted_block_int = pow(encrypted_block_int, e, n)
    # Mengonversi integer hasil dekripsi kembali menjadi teks
    decrypted_block_bytes = decrypted_block_int.to_bytes(
        (decrypted_block_int.bit_length() + 7) // 8, byteorder="big"
    )
    return decrypted_block_bytes.decode("utf-8")

# Fungsi untuk menandatangani pesan
def sign(message, d, n):
    block_size = (n.bit_length() - 1) // 8  # Menentukan ukuran blok
    if len(message) <= block_size:
        # Jika panjang pesan kurang dari ukuran blok, enkripsi langsung
        return [encrypt_block(message, d, n)]
    else:
        # Membagi pesan menjadi beberapa blok
        blocks = split_into_blocks(message, block_size)
        # Mengenkripsi setiap blok menggunakan kunci privat
        signed_blocks = [encrypt_block(block, d, n) for block in blocks]
        return blocks, signed_blocks

# Fungsi untuk memverifikasi tanda tangan
def verify(signed_blocks, e, n, original_message):
    # Mendekripsi setiap blok terenkripsi menggunakan kunci publik
    decrypted_blocks = [
        decrypt_block(signed_block, e, n) for signed_block in signed_blocks
    ]
    # Menggabungkan blok-blok yang didekripsi menjadi pesan lengkap
    decrypted_message = "".join(decrypted_blocks)
    # Mengembalikan True jika pesan yang didekripsi sama dengan pesan asli
    return decrypted_message == original_message

# --------Proses Pembuatan Kunci untuk RSA--------

# Menghasilkan dua bilangan prima p dan q dalam rentang tertentu
p, q = generate_prime(3, 5000), generate_prime(3, 5000)
while p == q:  # Pastikan p dan q berbeda
    q = generate_prime(3, 5000)

n = p * q  # Menghitung nilai n sebagai hasil perkalian p dan q
totient_n = (p - 1) * (q - 1)  # Menghitung totient dari n

# Mencari nilai "e" yang relatif prima dengan "totient_n"
e = randint(3, totient_n - 1)
while math.gcd(e, totient_n) != 1:
    e = randint(3, totient_n - 1)

d = mod_inverse(e, totient_n)  # Menghitung nilai d sebagai invers modular dari e

# Menampilkan kunci yang dihasilkan
print(
    f"\nKunci Publik: {e}\nKunci Privat: {d}\nn: {n}\nTotient dari n: {totient_n}\np: {p}\nq: {q}\n"
)

# Memasukkan pesan yang akan ditandatangani
message = input("Masukkan pesan: ")
# Menandatangani pesan
blocks, signed_blocks = sign(message, d, n)
# Memverifikasi tanda tangan
verification_result = verify(signed_blocks, e, n, message)

# Menampilkan hasil tanda tangan
blocks_str = "".join(blocks)  # Menggabungkan blok pesan asli
signed_blocks_str = " ".join(map(str, signed_blocks))  # Menggabungkan blok yang ditandatangani
signed_message = blocks_str + " | " + signed_blocks_str  # Menyusun pesan yang ditandatangani

print("\nPesan Terpisah:", blocks)
print("Blok Tertandatangani:", signed_blocks)
print("Pesan Tertandatangani:", signed_message)
print("Hasil Verifikasi:", verification_result)  # Menampilkan hasil verifikasi tanda tangan
