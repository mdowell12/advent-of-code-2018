from calculate_checksum import calculate_checksum
from similar_ids import find_similar_ids


box_ids = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
]

expected = 12
actual = calculate_checksum(box_ids)

print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print

# Part 2
box_ids = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz",
]

expected = 'fgij'
actual = find_similar_ids(box_ids)

print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print

