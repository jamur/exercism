'''
Fórmulas from Toravasaari solution
https://exercism.org/tracks/python/exercises/difference-of-squares/solutions/toravasaari
my solution commented
'''
def square_of_sum(number):
    return (number * (number + 1) // 2) ** 2
    #return sum(range(number + 1)) ** 2


def sum_of_squares(number):
    return number * (number + 1) * (2 * number + 1) // 6
    #return sum(base ** 2 for base in range(number + 1))


def difference_of_squares(number):
    return number * (number + 1) * (3 * number ** 2 - number - 2) // 12
    #return square_of_sum(number) - sum_of_squares(number)

