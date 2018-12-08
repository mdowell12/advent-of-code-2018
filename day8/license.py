

def read_input_file(f):
    with open(f, 'r') as ff:
        return ff.read().strip().split(" ")


def sum_metadata(data):
    data = map(int, data)
    _, metadatas = _parse_tree(data)
    return sum(metadatas)


def _parse_tree(data):
    # Base case is no children, so we will always have a header
    num_children = data[0]
    num_metadata = data[1]

    if num_children == 0:
        node_length = 2 + num_metadata
        return node_length, data[2:node_length]

    start = 2
    total_len_so_far = 2
    children_metadata = []

    for _ in range(num_children):
        remainder = data[start:]
        # if not remainder:
        #     import pdb; pdb.set_trace()
        child_len, child_metadata = _parse_tree(remainder)
        children_metadata += child_metadata
        start += child_len
        total_len_so_far += child_len

    # Start now represents the end of the final child
    end_metadata = start + num_metadata
    this_metadata = data[start:end_metadata]

    # end_metadata represents the length of this node
    return end_metadata, this_metadata + children_metadata


if __name__ == "__main__":
    import sys
    f = sys.argv[1]

    data = read_input_file(f)

    print "Metadata sum:", sum_metadata(data)
