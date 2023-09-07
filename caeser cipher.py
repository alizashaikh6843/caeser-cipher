def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted = shifted.upper()
            result += shifted
        else:
            result += char
    return result

# Example usage
plaintext = "Aliza Shaikh"
shift_amount = 3

encrypted_text = caesar_cipher(plaintext, shift_amount)
print("Encrypted:", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift_amount)
print("Decrypted:", decrypted_text)
