def find_group_from_node(graph, from_node):
    to_check = [from_node]
    seen = []
    while to_check:
        current = graph[to_check.pop(0)]
        for pipe in current:
            if not pipe in seen:
                seen.append(pipe)
                to_check.append(pipe)
    return seen


def find_all_groups_in_graph(graph):
    to_check = [i for i in graph.keys()]
    seen_groups = 0
    while to_check:
        current = to_check[0]
        seen_group = find_group_from_node(graph, current)
        for node in seen_group:
            to_check.remove(node)
        seen_groups += 1
    return seen_groups


with open('puzzle_input') as file:
    lines = file.readlines()
    lines = [line.strip().split(' <-> ') for line in lines]

graph = {}
for index, line in enumerate(lines): 
    graph[index] = [int(i) for i in line[1].split(', ')]

part1 = find_group_from_node(graph, 0)
print(f'Part 1: {len(part1)}')
part2 = find_all_groups_in_graph(graph)
print(f'Part 2: {part2}')
