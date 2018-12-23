#bruteforce

def solve1(s):
    max_size = 0
    for step_size in range(2, len(s)):
        for start in range(len(s) - step_size + 1):
            num_a = 0
            num_b = 0
            for i in range(start, start + step_size):
                if s[i] == 'a':
                    num_a += 1
                else:
                    num_b += 1
            if num_a == num_b:
                max_size = step_size
                break
    return max_size 

def populate_deltas(s):
    delta = 0
    freqs = {}
    for i, char in enumerate(s):
        if char == 'a':
            delta += 1
        else:
            delta -= 1
        freqs[i] = delta
    freqs[-1] = 0
    return freqs

def solve2(s):
    max_size = 0
    deltas = populate_deltas(s)
    for step_size in range(2, len(s)):
        for start in range(len(s) - step_size + 1):
            delta_end = deltas[start + step_size - 1]
            delta_start = deltas[start - 1]
            if (delta_end == delta_start):
                max_size = step_size
                break 
    return max_size

def solve3(s):
    max_size = 0
    deltas = populate_deltas(s)
    first_delta_ocurrence = {}
    for i in range(-1, len(deltas) - 1):
        if deltas[i] not in first_delta_ocurrence:
            first_delta_ocurrence[deltas[i]] = i
        else:
            max_size = max(max_size, i - first_delta_ocurrence[deltas[i]])
    return max_size

        
print(solve1('ababaaaa'))
print(solve2('ababaaaa'))
print(solve3('ababaaaa'))   