# 2018-06-25
# a naive implementation


import random
from tqdm import tqdm

lis = []
with open('kargerMinCut.txt') as file:
    for line in file:
        lis.append(list(map(int, line.split())))

def build_graph():
    # build the graph
    return {line[0]:line[1:] for line in lis}

def merge(graph):
    keys = list(graph.keys())
    connections = [[key, ele] for key in keys for ele in graph[key]]
    selection = random.sample(connections,1)[0]
    node_1, node_2 = min(selection), max(selection)
    graph[node_1] = [ele for ele in graph[node_1] if ele != node_2]
    graph[node_1].extend([ele for ele in graph[node_2] if ele != node_1])
    graph.pop(node_2)
    keys.remove(node_2)
    for key in keys:
        graph[key] = [ele if ele != node_2 else node_1 for ele in graph[key]]

graph = build_graph()
n = len(graph)
mini = n

for i in tqdm(range(n)):
    graph = build_graph()
    for _ in range(len(graph)-2):
        merge(graph)
    connection = len(graph[1])
    if connection < mini:
        mini = connection

print(mini)


