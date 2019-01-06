import time

SQUARE_WIDTH = 300


def find_max_grid_any_sub_grid_size(serial_number):
    # (grid_size, (top_left_x, top_left_y), power)
    best = None
    for sub_grid_size in range(1, SQUARE_WIDTH + 1):
        start = time.time()
        max_grid_coord, power = find_max_grid(serial_number, sub_grid_size)
        if best is None or power > best[-1]:
            best = (sub_grid_size, max_grid_coord, power)

        print "Finished calculating for sub grid size " + str(sub_grid_size) + " took " + str(time.time() - start) + "s"

    return best[1], best[0]


def find_max_grid(serial_number, sub_grid_size):
    coord_to_power_level = {coord: cell_power_level(coord, serial_number)
                            for coord in _coord_generator()}

    # _print_power_levels(coord_to_power_level)

    best_coord_so_far = (None, None)
    best_power_so_far = None

    coords_to_try = [c for c in _coord_generator()
                     if c[0] <= SQUARE_WIDTH - (sub_grid_size - 1)
                     and c[1] <= SQUARE_WIDTH - (sub_grid_size - 1)]

    for top_left in coords_to_try:
        sub_grid_power = _total_subgrid_power(
            top_left,
            coord_to_power_level,
            sub_grid_size
        )
        if best_coord_so_far is None or \
                best_power_so_far is None or \
                sub_grid_power > best_power_so_far:

            best_coord_so_far = top_left
            best_power_so_far = sub_grid_power

    return best_coord_so_far, best_power_so_far


def _total_subgrid_power(top_left, coord_to_power_level, sub_grid_size):
    start_x, start_y = top_left

    sub_grid_coords = ((x, y) for x in range(start_x, start_x + sub_grid_size) \
        for y in range(start_y, start_y + sub_grid_size))

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
    max_grid_upper_left = find_max_grid(4151, 3)
    print "Part 1 max grid:", max_grid_upper_left

    part_2_best = find_max_grid_any_sub_grid_size(4151)
    print "Part 2 max grid with sub grid size:", part_2_best
