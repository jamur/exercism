import re

def is_valid(isbn: str) -> bool:
    match = re.match(r'^(\d)[-\s]?(\d{3})[-\s]?(\d{5})-?([\dX])$', isbn)
    if match:
        digits = list(''.join(match.groups()))
        if digits[-1] == 'X': digits[-1] = 10
        return not sum(int(d)*m for d,m in zip(digits,range(10,0,-1))) % 11
    return False
