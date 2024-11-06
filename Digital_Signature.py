import math
import random

# --------Definisi Fungsi untuk Membuat Kunci RSA--------

# Fungsi untuk memeriksa apakah sebuah bilangan adalah bilangan prima
def is_prime(number):
    if number < 2:
        return False
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
    while not is_prime(prime):
        prime = randint(min_value, max_value)
    return prime

# Fungsi untuk menemukan nilai "d" yang memenuhi persamaan e * d ≡ 1 mod(totient_n)
def mod_inverse(e, totient_n):
    d = 3
    while (d * e) % totient_n != 1:
        d += 1
    return d

# --------Definisi Fungsi untuk Tanda Tangan Digital--------

# Fungsi untuk membagi pesan menjadi blok-blok
def split_into_blocks(message, block_size):
    return [message[i : i + block_size] for i in range(0, len(message), block_size)]

# Fungsi untuk enkripsi blok dengan kunci pribadi
def encrypt_block(block, d, n):
    block_int = int.from_bytes(block.encode("utf-8"), byteorder="big")
    encrypted_block_int = pow(block_int, d, n)
    return encrypted_block_int

# Fungsi untuk dekripsi blok dengan kunci publik
def decrypt_block(encrypted_block_int, e, n):
    decrypted_block_int = pow(encrypted_block_int, e, n)
    decrypted_block_bytes = decrypted_block_int.to_bytes(
        (decrypted_block_int.bit_length() + 7) // 8, byteorder="big"
    )
    return decrypted_block_bytes.decode("utf-8")

# Fungsi untuk menandatangani pesan
def sign(message, d, n):
    block_size = (n.bit_length() - 1) // 8
    if len(message) <= block_size:
        return [encrypt_block(message, d, n)]
    else:
        blocks = split_into_blocks(message, block_size)
        signed_blocks = [encrypt_block(block, d, n) for block in blocks]
        return blocks, signed_blocks

# Fungsi untuk memverifikasi tanda tangan
def verify(signed_blocks, e, n, original_message):
    decrypted_blocks = [
        decrypt_block(signed_block, e, n) for signed_block in signed_blocks
    ]
    decrypted_message = "".join(decrypted_blocks)
    return decrypted_message == original_message

# --------Proses Pembuatan Kunci untuk RSA--------

p, q = generate_prime(3, 5000), generate_prime(3, 5000)
while p == q:
    q = generate_prime(3, 47)

n = p * q
totient_n = (p - 1) * (q - 1)

# Mencari nilai "e" yang relatif prima dengan "totient_n"
e = randint(3, totient_n - 1)
while math.gcd(e, totient_n) != 1:
    e = randint(3, totient_n - 1)

d = mod_inverse(e, totient_n)

# Menampilkan kunci yang dihasilkan
print(
    f"\nKunci Publik: {e}\nKunci Privat: {d}\nn: {n}\nTotient dari n: {totient_n}\np: {p}\nq: {q}\n"
)

# Memasukkan pesan yang akan ditandatangani
message = input("Masukkan pesan: ")
blocks, signed_blocks = sign(message, d, n)
verification_result = verify(signed_blocks, e, n, message)

# Menampilkan hasil tanda tangan
blocks_str = "".join(blocks)
signed_blocks_str = " ".join(map(str, signed_blocks))
signed_message = blocks_str + " | " + signed_blocks_str

print("\nPesan Terpisah:", blocks)
print("Blok Tertandatangani:", signed_blocks)
print("Pesan Tertandatangani:", signed_message)
print("Hasil Verifikasi:", verification_result)
