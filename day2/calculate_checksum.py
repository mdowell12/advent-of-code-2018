
def read_input_file(f):
    with open(f, 'r') as input:
        return input.read().strip().split('\n')


def calculate_checksum(box_ids):
    # Repeated letter occurrence counters, keyed by 
    # the number of times the repeated letter occurs
    acc = {2: 0, 3: 0}

    for box_id in box_ids:
        has_two, has_three = _count_repeats(box_id)
        if has_two: acc[2] += 1
        if has_three: acc[3] += 1
    
    return _checksum(acc)


def _count_repeats(box_id):
    has_two = False
    has_three = False

    counts = {}

    for letter in box_id:
        if has_two and has_three:
            break

        if letter not in counts:
            counts[letter] = 1
        else:
            counts[letter] += 1

    has_two = 2 in set(counts.values())
    has_three = 3 in set(counts.values())
    
    return has_two, has_three


def _checksum(acc):
    return acc[2] * acc[3]


if __name__ == "__main__":
    import sys
    f = sys.argv[1]

    box_ids = read_input_file(f)

    checksum = calculate_checksum(box_ids)

    print "Checksum:", checksum

