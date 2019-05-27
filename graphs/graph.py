class Vertex:
    def __init__(self, label):
        self.__label = label
        self.__outbound_edges = []
        self.__inbound_edges = []

    def __str__(self):
        outbound_edges_str = ""
        for edge in self.__outbound_edges:
            outbound_edges_str += str(edge) + ", "

        return "Vertex : {0}, Outbound edges : {1}".format(self.__label, outbound_edges_str)

    def get_outbound_edges(self):
        return self.__outbound_edges

    def get_inbound_edges(self):
        return self.__inbound_edges

    def get_label(self):
        return self.__label

    def add_outbound_edge(self, edge):
        self.__outbound_edges.append(edge)

    def add_inbound_edge(self, edge):
        self.__inbound_edges.append(edge)


class Edge:
    def __init__(self, start_vertex, end_vertex, weight=1, directed=True):
        self.__start_vertex = start_vertex
        self.__end_vertex = end_vertex
        self.__weight = weight
        self.__directed = directed

    def __str__(self):
        if self.__directed == True:
            print_pattern = "{0} -{1}-> {2}"
        else:
            print_pattern = "{0} <-{1}-> {2}"
        return print_pattern.format(self.__start_vertex.get_label(), self.__weight, self.__end_vertex.get_label())

    def get_start_vertex(self):
        return self.__start_vertex

    def get_end_vertex(self):
        return self.__end_vertex

    def get_weight(self):
        return self.__weight

    def __lt__(self, other):
        return self.get_weight() < other.get_weight()


class Graph:
    def __init__(self, directed=True):
        self.__vertices = {}
        self.__edges = []
        self.__directed = directed

    def __str__(self):
        graph_str = ""

        for key in self.__vertices:
            graph_str += str(self.__vertices[key]) + '\n'

        return graph_str

    def add_vertex(self, label):
        self.__vertices[label] = Vertex(label)

    def add_edge(self, start_label, end_label, weight=1):
        edge = Edge(self.__vertices[start_label],
                    self.__vertices[end_label], weight, self.__directed)
        self.__vertices[start_label].add_outbound_edge(edge)
        self.__vertices[end_label].add_inbound_edge(edge)
        self.__edges.append(edge)

        if self.__directed == False:
            reverse_edge = Edge(
                self.__vertices[end_label], self.__vertices[start_label], weight, self.__directed)
            self.__vertices[end_label].add_outbound_edge(reverse_edge)
            self.__vertices[start_label].add_inbound_edge(reverse_edge)
            self.__edges.append(reverse_edge)

    def get_vertex(self, label):
        return self.__vertices[label]

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges

    def get_indegree(self, label):
        return len(self.__vertices[label].get_inbound_edges())

    def get_outdegree(self, label):
        return len(self.__vertices[label].get_outbound_edges())


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
