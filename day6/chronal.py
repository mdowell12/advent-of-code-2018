import itertools


def read_input_file(f):
    with open(f, 'r') as input:
        return input.read().strip().split('\n')


def largest_area(raw_coordinates):
    """
    1) Find the corners of the rectangular grid by doing cartesian products of min/max x and y
       From this, we know if a point is on the border of the grid when its x or y coord is equal
       to that of one of the corners.
    2) For each point in the grid, calculate who is closest to it, incrementing a counter for the
       coordinate who it turns out is closest.
    3) For each point on the border, remove the coordinate who is closest to that point, because
       such coordinates have infinite area
    4) Sort by the remaining counters and return the coordinate with largest area.
    """
    coordinates = _parse_coordinates(raw_coordinates)
    min_x, max_x, min_y, max_y = _find_corners(coordinates)
    
    grid = [i for i in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1))]
   
    # Maps a point on the grid to the coordinate closest to it
    closest_coords = {p: _find_closest_coord(p, coordinates) for p in grid}
    
    # Aid in debugging
    _print_grid(grid, closest_coords)

    counts = {}
    for point in grid:
        closest = closest_coords[point]
        if closest not in counts:
            counts[closest] = 0
        counts[closest] += 1

    # Remove any coordinates whose area is on the border of the grid
    border_points = [p for p in grid if p[0] in {min_x, max_x} or p[1] in {min_y, max_y}]
    for point in border_points:
        coord = closest_coords[point]
        if coord in counts:
            del counts[coord]

    max_area = max(counts.values())

    return max_area

def _find_closest_coord(point, coordinates):
    # Maps a distance to a set of coords who are that distance from the point
    distances = {}
    for coord in coordinates:
        distance = _manhattan_dist(point, coord)
        if distance not in distances:
            distances[distance] = []
        distances[distance].append(coord)
    
    min_dist = min(distances.keys())
    min_coords = distances[min_dist]
    # Return (-1, -1) if there is a tie
    return min_coords[0] if len(min_coords) == 1 else (-1, -1)


def _manhattan_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def _print_grid(grid, closest_coords):
    xs = sorted(set(i[0] for i in grid))
    ys = sorted(set(i[1] for i in grid))
    for y in ys:
        print "  ".join(str(closest_coords[(x, y)]) for x in xs)
        print


def _find_corners(coordinates):
    min_x = min(p[0] for p in coordinates)
    max_x = max(p[0] for p in coordinates)
    min_y = min(p[1] for p in coordinates)
    max_y = max(p[1] for p in coordinates)

    return min_x, max_x, min_y, max_y


def _parse_coordinates(raw_coordinates):
    coords = []
    for i in raw_coordinates:
        parts = i.split(",")
        coords.append((int(parts[0]), int(parts[1])))
    return coords


if __name__ == "__main__":
    import sys

    coordinates = read_input_file(sys.argv[1])

    largest_area = largest_area(coordinates)
    print "Largest area:", largest_area

