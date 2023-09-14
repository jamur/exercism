def square_root_(n):
    c = 0
    d = 1 << 30

    while d:
        print(c)
        if n >= c + d:
            n -= c + d
            c = (c >> 1) + d
        else:
            c >>= 1
        d >>= 2
    return c

def square_root(n, epsilon=1e-10):
    x = n / 10
    while True:
        print(x)
        next_x = (x + n / x) / 2
        if abs(x - next_x) < epsilon:
            return x
        x = next_x
    

print(square_root(1000))
print(square_root_(1000))
