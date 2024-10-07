from Crypto.Cipher import DES # type: ignore

def pad(text):
    # Padding to make the text a multiple of 8
    while len(text) % 8 != 0:
        text += ' '
    return text

def enkripsi(pesan, kunci):
    if len(kunci) < 8:
        print("Kunci harus minimal 8 karakter.")
        return

    # Truncate the key to 8 characters if it's longer
    kunci_bytes = kunci[:8].encode()  # Convert key to bytes and truncate if necessary
    cipher = DES.new(kunci_bytes, DES.MODE_ECB)  # Define DES ECB mode
    pesan_pad = pad(pesan)  # Pad the message to be a multiple of 8
    encrypted_pesan = cipher.encrypt(pesan_pad.encode())  # Encrypt message
    print(f"Hasil enkripsi: {encrypted_pesan}")
    return encrypted_pesan  # Return ciphertext

def dekripsi(pesan_terenkripsi, kunci):
    if len(kunci) < 8:
        print("Kunci harus minimal 8 karakter.")
        return

    # Truncate the key to 8 characters if it's longer
    kunci_bytes = kunci[:8].encode()  # Convert key to bytes and truncate if necessary
    cipher = DES.new(kunci_bytes, DES.MODE_ECB)  # Define DES ECB mode
    decrypted_pesan = cipher.decrypt(pesan_terenkripsi).decode().strip()  # Decrypt message and remove padding
    print(f"Hasil dekripsi: {decrypted_pesan}")
    
def ProgramEnkripsiDeskripsiDES():
    print("Pilih:")
    print("1. Enkripsi")
    print("2. Deskripsi")
    pilih = input()  # Get user selection

    if pilih == '1':
        print("Masukkan pesan yang akan dienkripsi:")
        pesan = input()
        print("Pilih panjang kunci:")
        print("1. 8 karakter")
        print("2. 10 karakter")
        pilihan_kunci = input()

        if pilihan_kunci == '1':
            print("Masukkan kunci 8 karakter:")
            kunci = input()

        elif pilihan_kunci == '2':
            print("Masukkan kunci 10 karakter:")
            kunci = input()
            if len(kunci) < 10:
                print("Kunci harus 10 karakter.")
                return
        else:
            print("Pilihan salah.")
            return

        print("Enkripsi pesan...")
        enkripsi(pesan, kunci)  # Call encryption function

    elif pilih == '2':
        print("Masukkan cipherteks yang akan dideskripsi (dalam format b'...'):")
        pesan = input()  # Get ciphertext input from user

        try:
            pesan_terenkripsi = eval(pesan)  # Convert string to bytes format
            print("Pilih panjang kunci:")
            print("1. 8 karakter")
            print("2. 10 karakter")
            pilihan_kunci = input()

            if pilihan_kunci == '1':
                print("Masukkan kunci 8 karakter:")
                kunci = input()

            elif pilihan_kunci == '2':
                print("Masukkan kunci 10 karakter:")
                kunci = input()
                if len(kunci) < 10:
                    print("Kunci harus 10 karakter.")
                    return
            else:
                print("Pilihan salah.")
                return

            dekripsi(pesan_terenkripsi, kunci)  # Call decryption function

        except:
            print("Format cipherteks tidak valid.")
    else:
        print("Pilihan salah")  # Display message if input is invalid

# Run the program
ProgramEnkripsiDeskripsiDES()
