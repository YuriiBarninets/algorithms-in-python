from packages.graph import Graph, display_graph
import heapq


def mst_prim(graph):
    # Prim's algorithm explanation https://www.youtube.com/watch?v=cplfcGZmX7I
    # This algorithm return list of edges, so if we have edges we may recreate MST
    mst = Graph(False)
    min_edge_heap = []
    visited_vertices = set()

    # 1. Choose arbitary vertex from which MST algorithm start looking for edges
    arbitary_vertex = next(iter(graph.get_vertices()))
    visited_vertices.add(arbitary_vertex)
    mst.add_vertex(arbitary_vertex)

    # 2. Find all adjacent edges of arbitary vertex and add them to heap
    for edge in graph.get_vertex(arbitary_vertex).get_outbound_edges():
        heapq.heappush(min_edge_heap, edge)

    input_graph_num_vertices = len(graph.get_vertices())
    while len(mst.get_vertices()) < input_graph_num_vertices:
        # 3. Select an edge with minimum weight (greedy algorithm)
        while True:
            min_edge = heapq.heappop(min_edge_heap)
            min_vertex = min_edge.get_end_vertex()
            min_vertex_label = min_vertex.get_label()
            if min_vertex_label not in visited_vertices:
                break

        # 4. Mark selected vertex as visited and add selected edge to MST
        visited_vertices.add(min_vertex_label)
        mst.add_vertex(min_vertex_label)
        mst.add_edge(min_edge.get_start_vertex().get_label(),
                     min_edge.get_end_vertex().get_label(), min_edge.get_weight())

        # 4. Find all adjacent edges of min vertex and add them to heap
        for edge in min_vertex.get_outbound_edges():
            heapq.heappush(min_edge_heap, edge)

    return mst


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

    display_graph(graph, "Input graph for Prim's algorithm")

    mst = mst_prim(graph)

    display_graph(mst, "Minimum spanning tree")
