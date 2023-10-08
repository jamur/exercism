class Luhn:
    def __init__(self, card_num):
        self.is_valid = self.__class__.is_valid_luhn(card_num)

    def valid(self):
        return self.is_valid

    @staticmethod
    def luhny_tune(digit: str) -> int:
        return dbl - 9 if (dbl := int(digit) * 2) > 9 else dbl
    @staticmethod
    def is_valid_luhn(num):
        num = num.replace(' ', '')
        if len(num) < 2:
            return False
        if not num.isdigit():
            return False
        sum_digits = \
            sum(
                Luhn.luhny_tune(digit) # even positions, double: if > 9, -9
                if idx % 2
            else
                int(digit)             # odd positions: same number
            for idx, digit in enumerate(reversed(num))
            )
        return not sum_digits % 10
