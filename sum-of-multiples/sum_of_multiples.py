from functools import reduce
def sum_of_multiples(limit, multiples):
    return  sum(
                # reduce returns a set, then sum
                reduce(
                    # This is the function to sum sets
                    # leveraging the property of removing duplicates
                    lambda it1, it2: set(it1) | set(it2),
                    # iterator
                    (
                        # generates ranges of the multiples
                        range(multiple, limit, multiple) if multiple > 0 else [] # avoids error in range
                        for multiple in multiples
                    )
                )
                if multiples else [] # No multiples: sum = 0
            ) #\
            #if multiples else 0 # No multiples: sum = 0

# apalala's solution
# https://exercism.org/tracks/python/exercises/sum-of-multiples/solutions/apalala
def sum_of_multiples_apalalas(limit, multiples):
    return  sum(
        {
            i
            for number in multiples if number # don't take 0 multiplier
            for i in range(number, limit, number)
        }
    )
