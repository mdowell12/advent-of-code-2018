import time


def read_input_file(f):
    with open(f, 'r') as ff:
        return [i.strip() for i in ff.read().strip().split("\n")]


def find_message(raw_points):
    points = _parse_points(raw_points)
    # import pdb; pdb.set_trace()
    # Point.EXISTING_POINTS = set(points)

    # Slowly loop and print the board until human stops us
    while True:
        _print_grid(points)
        for point in points:
            point.move()
        time.sleep(1)


def _print_grid(points):
    xs = range(Point.MIN_X - 1, Point.MAX_X + 1)
    ys = range(Point.MIN_Y - 1, Point.MAX_Y + 1)

    for y in ys:
        line = ["#" if Point.exists(x, y, points) else "." for x in xs]
        print "".join(line)

    print
    print


def _parse_points(raw_points):
    parsed = []
    for line in raw_points:
        parts = [int(i) for i in line.replace('position=<', '')
                                     .replace('>', '')
                                     .replace('velocity=<', '')
                                     .replace(',', ' ')
                                     .split(' ') if i]
        parsed.append(Point(
            parts[0],
            parts[1],
            parts[2],
            parts[3]
        ))
    return parsed


class Point(object):

    MIN_X = None
    MAX_X = None
    MIN_Y = None
    MAX_Y = None

    EXISTING_POINTS = set()

    def __init__(self, start_x, start_y, dx, dy):
        self.current_x = start_x
        self.current_y = start_y
        self.dx = dx
        self.dy = dy
        self._set_min_max_class_vals()

    @staticmethod
    def exists(x, y, points):
        for point in points:
            if x == point.current_x and y == point.current_y:
                return True
        return False
        # return point in Point.EXISTING_POINTS

    def move(self):
        self.current_x += self.dx
        self.current_y += self.dy
        # self._set_min_max_class_vals()

    def _set_min_max_class_vals(self):
        Point.MIN_X = min(self.current_x, Point.MIN_X) if Point.MIN_X is not None else self.current_x
        Point.MAX_X = max(self.current_x, Point.MAX_X) if Point.MAX_X is not None else self.current_x
        Point.MIN_Y = min(self.current_y, Point.MIN_Y) if Point.MIN_Y is not None else self.current_y
        Point.MAX_Y = max(self.current_y, Point.MAX_Y) if Point.MAX_Y is not None else self.current_y

    def __repr__(self):
        return "Point[X: %s, Y: %s, dx: %s, dy: %s]" % (
            self.current_x, self.current_y, self.dx, self.dy
        )

if __name__ == "__main__":
    import sys
    f = sys.argv[1]
    points = read_input_file(f)
    find_message(points)
