# BFS Implementation

class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = []
        self.distance = 9999
        self.color = 'black'
    
    def add_neighbor(self, n):
        if n not in self.neighbors:
            self.neighbors.append(n)
            self.neighbors.sort()

class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + ' ' + str(self.vertices[key].distance))
    
    def bfs(self, vertex):
        q = []
        vertex.color = 'red'
        vertex.distance = 0
        for v in vertex.neighbors:
            q.append(v)
            self.vertices[v].distance = vertex.distance + 1

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                if self.vertices[v].color == 'black':
                    q.append(v)
                    if self.vertices[v].distance > node_u.distance + 1:
                        self.vertices[v].distance = node_u.distance + 1

g = Graph()
a = Vertex('A')
g.add_vertex(a)
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[0], edge[1])

g.bfs(a)
g.print_graph()