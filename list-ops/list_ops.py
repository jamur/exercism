def append(list1, list2):
    result_list = list1
    for item in list2:
        result_list += [item]
    return result_list

def concat(lists):
    result_list = []
    for list in lists:
        for item in list:
            result_list += [item]
    return result_list

def filter(function, list):
    result_list = []
    for item in list:
        if function(item):
            result_list += [item]
    return result_list

def length(list):
    sum = 0
    for _ in list:
        sum += 1
    return sum

def map(function, list):
    result_list = []
    for item in list:
        result_list += [function(item)]
    return result_list

def foldl(function, list, initial):
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    for item in list[::-1]:
        initial = function(initial, item)
    return initial

def reverse(list):
    result_list = []
    for item in list[::-1]:
        result_list += [item]
    return result_list
