from scheduler import find_order, task_duration


test_input = [
    "Step C must be finished before step A can begin.",
    "Step C must be finished before step F can begin.",
    "Step A must be finished before step B can begin.",
    "Step A must be finished before step D can begin.",
    "Step B must be finished before step E can begin.",
    "Step D must be finished before step E can begin.",
    "Step F must be finished before step E can begin.",
]

expected = "CABDFE"
actual = find_order(test_input)

print "Part 1"
print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print

expected = 15
actual = task_duration(test_input, 0, 2)

print "Part 2"
print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print
