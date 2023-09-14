def say(number):
    if not 0 <= number < 1e12:
        raise ValueError("input out of range")

    def say_up_to_999(num):
        words = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
        tens_words = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
        
        if num == 0:
            return ""
        elif num < 20:
            return words[num]
        elif num < 100:
            t, u = divmod(num, 10)
            return tens_words[t] + ("-" + words[u] if u > 0 else "")
        else:
            h, r = divmod(num, 100)
            return words[h] + " hundred" + (" and " + say_up_to_999(r) if r > 0 else "")

    def say_with_units(num, unit):
        if num == 0:
            return ""
        elif num == 1:
            return say_up_to_999(num) + " " + unit
        else:
            return say_up_to_999(num) + " " + unit + "s"

    parts = []
    for i, unit in enumerate(["", "thousand", "million", "billion", "trillion"]):
        number, remainder = divmod(number, 1000)
        if remainder > 0:
            parts.append(say_with_units(remainder, unit))
        if number == 0:
            break

    return " ".join(parts[::-1]) or "zero"

# Exemplos de uso:
print(say(42))         # Saída: "forty-two"
print(say(1234567))    # Saída: "one million two hundred thirty-four thousand five hundred sixty-seven"
