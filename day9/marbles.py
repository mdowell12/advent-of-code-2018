

def high_score(num_players, last_marble):
    scores = {i: 0 for i in range(1, num_players + 1)}
    ring = [0]
    current_player = scores.keys()[0]
    current_marble = 0

    print "[-] (0)"
    # import pdb; pdb.set_trace()
    for marble in xrange(1, last_marble + 1):
        if marble % 23 == 0:
            ring, current_marble, score_to_add = _do_the_23(ring, marble, current_marble)
            scores[current_player] += score_to_add
        else:
            ring = _add_marble(marble, current_marble, ring)
            current_marble = marble

        # _print_board(current_player, current_marble, ring)
        current_player = _next_player(current_player, scores.keys())

    return sorted(scores.values())[-1]


def _do_the_23(ring, marble, current_marble):
    to_remove = _find_index(ring, ring.index(current_marble), 7, clockwise=False)
    next_current_marble_index = _find_index(ring, to_remove, 1, clockwise=True)
    next_current_marble = ring[next_current_marble_index]
    removed = ring.pop(to_remove)

    return ring, next_current_marble, marble + removed

def _add_marble(marble, current_marble, ring):
    current_marble_index = ring.index(current_marble)
    index = _find_index(ring, current_marble_index, 2)
    ring.insert(index, marble)
    return ring


def _find_index(ring, start, n, clockwise=True):
    """
    Given the starting index in ring, move n elements clockwise/counter-clockwise
    and return the resulting index.
    """
    magnitude = (start + n) if clockwise else (start - n)
    index = magnitude % len(ring)
    # Elements to be added between the beginning and end of the list are added
    # to the end by convention
    if index == 0:
        index = len(ring)

    return index


def _next_player(current_player, players):
    return current_player + 1 if current_player + 1 <= len(players) else 1


def _print_board(current_player, current_marble, ring):
    player = "[%s]" % (current_player)  # Add one to make output match example
    items = ["(%s)" % i if i == current_marble else " %s " % i for i in ring]

    print player + " " + " ".join(items)


if __name__ == "__main__":

    score = high_score(429, 70901 * 100)
    print "High score:", score
