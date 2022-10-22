def gp_generator():
    """Генератор для вычисления геометрической прогресии"""
    f = 5
    d = 6
    p = 6
    while p > 1:
        p -= 1
        f = f * d
        yield f


gp_generator()
my_gen = gp_generator()
print(list(my_gen))