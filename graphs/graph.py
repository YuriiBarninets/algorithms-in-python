class Vertex:
    def __init__(self, label, directed=True):
        self.__label = label
        self.__directed = directed
        self.__edges = []

    def __str__(self):
        outbound_edges_str = ""
        for edge in self.get_outbound_edges():
            outbound_edges_str += str(edge) + ", "

        inbound_edges_str = ""
        for edge in self.get_inbound_edges():
            inbound_edges_str += str(edge) + ", "

        return "Vertex : {0}, Outbound edges : {1}, Inbound edges : {2}".format(self.__label,
                                                                                outbound_edges_str, inbound_edges_str)

    def get_outbound_edges(self):
        if self.__directed == False:
            return self.__edges

        outbound_edges = []
        for edge in self.__edges:
            if edge.get_start_vertex() == self:
                outbound_edges.append(edge)

        return outbound_edges

    def get_inbound_edges(self):
        if self.__directed == False:
            return self.__edges

        inbound_edges = []
        for edge in self.__edges:
            if edge.get_end_vertex() == self:
                inbound_edges.append(edge)

        return inbound_edges

    def get_edges(self):
        return self.__edges

    def get_label(self):
        return self.__label

    def add_edge(self, edge):
        self.__edges.append(edge)

    def remove_edge(self, edge):
        if edge in self.__edges:
            self.__edges.remove(edge)
        else:
            raise ValueError(
                "Can not find edge {0} in vertex {1}".format(str(edge), str(self)))

    def __eq__(self, other):
        return self.__label == other.get_label()

    def __hash__(self):
        return hash(self.get_label())


class Edge:
    def __init__(self, start_vertex, end_vertex, weight=1, directed=True):
        self.__start_vertex = start_vertex
        self.__end_vertex = end_vertex
        self.__weight = weight
        self.__directed = directed

    def __str__(self):
        if self.__directed:
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
        return self.__weight < other.get_weight()

    def __eq__(self, other):
        weight_equal = self.__weight == other.get_weight()
        start_vertex_equal = self.__start_vertex == other.get_start_vertex()
        end_vertex_equal = self.__end_vertex == other.get_end_vertex()

        return weight_equal == start_vertex_equal == end_vertex_equal == True


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
        start_vertex = self.__vertices[start_label]
        end_vertex = self.__vertices[end_label]
        edge = Edge(start_vertex, end_vertex, weight, self.__directed)

        start_vertex.add_edge(edge)
        if start_vertex != end_vertex:
            end_vertex.add_edge(edge)

        self.__edges.append(edge)

    def remove_edge(self, start_label, end_label, weight=1):
        start_vertex = self.__vertices[start_label]
        end_vertex = self.__vertices[end_label]
        edge = Edge(start_vertex, end_vertex, weight, self.__directed)

        start_vertex.remove_edge(edge)
        end_vertex.remove_edge(edge)
        self.__edges.remove(edge)

    def remove_vertex(self, vertex_label):
        vertex = self.__vertices[vertex_label]

        # remove outbound edges to this vertex for all adjacent vertices
        # remove outbound edges from graph
        for edge in vertex.get_inbound_edges():
            adjacent_vertex = edge.get_start_vertex()
            adjacent_vertex.remove_edge(edge)
            self.__edges.remove(edge)

        # remove inbound edges from this vertex to all adjacent vertices
        # remove inbound edges from graph
        for edge in vertex.get_outbound_edges():
            adjacent_vertex = edge.get_end_vertex()
            adjacent_vertex.remove_edge(edge)
            self.__edges.remove(edge)

        # remove vertex from graph
        self.__vertices.pop(vertex_label)

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

    def is_directed(self):
        return self.__directed


if __name__ == "__main__":
    test_graph = Graph(True)

    test_graph.add_vertex("a")
    test_graph.add_vertex("b")
    test_graph.add_vertex("c")

    test_graph.add_edge("a", "b", 2)
    test_graph.add_edge("a", "c", 7)
    test_graph.add_edge("c", "b", 1)
    test_graph.add_edge("b", "c", 3)
