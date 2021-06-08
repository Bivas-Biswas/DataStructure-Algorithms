from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)

    def remove_edge(self, u, v):
        self.graph[u].remove(v)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.print_graph()
    print()
    # g.remove_edge(1, 4)
    # g.print_graph()
    print(list(g.graph.values()))





