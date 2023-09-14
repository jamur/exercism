def flatten(iterable):
    '''only to give a list from an iterable'''
    return list(flatten_helper(iterable))

def flatten_helper(iterable):
    '''recursively take items or other iterables'''
    for item in iterable:
        if _is_iterable(item):
            yield from flatten(item)
        else:
            if item is not None:
                yield item

# permit other iterables than tuple and list, as sets and dicts
def _is_iterable(item):
    return hasattr(item, '__iter__') and not isinstance(item, (str, bytes))

def flatten_list(iterable):
    result = []
    for item in iterable:
        if isinstance(item, list):
            result += flatten(item)
        else:
            if item is not None:
                result.append(item)
    return result

def flatten_myversion(iterable):
    result = []
    inside(result, iterable)
    return result

def inside(result, iterable):
    for item in iterable:
        if isinstance(item, list):
            inside(result, item)
        else:
            if item is not None:
                result.append(item)

# only works with the complete function (the first one)
if __name__ == '__main__':
    print(flatten([1,2,{3,2},{'oi': 3, 'nada': 0}, [1,[3,[5,7]]],10,[[[[[[[[[[[[11]]]]]]]]]]]]]))