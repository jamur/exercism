OPENERS = '[{('
CLOSERS = ']})'

def is_paired(input_string):
    hugs = []
    for char in input_string:
        if char in OPENERS:
            hugs += char
        elif char in CLOSERS:
            if hugs and hugs[-1] == OPENERS[CLOSERS.index(char)]:
                hugs.pop()
            else:
                return False
    if hugs:
        return False
    return True


print(is_paired('(ao[aoeu]90909{a}x)ouaouo[oaeuao(u{aoeu})u]'))
print(is_paired('o(e)O(O[Uooo])i'))


# def is_paired(input_string):
#     matched = True
#     next_closer = len(input_string) - 1
#     for c, l in enumerate(input_string):
#         opened = False
#         if l in OPENERS:
#             opened = True
#             for cc in range(next_closer, c, -1):
#                 if input_string[cc] in CLOSERS:
#                     if OPENERS.index(l) == CLOSERS.index(input_string[cc]):
#                         opened = False
#                     else:
#                         matched = False
#                     next_closer = cc - 1
#                     break
#                 next_closer = cc - 1
#             if not matched:
#                 break
#         elif l in CLOSERS:
#             matched = False
#             break
#         if next_closer <= c:
#             matched = not opened
#             break
#     return matched