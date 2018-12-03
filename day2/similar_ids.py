from calculate_checksum import read_input_file


def find_similar_ids(box_ids):
    for box_id in box_ids:
        similar = _find_similar(box_id, box_ids)
        if similar is not None:
            return _calculate_similar_letters(box_id, similar)
    raise Exception("could not find similar")



def _find_similar(box_id, all_box_ids):
    for other in all_box_ids:
        if other == box_id:
            continue

        num_different = 0
        for a, b in zip(box_id, other):
            if a != b:
                num_different += 1

        if num_different == 1:
            return other

    return None



def _calculate_similar_letters(box_id_a, box_id_b):
    similars = []
    for a, b in zip(box_id_a, box_id_b):
        if a == b:
            similars.append(a)
    return ''.join(similars)


if __name__ == "__main__":
    import sys
    f = sys.argv[1]

    box_ids = read_input_file(f)

    print find_similar_ids(box_ids)

