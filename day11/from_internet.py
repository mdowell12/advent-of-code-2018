import numpy
serial = int(4151)


def power(x, y):
    rack = (x + 1) + 10
    power = rack * (y + 1)
    power += serial
    power *= rack
    return (power // 100 % 10) - 5


def max_grid(width):
    windows = sum(grid[x:x-width+1 or None, y:y-width+1 or None] for x in range(width) for y in range(width))
    import pdb; pdb.set_trace()
    maximum = int(windows.max())
    location = numpy.where(windows == maximum)
    return location, maximum


grid = numpy.fromfunction(power, (300, 300))

# for width in range(3, 300):
for width in [3]:
    location, maximum = max_grid(width)
    print(width, maximum, location[0][0] + 1, location[1][0] + 1)
