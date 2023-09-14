import math
import time

# Função para medir o tempo de execução de uma função
def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

def find(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Evita estouro de inteiros

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    raise ValueError("value not in array")

def find2(search_list, value):
    if not search_list:
        raise ValueError("value not in array")

    index = len(search_list) // 2
    middle_value = search_list[index]
    if value > middle_value:
        return index + 1 + find(search_list[(index+1):], value)
    if value < middle_value:
        return find(search_list[:index], value)
    return index

def find3(search_list, value):
    len_sub = len(search_list)
    position =  len_sub - 1
    if len_sub == 0 or value > search_list[position] or value < search_list[0]:
        raise ValueError("value not in array")
    for _ in range(math.ceil(math.log2(len_sub)) + 2):
        if search_list[position] == value:
            return position
        len_sub //= 2
        if value < search_list[position]:
            position -= len_sub or 1
        else:
            position += len_sub or 1
    raise ValueError("value not in array")

if __name__ == "__main__":
    print(find(list(range(0,1500,5)), 1005))
    # Suas funções
    arr = list(range(0, 1500, 5))
    target = 1495

    # Medir o tempo para a primeira função
    result, elapsed_time = measure_time(find, arr, target)
    print(f"Tempo de execução para find: {elapsed_time} segundos")
    print(f"Resultado da busca: {result}")

    # Medir o tempo para a segunda função
    result, elapsed_time = measure_time(find2, arr, target)
    print(f"Tempo de execução para find2: {elapsed_time} segundos")
    print(f"Resultado da busca: {result}")

    # Medir o tempo para a terceira função
    result, elapsed_time = measure_time(find3, arr, target)
    print(f"Tempo de execução para find3: {elapsed_time} segundos")
    print(f"Resultado da busca: {result}")