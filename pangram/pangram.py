from string import ascii_lowercase
from timeit import timeit
import re

ALPHABET = set(ascii_lowercase)

# measuring performance
# do:
# pytest -s
# to see the prints
TIMES = 1000
def decor(func):
    def wrapper(arg):
        time_join_re = timeit(lambda: func(arg), number = TIMES)
        time_all = timeit(lambda: is_pangram_better_aproach(arg),number = TIMES )
        time_all_casefold = timeit(lambda: is_pangram_better_aproach_casefold(arg),number = TIMES )
        time_set = timeit(lambda: is_pangram_set(arg),number = TIMES )
        # Calculate the percentage difference
        #percent_faster = ((time_all - time_join_re) / time_all) * 100
        percent_faster = ((time_join_re - time_all) / time_all) * 100
        percent_faster_casefold = ((time_all - time_all_casefold) / time_all) * 100
        percent_set = ((time_all - time_set) / time_all) * 100

        print()
        print(f'\033[90mTime with all:\033[0m          {time_all:.9f}')
        print(f'\033[90mTime with join and re:\033[0m  {time_join_re:.9f}')
        print(f'\033[90mFunction with all is\033[0m                 {percent_faster:.2f}% \033[90mfaster than with join and re\033[0m')
        print(f'\033[90mTime all with casefold:\033[0m {time_all_casefold:.9f} \033[90m(bonus)\033[0m')
        print(f'\033[90mFunction with all and case fold is\033[0m   {percent_faster_casefold:.2f}% \033[90mfaster than with all.lower\033[0m')
        print(f'\033[90mTime with set:\033[0m          {time_set:.9f}')
        print(f'\033[90mFunction with set is\033[0m                 {percent_set:.2f}% \033[90mfaster than with all\033[0m')

        # call function and get the result
        return func(arg)
    return wrapper

# my version
@decor
def is_pangram(sentence: str) -> bool:
    alphabet = ''.join(chr(i) for i in range(ord('a'), ord('z') + 1))
    return set(re.sub(r'[^a-z]', '', sentence.lower())) == set(alphabet)

def is_pangram_better_aproach(sentence: str) -> bool:
    return all(letter in sentence.lower() for letter in ascii_lowercase)

def is_pangram_better_aproach_casefold(sentence: str) -> bool:
    return all(letter in sentence.casefold() for letter in ascii_lowercase)

# Tanhan Solution
# https://exercism.org/tracks/python/exercises/pangram/solutions/Tahnan
def is_pangram_set(string):
    return ALPHABET.issubset(string.lower())
