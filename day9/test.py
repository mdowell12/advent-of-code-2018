from marbles import high_score


test_input = [
    (9, 25, 32),
    (10, 1618, 8317),
    (13, 7999, 146373),
    (17, 1104, 2764),
    (21, 6111, 54718),
    (30, 5807, 37305),
]

print "Part 1"

for case in test_input:
    expected = case[2]
    actual = high_score(case[0], case[1])

    print "Case:", case
    print "Expected:", expected
    print "Actual:", actual
    print "PASSED" if expected == actual else "FAILED"
    print
