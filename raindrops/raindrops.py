def convert(number):
    # factors and words
    songs = {3: "Pling", 5: "Plang", 7: "Plong"}
    # generator to add a word if is factor
    filter_number = (word for factor, word in songs.items()
                  if not number % factor)
    # join the words about factors
    say = "".join(filter_number)
    # if there are (or there is) word(s) return it, if not
    # (no factor found), return the number
    return say or str(number)
