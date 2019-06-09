from packages.graph import Graph, display_graph
import math
import heapq


def dijkstra(graph, start_vertex):
    # 1. Shortest distance to each vertex is infinity and to start vertex equal to 0
    distances = {
        vertex: math.inf for vertex in graph.get_vertices().values()}
    distances[start_vertex] = 0

    # 2. create a list with unvisited vertices
    univisited_vertices = graph.get_vertices().copy()
    while len(univisited_vertices) > 0:

        # 3. find a vertex with minimum distance among unvisited vertices
        min_distance_heap = []
        for vertex in univisited_vertices.values():
            heapq.heappush(min_distance_heap,
                           (distances[vertex], vertex.get_label()))

        min_distance, min_vertex_label = heapq.heappop(min_distance_heap)
        univisited_vertices.pop(min_vertex_label)

        # 4. check if there is a better path from min distance vertex to each adjacent vertex
        min_vertex = graph.get_vertex(min_vertex_label)
        for edge in min_vertex.get_outbound_edges():
            new_distance = min_distance + edge.get_weight()

            # 4. write the new distance to adjacent vertex if we have found a better path
            adjacent_vertex = edge.get_end_vertex()
            if new_distance < distances[adjacent_vertex]:
                distances[adjacent_vertex] = new_distance

    return distances


if __name__ == "__main__":
    graph = Graph()

    graph.add_vertex("a")
    graph.add_vertex("b")
    graph.add_vertex("c")
    graph.add_vertex("d")
    graph.add_vertex("e")
    graph.add_vertex("f")

    graph.add_edge("a", "b", 2)
    graph.add_edge("a", "c", 4)
    graph.add_edge("b", "c", 1)
    graph.add_edge("c", "d", 5)
    graph.add_edge("c", "e", 3)
    graph.add_edge("d", "e", 1)
    graph.add_edge("e", "f", 8)

    display_graph(graph, "Input graph for Dijkstra's algorithm")

    shortest_distances_to_vertices = dijkstra(graph, graph.get_vertex("a"))
    for vertex, distance in shortest_distances_to_vertices.items():
        print("Vertex {0}, Distance {1}".format(vertex.get_label(), distance))
