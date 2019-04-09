class Vertex:
    def __init__(self, label):
        self.label = label
        self.outbound_edges = []

    def __str__(self):
        outbound_edges_str = ""
        for edge in self.outbound_edges:
            outbound_edges_str += str(edge) + ", "

        return "Vertex : {0}, Outbound edges : {1}".format(self.label, outbound_edges_str)


class Edge:
    def __init__(self, start_vertex, end_vertex):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

    def __str__(self):
        return "{0} -> {1}".format(self.start_vertex.label, self.end_vertex.label)


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def __str__(self):
        graph_str = ""

        for vertex in self.vertices:
            graph_str += str(vertex) + '\n'

        return graph_str
