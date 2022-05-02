from sys import argv
from random import choice


def eulerian_cycle(graph):
    cycle = []
    key = choice(list(graph))
    edge = choice(list(graph[key]))
    cycle.append(edge)
    key = edge
    while graph[key]:
        edge = choice(graph[key])
        cycle.append(edge)
        graph[key].remove(edge)
        key = edge
    remaining = {k:v for k,v in graph.items() if v}
    while [edge for node in graph.values() for edge in node]:
        newstart_index = cycle.index(choice([node for node in cycle if node in remaining]))
        cycle_prime = cycle[newstart_index:] + cycle[1:newstart_index+1]
        key = cycle[newstart_index]
        while remaining[key]:
            edge = choice(list(remaining[key]))
            cycle_prime.append(edge)
            remaining[key].remove(edge)
            key = edge
        cycle = cycle_prime
    return cycle


def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split('\n')
            formatted = [line.split(':') for line in inputs]
            graph = {int(node[0]):list(map(int, node[1].strip().split(' '))) for node in formatted}

    except:
        pattern = argv[1].split(',')
    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            cycle = eulerian_cycle(graph)
            out.write(' '.join(map(str, cycle)))

    else:
        print(*eulerian_cycle(graph))

if __name__ == "__main__":
    main()
    # import cProfile, pstats
    # profiler = cProfile.Profile()
    # profiler.enable()
    # main()
    # profiler.disable()
    # stats = pstats.Stats(profiler).sort_stats('ncalls')
    # stats.print_stats()


