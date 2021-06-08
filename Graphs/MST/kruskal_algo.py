class graph:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(graph) - 1

    # a utility function to find set of an element i
    # (use path cmpression technique)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # a function that does union of two sets of x and y
    # (uses union by rank)
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # attach smaller rank tree under root of
        # high rank tree (Union by Rank)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskalMST(self):
        result = []  # this will store the resultant MST

        # an index varible, usef for sorted edges
        i = 0

        # an index varible, used for result[0]
        e = 0

        # step 1: Sort all edges in
        # non-decreasing order of their
        # weight. If we are not allowed to change the
        # given graph, we can create a copy of graph
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            # step 2: Pick the smallest edge and increment
            # the index for next iteration
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if including this edge does't
            # cause cycle, include it in result
            # and increment the indexof result
            # for next edge
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
                # else discard the edge
                # print(result)
        print()
        print(result)


if __name__ == "__main__":
    g1 = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
    g = graph(g1)
    g.kruskalMST()
