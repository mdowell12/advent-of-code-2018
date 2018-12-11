
SQUARE_WIDTH = 300
SUB_GRID_WIDTH = 3


def find_max_grid(serial_number):
    coord_to_power_level = {coord: cell_power_level(coord, serial_number) \
        for coord in _coord_generator()}

    # _print_power_levels(coord_to_power_level)

    # Coord to total sub grid power
    highest_so_far = (None, None)

    coords_to_try = [c for c in _coord_generator() \
        if c[0] <= SQUARE_WIDTH - (SUB_GRID_WIDTH - 1) and c[1] <= SQUARE_WIDTH - (SUB_GRID_WIDTH - 1)]

    for top_left in coords_to_try:
        sub_grid_power = _total_subgrid_power(top_left, coord_to_power_level)
        if highest_so_far[0] is None or sub_grid_power > highest_so_far[1]:
            highest_so_far = (top_left, sub_grid_power)

    return highest_so_far[0]


def _total_subgrid_power(top_left, coord_to_power_level):
    start_x, start_y = top_left

    sub_grid_coords = ((x, y) for x in range(start_x, start_x + SUB_GRID_WIDTH) \
        for y in range(start_y, start_y + SUB_GRID_WIDTH))

    powers = [coord_to_power_level[coord] for coord in sub_grid_coords]

    return sum(powers)


def _coord_generator():
    return ((x, y) for x in range(1, SQUARE_WIDTH + 1) for y in range(1, SQUARE_WIDTH + 1))


def _print_power_levels(coord_to_power_level):
    for y in sorted(set(p[1] for p in coord_to_power_level.keys())):
        xs = [x for x in sorted(set(p[0] for p in coord_to_power_level.keys()))]
        power_levels = [str(coord_to_power_level[(x, y)]) for x in xs]
        print " ".join(" " + i if len(i) == 1 else i for i in power_levels)

def cell_power_level(coordinate, serial_number):
    x, y = coordinate
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level = int(str(power_level)[-3]) if len(str(power_level)) >= 3 else 0
    return power_level - 5


if __name__ == "__main__":
    max_grid_upper_left = find_max_grid(4151)
    print "Max grid:", max_grid_upper_left
