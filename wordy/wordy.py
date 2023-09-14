'''
Without eval and recursive
'''
# TODO: dig deeeper
import re

OPERAND = r'^ *(-*\d+) *'

def answer(question: str) -> float:
    question = question.casefold()
    if question.startswith("what is"):
        question = re.sub(r'^what is', '', question)
        match = re.match(OPERAND, question)
        if match:
            initial_operand = int(match.group(1))
        else:
            raise ValueError('syntax error') # erro de não ter um número
        question = re.sub(OPERAND, '', question)
        return calculate(question, initial_operand)
    raise ValueError('unknown operation')

OPERATIONS = {'plus': '__add__', 'minus': '__sub__', 'divided by': '__truediv__', 'multiplied by': '__mul__'}
OPERATION = r'^ *([a-z]+\s*(by)?) *'

def calculate(question, initial_operand):
    if question == '?':
        return initial_operand
    match = re.match(OPERATION, question)
    if match:
        sign_word = match.group(1).strip()
        if sign_word in OPERATIONS:
            operator = OPERATIONS[sign_word]
            question = re.sub(OPERATION, '', question)
            # find second operand
            match = re.match(OPERAND, question)
            if match:
                operand = match.group(1)
                question = re.sub(OPERAND, '', question)
                result = getattr(initial_operand, operator)(int(operand))
                return calculate(question, result)
            raise ValueError('syntax error')
        raise ValueError('unknown operation')
    raise ValueError('syntax error')

if __name__ == "__main__":
    print(answer('What is 5 plus 3 plus 2 multiplied by 3 divided by 2 multiplied by 2?'))
