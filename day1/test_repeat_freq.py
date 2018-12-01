from repeat_freq import find_first_repeat


def _run_test(test_input, expected, actual):
    print "For input", test_input
    print "Expected:", expected
    print "Actual:  ", actual
    print "PASSED" if expected == actual else "FAILED"
    print

test_inputs = [
    (["+1", "-1"], 0),
    (["+3","+3","+4","-2","-4"], 10),
    (["-6","+3","+8","+5","-6"], 5),
    (["+7","+7","-2","-7","-4"], 14),
]

for i, expected in test_inputs:
    result = find_first_repeat(i)
    _run_test(i, expected, result)


