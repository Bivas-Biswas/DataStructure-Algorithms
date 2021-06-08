from collections import defaultdict
# from collections import deque


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def print_graph(self):
        print(self.graph)

    def bfs_walk(self, q, visited):
        if not q:
            return
        temp = q.pop(0)
        # temp = q.popleft()
        print(temp, end=" ")
        for i in self.graph[temp]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
        self.bfs_walk(q, visited)

    def bfs(self, s):
        visited = [False] * len(self.graph)
        q = []
        # q = deque()
        q.append(s)
        visited[s] = True
        self.bfs_walk(q, visited)


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
    print()
    g.bfs(1)
