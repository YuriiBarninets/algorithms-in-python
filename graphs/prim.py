from graph import Graph
import heapq


def mst_prim(graph):
    # Prim's algorithm explanation https://www.youtube.com/watch?v=cplfcGZmX7I
    # This algorithm return list of edges, so if we have edges we may recreate MST
    mst_edges_result = []
    heap = []
    visited_vertices = {
        vertex_label: False for vertex_label in graph.get_vertices()}

    # 1. Choose arbitary vertex from which MST algorithm start looking for edges
    arbitary_vertex = next(iter(graph.get_vertices()))
    visited_vertices[arbitary_vertex] = True

    # 2. Find all adjacent vertices of arbitary vertex and add them to heap
    for edge in graph.get_vertex(arbitary_vertex).get_outbound_edges():
        heapq.heappush(heap, edge)

    while len(mst_edges_result) < len(graph.get_vertices()) - 1:
        # 2. Select an edge with minimum weight (greedy algorithm)
        while True:
            min_edge = heapq.heappop(heap)
            min_vertex_label = min_edge.get_end_vertex().get_label()
            if visited_vertices[min_vertex_label] == False:
                break

        # 3. Add selected edge to MST
        mst_edges_result.append(min_edge)
        visited_vertices[min_vertex_label] = True

        # 4. Find all adjacent vertices of min vertex and add them to heap
        for edge in graph.get_vertex(min_vertex_label).get_outbound_edges():
            heapq.heappush(heap, edge)

    return mst_edges_result


if __name__ == "__main__":
    graph = Graph(False)  # undirected weighted graph

    graph.add_vertex("a")
    graph.add_vertex("b")
    graph.add_vertex("c")
    graph.add_vertex("d")
    graph.add_vertex("e")
    graph.add_vertex("f")
    graph.add_vertex("g")

    graph.add_edge("a", "b", 2)
    graph.add_edge("a", "c", 3)
    graph.add_edge("a", "d", 3)
    graph.add_edge("b", "c", 4)
    graph.add_edge("b", "e", 3)
    graph.add_edge("c", "d", 5)
    graph.add_edge("c", "f", 6)
    graph.add_edge("c", "e", 1)
    graph.add_edge("d", "f", 7)
    graph.add_edge("e", "f", 8)
    graph.add_edge("f", "g", 9)

    mst_edges = mst_prim(graph)

    for edge in mst_edges:
        print(edge)
