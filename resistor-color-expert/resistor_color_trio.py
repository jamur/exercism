COLORS = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
          "blue": 6, "violet": 7, "grey": 8, "white": 9}

METRIC_PREFIXES = ["","kilo","mega","giga","tera","peta","exa","zetta","yotta","ronna","quetta"]

def label(colors):
    number = COLORS[colors[0]] * 10 + COLORS[colors[1]]
    zeros = COLORS[colors[2]]
    if number % 10 == 0:
        number = number // 10
        zeros += 1
    metric_prefix_multiplier, how_many_zeros = divmod(zeros, 3)
    return      f"{str(number) if number > 0 else ''}" \
            +   f"{'0' * how_many_zeros} " \
            +   f"{METRIC_PREFIXES[metric_prefix_multiplier]}ohms"
    
