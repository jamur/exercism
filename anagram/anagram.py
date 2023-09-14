def find_anagrams(word, candidates):
    return [candidate for candidate in candidates
            if sorted(word.casefold()) == sorted(candidate.casefold())
            and word.casefold() != candidate.casefold()]
    # return filter(lambda candidate:
    #               sorted(word.casefold()) == sorted(candidate.casefold())
    #               and word.casefold() != candidate.casefold(),
    #               candidates)
