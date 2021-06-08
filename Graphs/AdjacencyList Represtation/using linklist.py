class AdjNode:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, u, v):
        # Adding the node to the source node
        node = AdjNode(v)
        node.next = self.graph[u]
        self.graph[u] = node

        # adding the source node to the destination as
        # it is the undirected graph
        node = AdjNode(u)
        node.next = self.graph[v]
        self.graph[v] = node

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head [{}]".format(i, i), end=" ")
            temp = self.graph[i]
            while temp:
                print("-->[{}]".format(temp.vertex), end=" ")
                temp = temp.next
            print()


if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()
