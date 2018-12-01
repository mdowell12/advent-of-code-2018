

def read_input_file(f):
    with open(f, 'r') as input:
        return input.read().strip().split('\n')

def parse_sign_and_int(row):
    return row[0], int(row[1:])


def calculate_next_freq(acc, next_freq):
    sign, num = parse_sign_and_int(next_freq)
    if sign == "+":
        return acc + num
    else:
        return acc - num

def calculate_jitter(freqs):
    acc = 0
    for freq in iter(freqs):
	acc = calculate_next_freq(acc, freq) 
    return acc

if __name__ == "__main__":
    import sys
    f = sys.argv[1]
    
    freqs = read_input_file(f)
    result = calculate_jitter(freqs)

    print result
