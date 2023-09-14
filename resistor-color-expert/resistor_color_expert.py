COLORS = "black brown red orange yellow green blue violet grey white"
COLORS_VALUE = {color: index for index, color in enumerate(COLORS.split())}
# COLORS_VALUE = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5,
#           "blue": 6, "violet": 7, "grey": 8, "white": 9}

TOLERANCES = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
              "brown": 1, "red": 2, "gold": 5, "silver": 15}

METRIC_PREFIXES = ["","kilo","mega","giga","tera","peta","exa","zetta","yotta","ronna","quetta"]

def resistor_label(colors):
    *ohms_colors, tolerance = colors
    if len(ohms_colors) < 1 and colors[0] == "black":
        return "0 ohms"
    ohms = label(ohms_colors)
    return f"{ohms} ±{TOLERANCES[tolerance]}%"

def label(colors):
    *number_color_list, zeros_color = colors
    # number = 0
    # for index, color in enumerate(number_color_list):
    #     number += COLORS_VALUE[color] * (10 ** (len(number_color_list) - index - 1))
    number = sum(
        COLORS_VALUE[color] * (10 ** (len(number_color_list) - index - 1))
        for index, color in enumerate(number_color_list)
        )
    zeros = COLORS_VALUE[zeros_color]
    number = float(str(number) + "0" * zeros)
    metric_prefix_multiplier = 0
    while number > 1000:
        number /= 1000
        metric_prefix_multiplier += 1
    formatted_number = f"{number:.0f}" if number.is_integer() else str(number)
    return formatted_number + f" {METRIC_PREFIXES[metric_prefix_multiplier]}ohms"
