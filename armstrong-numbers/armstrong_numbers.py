def is_armstrong_number(number):
    return number == sum(int(num_str) ** len(str(number))
                         for num_str in str(number))
