from license import find_value
from license import sum_metadata


test_input = ['2', '3', '0', '3', '10', '11', '12', '1', '1', '0', '1', '99', '2', '1', '1', '2']

expected = 138
actual = sum_metadata(test_input)

print "Part 1"
print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print

expected = 66
actual = find_value(test_input)

print "Part 2"
print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print
