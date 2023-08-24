def score(x, y):
    hypotenuse = (x ** 2 + y ** 2) ** .5
    return  10  if hypotenuse <= 1  \
        else 5  if hypotenuse <= 5  \
        else 1  if hypotenuse <= 10 \
        else 0
  
def scoreb(x, y):
    return ((rr := x * x + y * y) <= 100) + 4 * (rr <= 25) + 5 * (rr <= 1)
