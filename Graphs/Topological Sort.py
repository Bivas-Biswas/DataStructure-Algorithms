class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph)

    def dfs(self, v, visited, st):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited, st)
        st.append(v)

    def topologicalSort(self):
        visited = [False] * self.V
        st = []
        for i in range(self.V):
            if not visited[i]:
                self.dfs(i, visited, st)

        print(st[::-1])


if __name__ == "__main__":
    graph = {5: [2, 0],
             4: [0, 1],
             2: [3],
             3: [1],
             1: [],
             0: []
             }
    g1 = Graph(graph)
    g1.topologicalSort()
