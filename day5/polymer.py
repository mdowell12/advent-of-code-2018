import sys


def read_input_file(f):
    with open(f, 'r') as input:
        return input.read().strip()


def fully_collapsed_size(polymer):
    units = set(i.lower() for i in polymer)
    min_length = len(polymer)
    
    print "Found %s units to try removing: %s" % (len(units), units)

    for unit in units:
        print "Reducing without unit", unit
        polymer_without_unit = polymer.replace(unit, "").replace(unit.upper(), "")
        reacted = perform_reactions(polymer_without_unit)
        min_length = min(len(reacted), min_length)

    return min_length


def perform_reactions(polymer):
    while True:
        new_polymer = _reduce_polymer(polymer)
        if new_polymer == polymer:
            return new_polymer
        else:
            polymer = new_polymer
        

def perform_reactions_old(polymer):
    new_polymer = _reduce_polymer(polymer)

    if new_polymer == polymer:
        return new_polymer
    else:
        return perform_reactions(new_polymer)    


def _reduce_polymer(polymer):
    keep_out = set()

    for i, letter in enumerate(polymer):
        if i == len(polymer) - 1:
            break

        if i not in keep_out and _can_react(letter, polymer[i+1]):
            keep_out.add(i)
            keep_out.add(i+1)

    reduced = ""
    for i, letter in enumerate(polymer):
        if i not in keep_out: reduced += letter

    return reduced



def _can_react(first, second):
    return first.lower() == second.lower() and first.isupper() != second.isupper()


if __name__ == "__main__":
    f = sys.argv[1]

    polymer = read_input_file(f)

    result = perform_reactions(polymer)
    
    print "After reaction:", len(result)

    print "Fully collapsed size:", fully_collapsed_size(polymer)
