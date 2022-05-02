from random import choice
from collections import Counter
from chapter1 import *
from chapter2 import *

def kmer_composition(k, text):
    return [text[ix:ix+k] for ix,_ in enumerate(text[:-k+1])]

def path_to_genome(path):
    genome = path[0]
    for sequence in path[1:]:
        genome += sequence[-1]
    return genome

def debruijn_adjacency(k, text):
    all_kmers = [text[ix:ix+k] for ix,_ in enumerate(text[:-k+1])]
    adjacency_list = {node[:-1]:[] for node in all_kmers}
    for kmer in all_kmers:
        adjacency_list[kmer[:-1]].append(kmer[1:])
    return adjacency_list

def debruijn_adjacency_from_kmers(patterns):
    adjacency_list = {node[:-1]:[] for node in patterns}
    for kmer in patterns:
        adjacency_list[kmer[:-1]].append(kmer[1:])
    return adjacency_list

def overlap_adjacency(patterns):
    adjacency_list = {}
    for kmer in patterns:
        kmer_list = []
        kmer_suffix= kmer[1:]
        for query in patterns:
            if query[:-1] == kmer_suffix:
                kmer_list.append(query)
        if kmer_list:
            adjacency_list[kmer] = kmer_list
    return adjacency_list

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
    
def string_reconstruction(patterns):
    db = debruijn_adjacency_from_kmers(patterns)
    path = eulerian_path(db)
    text = path_to_genome(path)
    return text

def string_spelled_by_patterns(first_patterns, second_patterns):
    prefix_string = ''.join([p[:-1] for p in first_patterns[:-1]]) + first_patterns[-1]
    suffix_string = ''.join([p[:-1] for p in second_patterns[:-1]]) + second_patterns[-1]
    distances = []
    for p_ix,_ in enumerate(prefix_string[1:], 1):
        p_query = prefix_string[p_ix:]
        s_query = suffix_string[:-p_ix]
        distances.append((hamming_distance(p_query, s_query)))

    comp_ix = distances.index(min(distances))+1

    return prefix_string[:comp_ix] + suffix_string

def string_spelled_by_gapped_patterns(k, d, gapped_patterns):
    first_patterns = [p[0] for p in gapped_patterns]
    second_patterns = [p[1] for p in gapped_patterns]
    prefix_string = string_spelled_by_patterns(first_patterns, k)
    suffix_string = string_spelled_by_patterns(second_patterns, k)
    for i in range(k+d+1, len(prefix_string)):
        if prefix_string[i] != suffix_string[i-k-d]:
            return "There is no string spelled by the gapped patterns"
    return prefix_string + suffix_string[-(k+d):]

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

def k_universal(k):
    kmers = [''.join(kmer) for kmer in list(product('01', repeat=k))]
    path = string_reconstruction(kmers)
    return path[:-k+1]