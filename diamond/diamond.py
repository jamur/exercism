from string import ascii_uppercase

def rows(letter):
    to_index = ascii_uppercase.index(letter) + 1
    length = (to_index * 2) - 1
    diamond = [f'{"A":^{length}}']
    for spaces, letter_it in zip(range(1, to_index * 2, 2), ascii_uppercase[1:to_index]):
        diamond_slice = f'{letter_it}{" " * spaces}{letter_it}'
        diamond += [f'{diamond_slice:^{length}}']
    diamond += diamond[:-1][::-1]
    return diamond

