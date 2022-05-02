from sys import argv
from collections import Counter
from chapter3 import eulerian_cycle

def graph_from_gapped_patterns(k, d, gapped_patterns):
    enumerate_dict = {pattern:[] for pattern in gapped_patterns}
    for pattern in gapped_patterns:
        enumerate_dict[pattern].append('|'.join([pattern[1:1+k-1], pattern[k+2:k+2+k-1]]))
        enumerate_dict[pattern].append('|'.join([pattern[:k-1], pattern[k+1:k+1+k-1]]))
    graph = {}
    for s_pair,s_fixes in enumerate_dict.items():
        graph[s_pair] = []
        for q_pair,q_fixes in enumerate_dict.items():
            if s_fixes[0] == q_fixes[1]:
                graph[s_pair].append(q_pair)
                break
    return graph

def reconstruction_from_read_pairs(k, graph, gapped_patterns):
    relative_degree_counter = Counter({node: len(graph[node]) for node in graph})
    indegree_counter = Counter()
    for adjacency_list in graph.values():
        indegree_counter.update(adjacency_list)
    relative_degree_counter.subtract(indegree_counter)
    start_node = list(+relative_degree_counter)[0]
    terminal_node = list(-relative_degree_counter)[0]
    graph.setdefault(terminal_node, []).append(start_node)
    path = eulerian_cycle(graph)
    for ix,node in enumerate(path):
        if (node == start_node):
            if path[ix-1] == terminal_node:
                path = path[ix:] + path[1:ix]
                break
    path = [p.split('|') for p in path]
    return path

def string_spelled_by_patterns(patterns, k):
    return ''.join([p[:-k+1] for p in patterns[:-1]]) + patterns[-1]

def string_spelled_by_gapped_pattern_path(k, d, path):
    first_patterns = [p[0] for p in path]
    second_patterns = [p[1] for p in path]
    prefix_string = string_spelled_by_patterns(first_patterns, k)
    suffix_string = string_spelled_by_patterns(second_patterns, k)
    for i in range(k+d+1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "There is no string spelled by the gapped patterns"
    return prefix_string + suffix_string[-(k+d):]
    

def main():
    try:
        with open(argv[1]) as data:
            inputs = data.read().split()
            k = int(inputs[0])
            d = int(inputs[1])
            gapped_patterns = inputs[2:]


    except:
        k = int(argv[1])
        d = int(argv[2])
        gapped_patterns = [p.split('|') for p in argv[3].split(',')]

    if len(argv) == 3 and argv[2].endswith('.txt'):
        output = argv[2]

        with open(output, 'wt') as out:
            graph = graph_from_gapped_patterns(k, d, gapped_patterns)
            path = reconstruction_from_read_pairs(k, graph, gapped_patterns)
            reconstruction = string_spelled_by_gapped_pattern_path(k, d, path)
            out.write(reconstruction)

    else:
        graph = graph_from_gapped_patterns(k, d, gapped_patterns)
        path = reconstruction_from_read_pairs(k, graph, gapped_patterns)
        reconstruction = string_spelled_by_gapped_pattern_path(k, d, path)
        print(reconstruction)
    
if __name__ == "__main__":
    main()
    # import cProfile, pstats
    # profiler = cProfile.Profile()
    # profiler.enable()
    # main()
    # profiler.disable()
    # stats = pstats.Stats(profiler).sort_stats('ncalls')
    # stats.print_stats()