from chronal_charge import cell_power_level, find_max_grid

test_cells = [
    ((122, 79), 57, -5),
    ((217, 196), 39, 0),
    ((101, 153), 71, 4),
]

print "Testing power level calculations."
for case in test_cells:
    expected = case[2]
    actual = cell_power_level(case[0], case[1])

    print "Case:", case
    print "Expected:", expected
    print "Actual:", actual
    print "PASSED" if expected == actual else "FAILED"
    print

test_max_grid_inputs = [
    (18, (33, 45)),
    (42, (21, 61)),
]

print "Testing max grid calculations."
for case in test_max_grid_inputs:
    expected = case[1]
    actual, _ = find_max_grid(case[0], 3)

    print "Case:", case
    print "Expected:", expected
    print "Actual:", actual
    print "PASSED" if expected == actual else "FAILED"
    print
