from graph import *
import math


def dijkstra(graph, start_vertex):
    # Initially, shortest distance to each vertex is infinity,
    # and the shortest distance to start vertex equal to 0
    distances = {vertex.label: math.inf for vertex in graph.vertices}
    distances[start_vertex.label] = 0

    # list of vertices that must be visited
    vertices_to_visit = graph.vertices.copy()

    while len(vertices_to_visit) > 0:
        shortest_distance_vertex = vertices_to_visit[0]

        # looking for the unvisited vertex with the minimum distance
        # Idea : use BinaryHeap in order to get a vertex with minimum distance
        for vertex in vertices_to_visit:
            if distances[vertex.label] < distances[shortest_distance_vertex.label]:
                shortest_distance_vertex = vertex

        vertices_to_visit.remove(shortest_distance_vertex)

        # for each adjacent vertex check if there is better path
        for edge in shortest_distance_vertex.outbound_edges:
            adjacent_vertex = edge.end_vertex
            new_distance = distances[shortest_distance_vertex.label] + edge.weight

            # write the new distance to adjacent vertex if we have found a better path
            if new_distance < distances[adjacent_vertex.label]:
                distances[adjacent_vertex.label] = new_distance

    return distances


if __name__ == "__main__":
    print("Dijkstra algorithm")
    # vertices
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")

    # a -2-> b, a -4-> c
    a.outbound_edges.append(Edge(a, b, 2))
    a.outbound_edges.append(Edge(a, c, 4))

    # b -4-> c
    b.outbound_edges.append(Edge(b, c, 4))

    # c -5-> d, c -3-> e
    c.outbound_edges.append(Edge(c, d, 5))
    c.outbound_edges.append(Edge(c, e, 3))

    # d -1-> e
    d.outbound_edges.append(Edge(d, e, 1))

    # e -9-> f
    e.outbound_edges.append(Edge(e, f, 9))

    # graph
    vertices = [a, b, c, d, e, f]
    all_edges = []

    for vertex in vertices:
        all_edges.extend(vertex.outbound_edges)

    graph = Graph(vertices, all_edges)
    shortest_distances_to_vertices = dijkstra(graph, a)
    print(shortest_distances_to_vertices)
