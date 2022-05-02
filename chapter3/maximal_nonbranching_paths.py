from sys import argv
from collections import Counter

def maximal_nonbranching_paths(graph):
    paths = []
    relative_degree_counter = Counter({node: len(graph[node]) for node in graph})
    indegree_counter = Counter()
    for adjacency_list in graph.values():
        indegree_counter.update(adjacency_list)
    relative_degree_counter.subtract(indegree_counter)
    for v in graph:
        if relative_degree_counter[v] != 0:
            if relative_degree_counter[v] > 0:
                for w in graph[v]:
                    non_branching = [v]
                    non_branching.append(w)
                    while relative_degree_counter[w] == 0:
                        u = graph[w][0]
                        non_branching.append(u)
                        w = u
                    paths.append(' '.join(non_branching))
    # Need to deal with isolated cycle
    isolated_cycles = []
    for v in graph:
        if relative_degree_counter[v] <= 0:
            for w in graph[v]:
                cycle = [v]
                if relative_degree_counter[w] <= 0:
                    cycle.append(w)
                while relative_degree_counter[w] == 0:
                    u = graph[w][0]
                    cycle.append(u)
                    w = u
                    if cycle[0] == cycle[-1]:
                        break
                if len(cycle) > 1:
                    isolated_cycles.append(cycle)
    filtered = []
    isolated_cycles = sorted(isolated_cycles, reverse=True, key=len)
    for cycle in isolated_cycles:
        if set(cycle) not in [set(f) for f in filtered]:
            filtered.append(cycle)
    filtered = [' '.join(f) for f in sorted(filtered, reverse=True, key=len)]
    to_remove = set()
    for f in filtered:
        for q in filtered:
            if (f in q) and (f != q):
                to_remove.add(f)
        for p in paths:
            if f in p:
                to_remove.add(f)
    for r in to_remove:
        if r in filtered:
            filtered.remove(r)
    for f in filtered:
        paths.append(f)    

    return paths


def main():
    with open(argv[1]) as data:
            inputs = data.read().split('\n')
            formatted = [line.split(':') for line in inputs]
            graph = {node[0]:node[1].strip().split(' ') for node in formatted}

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]
        with open(output, 'wt') as out:
            paths = maximal_nonbranching_paths(graph)
            out.write('\n'.join(paths))

    else:
        paths = maximal_nonbranching_paths(graph)
        for p in paths:
            print(p)

if __name__ == "__main__":
    main()