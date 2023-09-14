UNITS = 'zero one two three four five six seven eight nine'.split()
ELEVENS = 'ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
MULT = ['', 'thousand', 'million', 'billion', 'trillion']

def say(number):
    if not 0 <= number < 1e12:
        raise ValueError("input out of range")

    def say_up_to_999(number):
        if number < 10:
            return UNITS[number]
        elif number < 20:
            return ELEVENS[number - 10]
        elif number < 100:
            t, u = divmod(number, 10)
            return TENS[t] + ('-' + UNITS[u] if u > 0 else '')
        else:
            h, r = divmod(number, 100)
            return UNITS[h] + ' hundred' + (' ' + say_up_to_999(r) if r > 0 else '')

    parts = []
    for i in range(3):
        number, remainder = divmod(number, 1000)
        if remainder > 0:
            parts.append(say_up_to_999(remainder) + (' ' + MULT[i] if i > 0 else ''))
        if number == 0:
            break

    return ' '.join(parts[::-1]) or 'zero'

# Exemplos de uso:
print(say(42))         # Saída: "forty-two"
print(say(1234567))    # Saída: "one million two hundred thirty-four thousand five hundred sixty-seven"
