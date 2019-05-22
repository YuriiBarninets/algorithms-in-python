from graph import *
import math


def dijkstra(graph, start_vertex):
    # Initially, shortest distance to each vertex is infinity,
    # and the shortest distance to start vertex equal to 0
    distances = {
        vertex: math.inf for vertex in graph.get_vertices().keys()}
    distances[start_vertex.get_label()] = 0

    # create list of vertices that must be visited
    vertices_to_visit = graph.get_vertices().copy()

    while len(vertices_to_visit) > 0:
        shortest_distance_vertex = list(vertices_to_visit.values())[0]

        # looking for the unvisited vertex with the MINIMUM distance
        # Idea : use BinaryHeap in order to get a vertex with minimum distance
        for vertex in vertices_to_visit.values():
            if distances[vertex.get_label()] < distances[shortest_distance_vertex.get_label()]:
                shortest_distance_vertex = vertex

        vertices_to_visit.pop(shortest_distance_vertex.get_label())

        # check if there is a better path from shortest distance vertex to each adjacent vertex
        for edge in shortest_distance_vertex.get_outbound_edges():
            new_distance = distances[shortest_distance_vertex.get_label(
            )] + edge.get_weight()

            # write the new distance to adjacent vertex if we have found a better path
            adjacent_vertex = edge.get_end_vertex()
            if new_distance < distances[adjacent_vertex.get_label()]:
                distances[adjacent_vertex.get_label()] = new_distance

    return distances


if __name__ == "__main__":
    print("Dijkstra algorithm")

    # vertices
    graph = Graph()
    graph.add_vertex("a")
    graph.add_vertex("b")
    graph.add_vertex("c")
    graph.add_vertex("d")
    graph.add_vertex("e")
    graph.add_vertex("f")

    # a -2-> b, a -4-> c
    graph.add_edge("a", "b", 2)
    graph.add_edge("a", "c", 4)

    # b -4-> c
    graph.add_edge("b", "c", 1)

    # c -5-> d, c -3-> e
    graph.add_edge("c", "d", 5)
    graph.add_edge("c", "e", 3)

    # d -1-> e
    graph.add_edge("d", "e", 1)

    # e -9-> f
    graph.add_edge("e", "f", 8)

    shortest_distances_to_vertices = dijkstra(graph, graph.get_vertex("a"))
    print(shortest_distances_to_vertices)
