A_LCASE = 97
Z_LCASE = 122
A_UCASE = 65
Z_UCASE = 90

def is_isogram_bak(string):
    only_letters = [letter for letter in string.casefold() if letter.isalpha()]
    return len(set(only_letters)) == len(only_letters)

def is_isogram_bit_field(phrase):
    letter_flags = 0

    for ltr in phrase:
        letter = ord(ltr)
        if A_LCASE <= letter <= Z_LCASE:
            if letter_flags & (1 << (letter - A_LCASE)) != 0:
                return False
            letter_flags |= 1 << (letter - A_LCASE)
        elif A_UCASE <= letter <= Z_UCASE:
            if letter_flags & (1 << (letter - A_UCASE)) != 0:
                return False
            letter_flags |= 1 << (letter - A_UCASE)
    return True

# TODO: make the Eratostenes Sieve using this bit field aproach
# did it: test the bitfield to learn how to flag without dicts
# https://exercism.org/tracks/python/exercises/isogram/approaches/bitfield
