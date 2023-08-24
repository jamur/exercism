#!/usr/bin/env python3
"""
Unconvetional conversion
"""
import sys
import ast
from functools import reduce

def rebase(input_base, digits, output_base):
    """
    Convert unconventional base to unconventional base
    """
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if not all((0 <= int(d) < input_base) for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    def convert_to_base_ten(digits, input_base):
        return list(int(n) for n in list(str(sum(
                int(number) * input_base ** index
                for index, number
                in enumerate(digits[::-1])
            ))))

    def convert_from_base_ten(number, to_base):
        if number == [0]:
            return [0]
        # convert matrix to number ex: [1,0,1] to 101
        number = int(reduce(lambda d, nd: str(d) + str(nd), number))
        digits = []
        rest = number
        while rest > 0:
            digits.append(rest % to_base)
            rest = rest // to_base
        return digits[::-1]

    if output_base == 10:
        return convert_to_base_ten(digits, input_base)
    return convert_from_base_ten(
            convert_to_base_ten(digits, input_base), output_base
            )

if __name__ == "__main__":
    try:
        matrix = ast.literal_eval(sys.argv[2])
        if not isinstance(matrix, list):
            raise ValueError("O argumento não representa uma lista válida.")
    except (ValueError, SyntaxError):
        print("The second arguments isn't a valid list.")
        sys.exit(1)
    try:
        result_matrix  = rebase(int(sys.argv[1]), matrix, int(sys.argv[3]))
    except ValueError as e:
        print("Please beware this mistake: ", e)
    print(result_matrix)

