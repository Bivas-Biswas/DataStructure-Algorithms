class Graph:
    def __init__(self, V):
        self.graph = []
        self.v = V

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def print_graph(self):
        print(self.graph)

    def bellman_ford(self, s):
        n = self.v
        graph = self.graph

        # dist = [float('inf')] * n
        # Step 1: fill the distance array and predecessor array
        dist = {elem: float('inf') for elem in range(0, n)}

        # Mark the source vertex
        dist[s] = 0

        # Step 2: relax edges |V| - 1 times
        for i in range(n):
            for s, v, w in graph:
                newdist = dist[s] + w
                if dist[s] != float('inf') and dist[v] > newdist:
                    dist[v] = newdist

        # Step 3: detect negative cycle
        # if value changes then we have a negative cycle in the graph
        # and we cannot find the shortest distances
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        print(dist)


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 20)
    g.add_edge(1, 2, 30)
    g.add_edge(1, 3, 40)
    g.add_edge(1, 4, 60)
    g.add_edge(2, 3, 70)
    g.add_edge(3, 4, 80)
    g.add_edge(4, 3, 90)
    g.print_graph()
    print()
    # # g.remove_edge(1, 4)
    # # g.print_graph()
    # print(list(g.graph.values()))
    g.bellman_ford(0)
