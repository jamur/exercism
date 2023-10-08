class Luhn:
    def __init__(self, card_num):
        self.isValid = Luhn.luhny_bin(0, 0, list(card_num[::-1]))

    def valid(self):
        return self.isValid

    @staticmethod
    def luhny_tune(num):
        return dbl - 9 if (dbl := 2 * num) > 9 else dbl

    @staticmethod
    def luhny_bin(pos, sum, chars):
        if not chars:
            return pos > 1 and sum % 10 == 0
        else:
            head, *tail = chars
            if head.isdigit():
                if not pos % 2:
                    return Luhn.luhny_bin(pos + 1, sum + int(head), tail)
                return Luhn.luhny_bin(pos + 1, sum + Luhn.luhny_tune(int(head)), tail)
            if head == " ":
                return Luhn.luhny_bin(pos, sum, tail)
            return False