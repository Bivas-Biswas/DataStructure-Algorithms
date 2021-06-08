from collections import defaultdict
import heapq


class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edge(self, u, v, w):
        self.graph[u][v] = w

    def print_graph(self):
        print(self.graph)

    # basic implementation [O(E^2)]
    def dijkstra_basic(self, s):
        graph = self.graph
        dist = {}
        q = []
        q.append((s, 0))
        while q:
            index, mindist = q.pop(0)

            # in this condition we check if the index in dist diconary
            # already vistied and the old value if less than the current value in mindist
            if index in dist and dist[index] < mindist:
                continue
            dist[index] = mindist
            for edge in graph[index]:
                newdist = dist[index] + graph[index][edge]

                # in next line condition very important because
                # if there is a edge already exist in the dist diconary
                # and the edge's distance is bigger than newdist
                # then we also need to compare the the distance new and old,
                # ohterwise we not get the smallest distance
                if edge not in dist or dist[edge] > newdist:
                    q.append((edge, newdist))
        print(dist)

    # Heap implementation --> O(ELogV)

    def dijkstra_heap(self, s):
        graph = self.graph
        dist = {}
        heap = [(s, 0)]
        while heap:
            index, mindist = heapq.heappop(heap)

            # in this condition we check if the index in dist diconary
            # already vistied and the old value if less than the current value in mindist
            if index in dist and dist[index] < mindist:
                continue
            dist[index] = mindist
            for edge in graph[index]:
                newdist = dist[index] + graph[index][edge]

                # here we not need to compare the old edge distance and newdist
                # because when we pop from the pq we always get min value
                # when we insert first time a edge distance, this is the minimum distance
                # for the edge because of priority queqe properties
                if edge not in dist:
                    heapq.heappush(heap, (edge, newdist))

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
    # print()
    g.dijkstra_basic(0)
    # print()
    g.dijkstra_heap(0)
