'''
Say numbers in english
'''
# Define lists for number representations
UNITS = 'zero one two three four five six seven eight nine'.split()
ELEVENS = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
MULT = ['', 'thousand', 'million', 'billion', 'trillion']

# Convert numbers from 1 to 99 into textual representation
def say_up_to_99(number):
    '''
    Convert a number from 1 to 99 into its textual representation.
    '''
    if 0 <= number <= 9:
        return UNITS[number]
    if 10 <= number <= 19:
        return ELEVENS[number % 10]
    quotient, remainder = divmod(number, 10)
    if remainder:
        return TENS[quotient] + '-' + UNITS[remainder]
    return TENS[quotient]

# Convert numbers from 1 to 999 into textual representation
def say_up_to_999(number):
    '''
    Convert a number from 1 to 999 into its textual representation.
    '''
    if 0 <= number <= 99:
        return say_up_to_99(number)
    if 100 <= number <= 999:
        centena, dezena = divmod(number, 100)
        if dezena == 0:
            return UNITS[centena] + ' hundred'
        return UNITS[centena] + ' hundred' + ' ' + say_up_to_99(dezena)

# Main function to convert a number into textual representation
def say(number):
    '''
    Convert a number into its textual representation.
    '''
    if not 0 <= number < 1e12:
        # no negative or too big numbers
        raise ValueError("input out of range")
    to_say = say_inner(number)
    return to_say

# Recursive helper function for numbers with multiple units (thousands, millions, etc.)
def say_inner(number, mult=0):
    '''
        Convert a number with multiple units (thousands, millions, etc.)
    into its textual representation.
    '''
    # base case
    if number < 1000:
        to_say = say_up_to_999(number)
        if number and mult:
            to_say += ' ' + MULT[mult]
        return to_say

    quocient, remainder = divmod(number, 1000)

    to_say = ''

    if quocient:
        to_say = say_inner(quocient, mult + 1)

    if remainder:
        to_say += ' ' + say_inner(remainder, mult)

    return to_say

























































# test
if __name__ == '__main__':
    for number in [0, 2000001, 2_000_010_000, 1_000_001_000, 2_001_001_001,
                   100000, 987654321123]:
        print(number, say(number))











# historic
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

#if (remainder * 10 ** (mult * 3)) >= (1 * 10 ** ((mult + 1) * 3)):


    # adds mult word only if doesn't have one
    # if to_say.split()[-1] not in MULT:
    #     to_say +=  ' ' + MULT[mult + 1]
