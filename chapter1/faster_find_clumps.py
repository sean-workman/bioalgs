from sys import argv

def fast_find_clumps(text, k, L, t):
    pos_map = position_table(text, k)
    clumps = set()
    for pattern in pos_map:
        positions = pos_map[pattern]
        if len(positions) >= t:
            if is_clump(positions, k, L, t):
                clumps.add(pattern)
    return clumps

def position_table(text, k):
    pos_map = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        try:
            pos_map[pattern].append(i)
        except KeyError:
            pos_map[pattern] = [i]
    return pos_map

def is_clump(positions, k, L, t):
    for i in range(len(positions) - t + 1):
        if positions[i + t - 1] - positions[i] <= L - k:
            return True
    return False

if __name__ == "__main__":

    try:
        with open(argv[1]) as data:
            lines = ' '.join([l.rstrip() for l in data.readlines()]).split()
            text = lines[0]
            k = int(lines[1])
            L = int(lines[2])
            t = int(lines[3])

    except:
        text = argv[1]
        k = int(argv[2])
        L = int(argv[3])
        t = int(argv[4])

    if len(argv) == 3:
        output = argv[2]

        with open(output, 'wt') as out:
            patterns = fast_find_clumps(text, k, L, t)
            out.write(' '.join(patterns))

    else:
        print(len(fast_find_clumps(text, k, L, t)))