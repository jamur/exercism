from string import ascii_lowercase, ascii_uppercase

def rotate(text, key):
    ciphered = ''
    for letter in text:
        if letter.isupper():
            ciphered += chr(((ord(letter) - ord('A') + key) % 26) + ord('A'))
        elif letter.islower():
            ciphered += chr(((ord(letter) - ord('a') + key) % 26) + ord('a'))
        else:
            ciphered += letter
    return ciphered

# str.maketrans
def rotate_alphabet_maketrans_translate(text, key):
    table = ascii_lowercase[key:] + ascii_lowercase[:key]
    trans = str.maketrans(ascii_lowercase + ascii_uppercase, table + table.upper())
    return text.translate(trans)

# recursion
def rotate_alphabet_recursion(text, key):
    if text == '':
        return ''
    first_letter, rest = text[0], text[1:]
    if first_letter.isupper():
        return chr(((ord(first_letter) - ord('A') + key) % 26) + ord('A')) + rotate_alphabet(rest, key)
    if first_letter.islower():
        return chr(((ord(first_letter) - ord('a') + key) % 26) + ord('a')) + rotate_alphabet(rest, key)
    return first_letter + rotate_alphabet(rest, key)

# alphabet
def rotate_alphabet(text, key):
    result = ""
    alphabet = ascii_lowercase + "áéíóúâêîôûà"

    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                result += alphabet[(alphabet.index(letter.lower()) + key) % len(alphabet)].upper()
            else:
                result += alphabet[(alphabet.index(letter) + key) % len(alphabet)]
        else:
            result += letter
    return result

# alphabet recursion
def rotate_alphabet_recursion(text, key):
    if text == "":
        return ""
    alphabet = ascii_lowercase # + "áéíóúâêîôûà"
    first_letter, rest = text[0], text[1:]
    if first_letter.isalpha():
        if first_letter.isupper():
            return alphabet[
                (alphabet.index(first_letter.lower()) + key) % len(alphabet)
                ].upper() + rotate_alphabet_recursion(rest, key)
        return alphabet[(alphabet.index(first_letter) + key) % len(alphabet)] \
               + rotate_alphabet_recursion(rest, key)
    return first_letter + rotate_alphabet_recursion(rest, key)

