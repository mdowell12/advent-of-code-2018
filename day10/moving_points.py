import time


POINT_PRESENT_CHAR = "#"
POINT_ABSENT_CHAR =  " "


def read_input_file(f):
    with open(f, 'r') as ff:
        return [i.strip() for i in ff.read().strip().split("\n")]


def find_message(raw_points):
    points = _parse_points(raw_points)
    # import pdb; pdb.set_trace()
    # Point.EXISTING_POINTS = set(points)
    Point.set_corners(points)
    # Slowly loop and print the board until human stops us
    while True:
        coords = tuple((p.current_x, p.current_y) for p in points)
        _print_grid(coords)
        for point in points:
            point.move()
        Point.set_corners(points)
        time.sleep(0.5)


def _print_grid(coords):
    xs = range(Point.MIN_X - 1, Point.MAX_X + 1)
    ys = range(Point.MIN_Y - 1, Point.MAX_Y + 1)

    for y in ys:
        # import/ pdb; pdb.set_trace()
        # line = [POINT_PRESENT_CHAR if Point.exists(x, y, points) else POINT_ABSENT_CHAR for x in xs]
        line = [POINT_PRESENT_CHAR if (x, y) in coords else POINT_ABSENT_CHAR for x in xs]
        # print "".join(line)
    print "grid corners (%s %s %s %s)" % (Point.MIN_X, Point.MAX_X, Point.MIN_Y, Point.MAX_Y)
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

    def __init__(self, start_x, start_y, dx, dy):
        self.current_x = start_x
        self.current_y = start_y
        self.dx = dx
        self.dy = dy

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

    @staticmethod
    def set_corners(points):
        Point.MIN_X = min(p.current_x for p in points)
        Point.MAX_X = max(p.current_x for p in points)
        Point.MIN_Y = min(p.current_y for p in points)
        Point.MAX_Y = max(p.current_y for p in points)

    def __repr__(self):
        return "Point[X: %s, Y: %s, dx: %s, dy: %s]" % (
            self.current_x, self.current_y, self.dx, self.dy
        )

if __name__ == "__main__":
    import sys
    f = sys.argv[1]
    points = read_input_file(f)
    find_message(points)
