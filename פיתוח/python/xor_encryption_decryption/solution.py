plain_text = "omer"
key = "thatkey"

# המרת טקסט וקוד ASCII לייצוג בינארי
ascii_plain_text = [ord(char) for char in plain_text]
ascii_key = [ord(char) for char in key]

# הבטחת אורך מתאים למפתח (הארכה או חיתוך)
while len(ascii_key) < len(ascii_plain_text):
    ascii_key.extend(ascii_key)
ascii_key = ascii_key[:len(ascii_plain_text)]

# המרת ASCII לבינארי
bin_plain_text = [format(num, '08b') for num in ascii_plain_text]
bin_key = [format(num, '08b') for num in ascii_key]


def xor_binary(bin1, bin2):
    """
    מבצע XOR על שני מחרוזות בינאריות.
    """
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bin1, bin2))


def encrypt_binary(input_text, key_binary):
    encrypted_binary = []
    for i in range(len(input_text)):
        encrypted_char = xor_binary(input_text[i], key_binary[i])  # XOR בין תווי הטקסט והמפתח
        encrypted_binary.append(encrypted_char)
    return encrypted_binary


def decrypt_binary(encrypted_binary, key_binary):
    decrypted_binary = []
    for i in range(len(encrypted_binary)):
        decrypted_char = xor_binary(encrypted_binary[i], key_binary[i])  # XOR שוב כדי לפענח
        decrypted_binary.append(decrypted_char)
    return decrypted_binary


def binary_to_ascii(binary_list):
    """
    המרה מייצוג בינארי לאסקי.
    """
    return [int(b, 2) for b in binary_list]


def ascii_to_text(ascii_list):
    """
    המרה מקוד ASCII לטקסט רגיל.
    """
    return ''.join([chr(num) for num in ascii_list])


# הצפנה
encrypted = encrypt_binary(bin_plain_text, bin_key)
print("טקסט מוצפן (בינארי):", encrypted)

# המרה לאסקי מוצפן
encrypted_ascii = binary_to_ascii(encrypted)
print("טקסט מוצפן (אסקי):", encrypted_ascii)
ascii_n = [chr(num) for num in encrypted_ascii]
p
# פענוח לבינארי לא מוצפן
decrypted_binary = decrypt_binary(encrypted, bin_key)
print("בינארי לא מוצפן:", decrypted_binary)

# המרה לאסקי לא מוצפן
decrypted_ascii = binary_to_ascii(decrypted_binary)
print("אסקי לא מוצפן:", decrypted_ascii)

# המרה לטקסט רגיל לא מוצפן
decrypted_text = ascii_to_text(decrypted_ascii)
print("טקסט רגיל לא מוצפן:", decrypted_text)
