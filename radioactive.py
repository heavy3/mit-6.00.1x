def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    expose = 0
    while start < stop:
        expose += f(start) * step
        start += step
    return expose

print radiationExposure(0, 5, 1)
