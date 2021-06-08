from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)

    def dfs_walk(self, visited, s):
        st = []
        st.append(s)
        # visited[s] = True
        while len(st):
            s = st.pop()
            if not visited[s]:
                print(s, end=" ")
                visited[s] = True

            for v in self.graph[s]:
                if not visited[v]:
                    st.append(v)

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

    # Root - Child Output -->

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
