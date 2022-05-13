from sys import argv

def spectral_convolution(spectrum):
    convolution_map = {}
    for s_mass in spectrum:
        for q_mass in spectrum:
            diff = s_mass - q_mass
            if diff > 0:
                if diff in convolution_map:
                    convolution_map[diff] += 1
                else:
                    convolution_map[diff] = 1
    convolution = {k:v for k,v in sorted(convolution_map.items(), key = lambda item: item[1], reverse=True) if 57 <= k <= 200}
    convolution = list(convolution.keys())[:5]
    return convolution

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            spectrum = [int(i) for i in inputs]
    except:
        spectrum = [int(i) for i in argv[1].split(',')]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            convolution = spectral_convolution(spectrum)
            out.write(convolution)

    else:
        print(spectral_convolution(spectrum))

if __name__ == "__main__":
    main()
    # import cProfile, pstats
    # profiler = cProfile.Profile()
    # profiler.enable()
    # main()
    # profiler.disable()
    # stats = pstats.Stats(profiler).sort_stats('ncalls')
    # stats.print_stats()