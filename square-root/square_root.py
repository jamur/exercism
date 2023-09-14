def square_root(n):
    return round(square_root_float(n))

def square_root_integer(n):
    c = 0
    d = 1 << 30

    while d:
        if n >= c + d:
            n -= c + d
            c = (c >> 1) + d
        else:
            c >>= 1
        d >>= 2
    return c

def square_root_float(n, epsilon=1e-10):
    x = n
    while True:
        next_x = (x + n / x) / 2
        if abs(x - next_x) < epsilon:
            return x
        x = next_x
    

#print(square_root(25))
print(square_root(1e12 + 7000))
