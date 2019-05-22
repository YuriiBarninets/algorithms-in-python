class Vertex:
    def __init__(self, label):
        self.__label = label
        self.__outbound_edges = []

    def __str__(self):
        outbound_edges_str = ""
        for edge in self.__outbound_edges:
            outbound_edges_str += str(edge) + ", "

        return "Vertex : {0}, Outbound edges : {1}".format(self.__label, outbound_edges_str)

    def get_outbound_edges(self):
        return self.__outbound_edges

    def get_label(self):
        return self.__label

    def add_edge(self, edge):
        self.__outbound_edges.append(edge)


class Edge:
    def __init__(self, start_vertex, end_vertex, weight=1):
        self.__start_vertex = start_vertex
        self.__end_vertex = end_vertex
        self.__weight = weight

    def __str__(self):
        return "{0} -{1}-> {2}".format(self.__start_vertex.get_label(), self.__weight, self.__end_vertex.get_label())

    def get_start_vertex(self):
        return self.__start_vertex

    def get_end_vertex(self):
        return self.__end_vertex

    def get_weight(self):
        return self.__weight


class Graph:
    def __init__(self):
        self.__vertices = {}
        self.__edges = []

    def __str__(self):
        graph_str = ""

        for key in self.__vertices:
            graph_str += str(self.__vertices[key]) + '\n'

        return graph_str

    def add_vertex(self, label):
        self.__vertices[label] = Vertex(label)

    def add_edge(self, start_label, end_label, weight=1):
        edge = Edge(self.__vertices[start_label],
                    self.__vertices[end_label], weight)
        self.__vertices[start_label].add_edge(edge)
        self.__edges.append(edge)

    def get_vertex(self, label):
        return self.__vertices[label]

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges


if __name__ == "__main__":
    test_graph = Graph()

    # vertices
    test_graph.add_vertex("a")
    test_graph.add_vertex("b")
    test_graph.add_vertex("c")

    # edges
    test_graph.add_edge("a", "b", 2)
    test_graph.add_edge("a", "c", 7)
    test_graph.add_edge("c", "b", 1)
    test_graph.add_edge("b", "c", 3)

    print(str(test_graph))
