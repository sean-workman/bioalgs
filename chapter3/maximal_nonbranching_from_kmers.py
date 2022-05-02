from sys import argv
from collections import Counter

def debruijn_adjacency_from_kmers(patterns):
    adjacency_list = {node[:-1]:[] for node in patterns}
    for kmer in patterns:
        adjacency_list[kmer[:-1]].append(kmer[1:])
    return adjacency_list

def path_to_genome(path):
    genome = path[0]
    for sequence in path[1:]:
        genome += sequence[-1]
    return genome

def maximal_nonbranching_paths(graph):
    paths = []
    outdegree = Counter({node: len(graph[node]) for node in graph})
    indegree = Counter()
    relative_degree = Counter({node: len(graph[node]) for node in graph})
    for adjacency_list in graph.values():
        indegree.update(adjacency_list)
    relative_degree.subtract(indegree)
    isolated_cycles = []
    for v in graph:
        if (indegree[v] and outdegree[v]) != 1:
            if outdegree[v] > 0:
                for w in graph[v]:
                    nonbranching = [v]
                    nonbranching.append(w)
                    while (indegree[w] == 1) and (outdegree[w] == 1):
                        u = graph[w][0]
                        nonbranching.append(u)
                        w = u
                    paths.append(path_to_genome(nonbranching))
        else:
            for w in graph[v]:
                cycle = [v]
                if relative_degree[w] <= 0:
                    cycle.append(w)
                while (relative_degree[w] == 0) and (outdegree[w] < 2):
                    u = graph[w][0]
                    cycle.append(u)
                    w = u
                    if cycle[0] == cycle[-1]:
                        break
                if len(cycle) > 1:
                    isolated_cycles.append(cycle)
    filtered = []
    isolated_cycles = sorted(isolated_cycles, reverse=True, key=len)
    filtermap = [set(f) for f in filtered]
    for cycle in isolated_cycles:
        if set(cycle) not in filtermap:
            filtered.append(cycle)
    filtered = [path_to_genome(f) for f in sorted(filtered, reverse=True, key=len)]
    for f in filtered:
        if not any(f in p for p in paths):
            paths.append(f)
    return paths


def main():
    with open(argv[1]) as data:
            inputs = data.read().split()
            kmers = inputs

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            graph = debruijn_adjacency_from_kmers(kmers)
            paths = maximal_nonbranching_paths(graph)
            out.write('\n'.join(paths))

    else:
        graph = debruijn_adjacency_from_kmers(kmers)
        paths = maximal_nonbranching_paths(graph)
        for p in paths:
            print(p)

if __name__ == "__main__":
    # main()
    import cProfile, pstats
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()