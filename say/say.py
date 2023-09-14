UNITS = 'zero one two three four five six seven eight nine'.split()
ELEVENS = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
MULT = 'thousand million billion trillion'.split()
MULT.insert(0, '')

def say_up_to_99(number):
    ''' say numbers up to 99 '''
    if 1 <= number <= 9:
        return UNITS[number]
    if 10 <= number <= 19:
        return ELEVENS[number % 10]
    quotient, remainder = divmod(number, 10)
    if quotient == 0:
        return ''
    to_say = TENS[quotient]
    if remainder:
        to_say += '-' + UNITS[remainder]
    return to_say

def say_up_to_999(number):
    ''' say numbers up to 999 '''
    if number == 0:
        return 'zero'
    if 1 <= number <= 9:
        return UNITS[number]
    if 10 <= number <= 19:
        return ELEVENS[number % 10]
    if 20 <= number <= 99:
        return say_up_to_99(number)
    if 100 <= number <= 999:
        centena, dezena = divmod(number, 100)
        space = ' ' if dezena > 0 else ''
        return UNITS[centena] + ' hundred' + space + say_up_to_99(dezena)

def say(number):
    if not 0 <= number < 1_000_000_000_000:
        # if the number is negative or too big
        raise ValueError("input out of range")
    to_say, _ = say_inner(number)
    return to_say

def say_inner(number, mult=0):
    # base case
    if number < 1000:
        to_say = say_up_to_999(number)
        if mult:
            to_say += ' ' + MULT[mult]
        return to_say, True # True mark the last iteration
    quotient, remainder = divmod(number, 1000)
    to_say = ''
    if quotient:
        to_say, last = say_inner(quotient, mult + 1)
    if remainder:
        if not last:
            to_say +=  ' ' + MULT[mult + 1]
        to_say += ' ' + say_inner(remainder)[0]
    return to_say, False # False marks not the last iteration

if __name__ == '__main__':
    for number in [2000000,1000,987_654_321_123, 1_000_001_000]:
        print(number, say(number))









'''
def say(number):
    # if the number is negative or too big
    if not 0 <= number <= 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return 'zero'
    return say_to_infinite(number)
    

    if number < 1000:
        return say_to_999(number)
    if 1000 <= number < 1_000_000:
        quocient, remainder = divmod(number, 1000)
        if quocient:
            to_say = say_to_999(quocient) + ' ' + MULT[1]
        if remainder > 0:
            to_say += ' ' + say_to_999(remainder)
        #space = ' ' if remainder > 0 else ''
        #return  say_to_999(quocient) + ' ' + MULT[1] + space + say_to_999(remainder)
        return to_say
    if 1_000_000 <= number < 1_000_000_000:
        quocient, remainder = divmod(number, 1_000_000)
        if quocient:
            to_say =  say_to_999(quocient) + ' ' + MULT[2]
        if 0 < remainder < 1000:
            to_say += ' ' + say_to_999(remainder)
        quocient, remainder = divmod(remainder, 1_000)
        if quocient:
            to_say += ' ' + say_to_999(quocient) + ' ' + MULT[1]
        if remainder:
            to_say += ' ' + say_to_999(remainder)
        return to_say
    if 1_000_000_000 <= number < 1_000_000_000_000:
        quocient, remainder = divmod(number, 1_000_000_000)
        to_say =  say_to_999(quocient) + ' ' + MULT[3]
        quocient, remainder = divmod(remainder, 1_000_000)
        if quocient:
            to_say += ' ' + say_to_999(quocient) + ' ' + MULT[2]
        if 0 < remainder < 1000:
            to_say += ' ' + say_to_999(remainder)
        quocient, remainder = divmod(remainder, 1_000)
        if quocient:
            to_say += ' ' + say_to_999(quocient) + ' ' + MULT[1]
        if remainder:
            to_say += ' ' + say_to_999(remainder)
        return to_say
'''
