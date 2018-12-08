from chronal import largest_area
from chronal import safe_zone


test_input = [
    "1, 1",
    "1, 6",
    "8, 3",
    "3, 4",
    "5, 5",
    "8, 9",
]

expected = 17
actual = largest_area(test_input)

print "Part 1"
print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print

expected = 16
actual = safe_zone(test_input, 32)

print "Part 2"
print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print
