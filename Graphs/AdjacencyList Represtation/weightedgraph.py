from collections import defaultdict


class Graph:
    def __init__(self):
        # self.graph = defaultdict(list)  # using tuple
        self.graph = defaultdict(dict)  # using dict

    def add_edge(self, u, v, w):
        # self.graph[u].append((v, w))
        self.graph[u][v] = w

    def print_graph(self):
        print(self.graph)

    def remove_edge(self, u, v):

        self.graph[u].pop(v)  # for dic


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 20)
    g.add_edge(1, 2, 30)
    g.add_edge(1, 3, 40)
    g.add_edge(1, 4, 60)
    g.add_edge(2, 3, 70)
    g.add_edge(3, 4, 80)
    g.print_graph()
    print()
    # g.remove_edge(1, 4)
    # g.print_graph()
    print(list(g.graph.values()))
