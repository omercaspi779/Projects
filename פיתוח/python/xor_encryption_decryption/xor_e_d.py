plain_text = "omer"
asci_codes = [ord(char) for char in plain_text]
bin_text = [bin(num)[2:] for num in asci_codes]
key = "thatkey"
asci_codes_key = [ord(char) for char in key]
bin_key = [bin(num)[2:] for num in asci_codes_key]


def xor_binary(bin1, bin2):
    result = []
    for b1, b2 in zip(str(bin1),str(bin2)):
        if b1 != b2:
            result.append(1)
        else:
            result.append(0)
    return result


print(xor_binary("00000000", 11111111))



def encrypt(input_text, key2):
    encrypted_text = []
    for i in range(len(input_text)):
        append = chr(int(bin_text[i]) ^ int(bin_key[i]))
        print(append)
        encrypted_text.append(append)
    return encrypted_text


encrypted = encrypt(plain_text, key)


def decrypt(chiper_text, key):
    decrypted_text = []
    ascii_chiper = [ord(char) for char in chiper_text]
    bin_chiper = [bin(num)[2:] for num in ascii_chiper]
    for i in range(len(chiper_text)):
        append = chr(int(bin_chiper[i]) ^ int(bin_key[i]))
        print(append)
        decrypted_text.append(append)
    return decrypted_text

print()
print()
decrypt(encrypted, key)
