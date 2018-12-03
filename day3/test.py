from overlap import calculate_overlap
from overlap import find_no_overlap


claims = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2",
]

expected = 4
actual = calculate_overlap(claims)

print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print


# Part 2

expected = "#3"
actual = find_no_overlap(claims)

print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print
