# list comprehension
def rotate(text, key):
    return ''.join(
        [
            chr(
                    (
                        (
                            ord(char)
                            -(dou := ord('A' if 'A' <= char <= 'Z' else 'a'))
                            + key
                        )
                        % 26
                    )
                    + dou
                )
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z'
            else char
            for char in text
        ]
    )

# str.maketrans
from string import ascii_lowercase
def rotate_maketrans(text, key):
    table = ascii_lowercase[key:] + ascii_lowercase[:key]
    trans = str.maketrans(table)
    return text.translate(trans)