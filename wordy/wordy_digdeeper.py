OPS = {
    "plus": "__add__",
    "minus": "__sub__",
    "multiplied by": "__mul__",
    "divided by": "__truediv__"
}


def answer(question):
    question = question.removeprefix("What is").removesuffix("?").strip()
    if not question: raise ValueError("syntax error")
    if question.isdigit(): return int(question)

    found_op = False
    for name, op in OPS.items():
        if name in question:
            question = question.replace(name, op)
            found_op = True
    if not found_op: raise ValueError("unknown operation")

    ret = question.split()
    while len(ret) > 1:
        try:
            x, op, y, *tail = ret
            if op not in OPS.values(): raise ValueError("syntax error")
            ret = [getattr(int(x), op)(int(y)), *tail]
        except Exception as e:
            raise ValueError("syntax error") from e
    return ret[0]