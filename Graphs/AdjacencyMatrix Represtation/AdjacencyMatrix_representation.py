class Graph:
    def __init__(self, size):
        self.matrix = []
        for i in range(size):
            self.matrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, u, v):
        if u == v:
            print("Same vertex {} and{} ", format(u, v))
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    def delete_edge(self, u, v):
        if self.matrix[u][v] == 0:
            print(" No edge between {} and {}".format(u, v))
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    def print_matrix(self):
        n = self.size
        print("   ", end=" ")
        for i in range(n):
            print(i, end=' ')
        print()

        for row in range(n):
            print("{} :".format(row), end=" ")
            for col in range(n):
                print(self.matrix[row][col], end=" ")
            print()


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()
    print("after delete : ")
    g.delete_edge(2, 0)
    g.print_matrix()

