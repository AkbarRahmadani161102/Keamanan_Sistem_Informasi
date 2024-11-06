import string

# Fungsi untuk membersihkan input (menghapus karakter non-alfabet)
def clean_input(text):
    return ''.join([char.upper() for char in text if char.isalpha()])

# Fungsi untuk memperluas kunci agar sepanjang plainteks
def extend_key(plain_text, key):
    key = key.upper()
    key_extended = key * (len(plain_text) // len(key)) + key[:len(plain_text) % len(key)]
    return key_extended

# Fungsi untuk enkripsi Vigenère Cipher
def encrypt_vigenere(plain_text, key):
    key_extended = extend_key(plain_text, key)
    cipher_text = []
    
    for i in range(len(plain_text)):
        shift = (ord(plain_text[i]) - ord('A') + ord(key_extended[i]) - ord('A')) % 26
        cipher_text.append(chr(shift + ord('A')))
        
    return ''.join(cipher_text)

# Fungsi untuk dekripsi Vigenère Cipher
def decrypt_vigenere(cipher_text, key):
    key_extended = extend_key(cipher_text, key)
    plain_text = []
    
    for i in range(len(cipher_text)):
        shift = (ord(cipher_text[i]) - ord(key_extended[i]) + 26) % 26
        plain_text.append(chr(shift + ord('A')))
        
    return ''.join(plain_text)

# Fungsi untuk format cipherteks
def format_ciphertext(cipher_text, format_type):
    if format_type == '1':  # Apa adanya
        return cipher_text
    elif format_type == '2':  # Tanpa spasi
        return cipher_text.replace(' ', '')
    elif format_type == '3':  # Dalam kelompok 5 huruf
        return ' '.join(cipher_text[i:i + 5] for i in range(0, len(cipher_text), 5))

# Fungsi untuk membaca dari file atau papan ketik
def read_input():
    choice = input("Masukkan pilihan: (1) file teks atau (2) papan ketik: ")
    if choice == '1':
        file_name = input("Masukkan nama file: ")
        with open(file_name, 'r') as file:
            text = file.read()
    elif choice == '2':
        text = input("Ketikkan pesan: ")
    return clean_input(text)

# Fungsi utama program
def main():
    while True:
        print("\n=== Program Vigenère Cipher ===")
        action = input("Pilih aksi: (1) Enkripsi atau (2) Dekripsi: ")
        text = read_input()
        key = input("Masukkan kunci (maksimal 25 huruf): ")
        key = clean_input(key[:25])
        
        if action == '1':  # Enkripsi
            cipher_text = encrypt_vigenere(text, key)
            print("\n=== Hasil Enkripsi ===")
            print("Plainteks   : ", text)
            print("Cipherteks  : ", cipher_text)
            
            # Opsi tampilan cipherteks
            format_choice = input("Pilih format cipherteks: (1) apa adanya, (2) tanpa spasi, (3) kelompok 5-huruf: ")
            formatted_ciphertext = format_ciphertext(cipher_text, format_choice)
            print("Cipherteks (format): ", formatted_ciphertext)
            
            # Simpan ke file
            save_choice = input("Simpan cipherteks ke file? (y/n): ")
            if save_choice.lower() == 'y':
                output_file = input("Masukkan nama file output: ")
                with open(output_file, 'w') as file:
                    file.write(formatted_ciphertext)
                print("Cipherteks disimpan ke file", output_file)
                
        elif action == '2':  # Dekripsi
            plain_text = decrypt_vigenere(text, key)
            print("\n=== Hasil Dekripsi ===")
            print("Cipherteks  : ", text)
            print("Plainteks   : ", plain_text)
        
        # Looping untuk program
        cont = input("Apakah Anda ingin melanjutkan? (y/n): ")
        if cont.lower() != 'y':
            break

# Jalankan program
if __name__ == "__main__":
    main()
