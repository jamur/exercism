HAND_SHAKES = ['wink', 'double blink', 'close your eyes', 'jump']
def commands(binary_str):
    binary_str_reversed = binary_str[::-1]
    shakes = [shake for index, shake in enumerate(HAND_SHAKES)
                    if binary_str_reversed[index] == '1']
    return shakes if binary_str[0] != '1' else shakes[::-1]
