from polymer import fully_collapsed_size, perform_reactions


data = [
    ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'),
    ('aA', ''),
    ('abBA', ''),
    ('abAB', 'abAB'),
    ('aabAAB', 'aabAAB'),
]

for d in data:
    expected = d[1]
    actual = perform_reactions(d[0])

    print "Case:", d[0]
    print "Expected:", expected
    print "Actual:", actual
    print "PASSED" if expected == actual else "FAILED"
    print


# Part 2

print "PART 2"
print

test_input = 'dabAcCaCBAcCcaDA'

expected = 4
actual = fully_collapsed_size(test_input)

print "Expected:", expected
print "Actual:", actual
print "PASSED" if expected == actual else "FAILED"
print
