from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)

    # for one graph component
    def dfs_walk(self, visted, s):
        if visted[s]:
            return
        visted[s] = True
        for neighbor in self.graph[s]:
            if not visted[neighbor]:
                self.dfs_walk(visted, neighbor)
        print(s, end=" ")

    # for connected componenets, we traverse all component
    # one by one
    def dfs(self):
        visted = [False] * len(self.graph)
        for u in range(len(self.graph)):
            if not visted[u]:
                self.dfs_walk(visted, u)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 0)
    g.print_graph()

    # Child - Root Output -->

    # for one component we call function
    # by edges value
    # here we have control over chosen the vertic
    visted1 = [False] * len(g.graph)
    g.dfs_walk(visted1, 0)
    print()

    # for one more connected components
    # we traverse all componets one by one
    # here we have no control over chosen the vertic
    g.dfs()

