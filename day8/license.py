

def read_input_file(f):
    with open(f, 'r') as ff:
        return ff.read().strip().split(" ")


def sum_metadata(data):
    data = map(int, data)
    _, metadatas = _walk_tree_sum_metadata(data)
    return sum(metadatas)


def find_value(data):
    data = map(int, data)
    _, value = _walk_tree_sum_values(data)
    return value


def _walk_tree_sum_values(data):
    # Base case is no children, so we will always have a header
    num_children = data[0]
    num_metadata = data[1]

    if num_children == 0:
        node_length = 2 + num_metadata
        this_metadata = data[2:node_length]
        return node_length, sum(this_metadata)

    start = 2
    children_values = {}

    for i in range(num_children):
        child_len, child_value = _walk_tree_sum_values(data[start:])
        children_values[i + 1] = child_value
        start += child_len

    # Start now represents the end of the final child
    end_metadata = start + num_metadata
    this_metadata = data[start:end_metadata]

    value = sum(children_values.get(i, 0) for i in this_metadata)

    # end_metadata represents the length of this node
    return end_metadata, value


def _walk_tree_sum_metadata(data):
    # Base case is no children, so we will always have a header
    num_children = data[0]
    num_metadata = data[1]

    if num_children == 0:
        node_length = 2 + num_metadata
        return node_length, data[2:node_length]

    start = 2
    children_metadata = []

    for _ in range(num_children):
        child_len, child_metadata = _walk_tree_sum_metadata(data[start:])
        children_metadata += child_metadata
        start += child_len

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
    print "Value:", find_value(data)
