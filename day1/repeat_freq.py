from jitter import calculate_next_freq
from jitter import read_input_file


def find_first_repeat(freqs, acc=0, seen=None):
    seen = seen if seen else {0,}
    for freq in iter(freqs):
        acc = calculate_next_freq(acc, freq)
        if acc in seen:
            return acc
        else:
            seen.add(acc)

    return find_first_repeat(freqs, acc=acc, seen=seen)


if __name__ == "__main__":
    import sys
    f = sys.argv[1]
    freqs = read_input_file(f)

    result = find_first_repeat(freqs)
    
    print result
