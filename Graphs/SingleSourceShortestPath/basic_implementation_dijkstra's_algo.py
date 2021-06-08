from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def print_graph(self):
        print(self.graph)

    def dijkstra_basic(self, s):
        graph = self.graph
        n = len(graph)
        dist = [float('inf')] * n
        visited = [False] * n
        q = []
        q.append((s, 0))
        while q:
            index, mindist = q.pop(0)

            # in this condition we check if the index visited or not
            # and also compare already vistied and the old value if less than the current value in mindist
            if visited[index] and dist[index] < mindist:
                continue
            dist[index] = mindist
            visited[index] = True
            for edge in graph[index]:
                newdist = dist[index] + graph[index][edge]

                # in next line condition very important because
                # if there is a edge already visited
                # and the edge's distance is bigger than newdist
                # then we also need to compare the the distance new and old,
                # ohterwise we not get the smallest distance
                if not visited[edge] or dist[edge] > newdist:
                    q.append((edge, newdist))
        print(dist)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 10)
    g.add_edge(0, 4, 20)
    g.add_edge(1, 2, 30)
    g.add_edge(1, 3, 40)
    g.add_edge(1, 4, 60)
    g.add_edge(2, 3, 70)
    g.add_edge(3, 4, 80)
    g.add_edge(4, 3, 90)
    g.print_graph()
    g.dijkstra_basic(0)

