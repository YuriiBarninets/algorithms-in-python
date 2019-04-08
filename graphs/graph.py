class Vertex:
    def __init__(self, label):
        self.label = label
        self.outbound_edges = []


class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges


if __name__ == "__main__":
    # vertices
    ivan = Vertex("Ivan")
    stepan = Vertex("Stepan")
    taras = Vertex("Taras")

    # edges ivan --> stepan, ivan --> taras
    ivan.outbound_edges.append(Edge(ivan, stepan))
    ivan.outbound_edges.append(Edge(ivan, taras))

    # edge taras --> stepan
    taras.outbound_edges.append(Edge(taras, stepan))

    # edge stepan --> ivan
    stepan.outbound_edges.append(Edge(stepan, ivan))

    # graph
    vertices = [ivan, stepan, taras]
    edges = []

    for vertex in vertices:
        edges.extend(vertex.outbound_edges)

    graph = Graph(vertices, edges)
