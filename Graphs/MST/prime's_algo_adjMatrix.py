class Graph:
    def __init__(self, graph):
        self.graph = graph

    def selectMinVertex(self, value, setMst):
        minimum = float('inf')
        n = len(self.graph)

        for i in range(n):

            # here we first avoid the non relaxing edge
            # and find the minimum distance vertics
            if setMst[i] == False and value[i] < minimum:
                vertex = i
                minimum = value[i]
                print(i)
        return vertex

    def primMST(self):
        n = len(self.graph)
        parent = [i for i in range(n)]  # stores MST
        value = [float('inf')] * n  # used for edge relaxation
        setMst = [False] * n  # TRUE -> vertex is included in BST

        # assuming start point as Node -> 0
        parent[0] = -1
        value[0] = 0

        # form MST with (V-1) edges
        for i in range(n):
            # step 1
            # select best vertex by applying greedy method
            u = self.selectMinVertex(value, setMst)
            setMst[u] = True  # include new vertex in MST
            print("!")

            # step 2
            # relax adjacency vertices ( not yet include in MST)
            for j in range(n):
                # constraints to relac :-
                #       1. Edge is present from u to 3
                #       2. Vertex j is not included in MST
                #       3. Edge weight is smaller than current edge weight
                if self.graph[u][j] != 0 and setMst[j] == False and self.graph[u][j] < value[j]:
                    value[j] = self.graph[u][j]

                    parent[j] = u
        print(parent)
        print(value)


if __name__ == "__main__":
    g1 = [[0, 3, 1, 0],
          [3, 0, 4, 1],
          [1, 4, 0, 2],
          [0, 1, 2, 0]]
    g = Graph(g1)
    g.primMST()

# time complexity O(n*n)
