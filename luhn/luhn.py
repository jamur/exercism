class Luhn:
    def __init__(self, card_num):
        self.is_valid = self.__class__.is_valid_luhn(card_num)

    def valid(self):
        return self.is_valid

    @staticmethod
    def is_valid_luhn(num):
        num = num.replace(' ', '')
        if len(num) < 2:
            return False
        if not num.isdigit():
            return False
        sum_digits = \
            sum(
                dbl - 9         # even positions, double: if > 9, -9
                if idx % 2 and (dbl := int(digito) * 2) > 9
            else
                dbl             # even positions, double <= 9
                if idx % 2
            else
                int(digito)     # odd positions: same number
            for idx, digito in enumerate(reversed(num))
            )
        return not sum_digits % 10
