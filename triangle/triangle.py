def valid_triangle(f):
    def inner(sides):
        less_long, middle_lenght, larger = sorted(sides)
        return larger < less_long + middle_lenght and f(sides)
    return inner

@valid_triangle
def equilateral(sides):
    return len(sides_set := set(sides)) == 1 and sides_set != {0}

@valid_triangle
def isosceles(sides):
    return len(set(sides)) in (1,2)

@valid_triangle
def scalene(sides):
    return len(set(sides)) == 3
