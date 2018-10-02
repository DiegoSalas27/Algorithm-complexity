# BFS implementation
# red visited
# black not visited 
class Vertex:
    def __init__(self, n): # takes a name argument
        self.name = n
        self.neighbors = []
        self.distance = 9999
        self.color = 'black'
    
    def add_neighbor(self, v): # v is a letter name of a vertex
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()

class Graph:
    vertices = {} # holds the vertex name as a key and the object as a value

    def add_vertex(self, vertex): # vertex is an object
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex 
            return True
        else:
            return False

    def add_edge(self, u, v): # u and v are two vertices names which are connected
        if u in self.vertices and v in self.vertices: # if u and v are keys of this dictionary
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbors) + ' ' + str(self.vertices[key].distance))

    def bfs(self, vert): # takes a vertex object as a starting point
        q = []
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1

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



