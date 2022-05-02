from sys import argv
from collections import Counter
from chapter3 import eulerian_cycle


def eulerian_path(graph):
    relative_degree_counter = Counter({node: len(graph[node]) for node in graph})
    indegree_counter = Counter()
    for adjacency_list in graph.values():
        indegree_counter.update(adjacency_list)
    relative_degree_counter.subtract(indegree_counter)
    if +relative_degree_counter:
        start_node = list(+relative_degree_counter)[0]
        terminal_node = list(-relative_degree_counter)[0]
        graph.setdefault(terminal_node, []).append(start_node)
        path = eulerian_cycle(graph)
        for ix,node in enumerate(path):
            if (node == start_node):
                if path[ix-1] == terminal_node:
                    path = path[ix:] + path[1:ix]
                    break
    else:
        path = eulerian_cycle(graph)
    return path
    



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
            path = eulerian_path(graph)
            out.write(' '.join(map(str, path)))

    else:
        print(*eulerian_path(graph))

if __name__ == "__main__":
    main()
    # import cProfile, pstats
    # profiler = cProfile.Profile()
    # profiler.enable()
    # main()
    # profiler.disable()
    # stats = pstats.Stats(profiler).sort_stats('ncalls')
    # stats.print_stats()


