def Encryption(plaintext, key_val):
    ciphertext = ""
    
    for i in range(len(plaintext)):
        special = plaintext[i]
        new_special = special.lower()

        if new_special == ' ':
            ciphertext += ' '
        elif special.isalpha():
            # Shift character and wrap around using modulo
            shift = (ord(new_special) + key_val - 97) % 26 + 97
            ciphertext += chr(shift)
    
    return ciphertext

def Decryption(ciphertext, key_val):
    plaintext = ""
    
    for i in range(len(ciphertext)):
        special = ciphertext[i]
        new_special = special.lower()

        if new_special == ' ':
            plaintext += ' '
        elif special.isalpha():
            # Shift character back and wrap around using modulo
            shift = (ord(new_special) - key_val - 97) % 26 + 97
            plaintext += chr(shift)
    
    return plaintext

while True:
    print("Welcome to my Word Encryption Tool..")
    print("[*] Tombol 1 untuk Enkripsi")
    print("[*] Tombol 0 untuk Deskripsi")
    print("[*] Tombol 01 untuk Keluar")
    print("Tip ---> Encryption/Decryption with shift value of your choice!")

    choice = input('Masukkan Kode: ')
    
    if choice.isdigit():
        if choice == '1':
            sen = input('Masukkan Teks: ')
            key = int(input("Masukkan Kunci (Nilai): "))
            print(50 * "-")
            print(f'Ciphertext Enkripsi ---> {Encryption(sen, key)}')
            print(50 * "-")
            con = input('Shall we continue? (Any Ya/Tidak): ')
            if con.lower() == 'no':
                print('Exiting..')
                break
            else:
                pass
        
        elif choice == '0':
            csen = input('Masukkan Teks: ')
            key = int(input("Masukkan Kunci: "))
            print(50 * "-")
            print(f'Hasil Deskripsi ---> {Decryption(csen, key)}')
            print(50 * "-")
            print('Special symbols (1, etc) and numbers are deleted..')
            con = input('Shall we continue? [Any Ya/Tidak]: ')
            if con.lower() == 'no':
                print('Exiting..')
                break
            else:
                pass
        
        elif choice == '01':
            print('Exiting..')
            break
        
        else:
            print('Exception error.. \nPlease insert 0 or 1')
    else:
        print('Invalid input, please enter a digit.')
