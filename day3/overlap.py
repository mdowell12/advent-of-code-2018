
def read_input_file(f):
    with open(f, 'r') as input:
        return input.read().strip().split('\n')


def find_no_overlap(claims):
    parsed_claims = [_parse_claim(c) for c in claims]
    fabric = _layout_claims(parsed_claims)

    return _find_first_non_overlapping(parsed_claims, fabric)


def calculate_overlap(claims):
    parsed_claims = [_parse_claim(c) for c in claims]
    fabric = _layout_claims(parsed_claims)

    return _count_overlaps(fabric)


def _find_first_non_overlapping(parsed_claims, fabric):
    for claim in parsed_claims:
        claim_id, left_margin, top_margin, width, height = claim
        if _has_no_overlap(left_margin, top_margin, width, height, fabric):
            return claim_id
                
    raise Exception("No non-overlapping claim found")


def _has_no_overlap(left_margin, top_margin, width, height, fabric):
    for x in xrange(left_margin, left_margin + width):
        for y in xrange(top_margin, top_margin + height):
            if fabric[(x,y)] != 1:
                return False 
    return True


def _layout_claims(parsed_claims):
    # Maps tuple of (x,y) coordinate to the number of claims
    # on that coordinate
    fabric = {}

    for claim in parsed_claims:
        _claim_id, left_margin, top_margin, width, height = claim
        fabric = _layout_claim(fabric, left_margin, top_margin, width, height)

    return fabric


def _layout_claim(fabric, left_margin, top_margin, width, height):
    top_left = (left_margin, top_margin)

    for x in xrange(left_margin, left_margin + width):
        for y in xrange(top_margin, top_margin + height):
            point = (x, y)
            if point not in fabric:
                fabric[point] = 1
            else:
                fabric[point] += 1    

    return fabric


def _parse_claim(claim):
    parts = claim.strip().split(' ')
    claim_id = parts[0]
    margins = map(int, parts[2][:-1].split(','))
    dimensions = map(int, parts[3].split('x'))

    return claim_id, margins[0], margins[1], dimensions[0], dimensions[1]


def _count_overlaps(fabric):
    return sum([1 for i in fabric.values() if i > 1])


if __name__ == "__main__":
    import sys
    f = sys.argv[1]

    claims = read_input_file(f)
    num_overlaps = calculate_overlap(claims)

    print "Number of overlaps:", num_overlaps

    non_overlapping = find_no_overlap(claims)
    print "Non-overlapping claim:", non_overlapping
