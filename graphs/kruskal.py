from graph import Graph
from collections import deque
import heapq
import graph_visualizer


def has_cycle(graph):
    """
    Use DFS algorithm to check if this graph has a cycle
    If there is an adjacent vertex that has been already visited
    and this vertex is not previous(parent) then there is a cycle in graph.
    """
    stack = deque()
    visited_vertices = set()

    random_vertex = next(iter(graph.get_vertices().values()))
    prev_vertex = random_vertex
    vertex = random_vertex

    # prev_vertex let us to track "parent" vertex in undirected graph
    stack.append((prev_vertex, vertex))

    while len(stack) > 0:
        prev, vertex = stack.pop()

        visited_vertices.add(vertex)

        for adjacent_edge in vertex.get_outbound_edges():
            # this graph is undirected, so end_vertex may be start_vertex and vice versa
            if vertex != adjacent_edge.get_end_vertex():
                adjacent_vertex = adjacent_edge.get_end_vertex()
            else:
                adjacent_vertex = adjacent_edge.get_start_vertex()

            # If there is an adjacent vertex that has been already visited
            # and this vertex is not previous(parent) then there is a cycle in graph.
            if adjacent_vertex in visited_vertices and adjacent_vertex != prev:
                return True

            if adjacent_vertex not in visited_vertices:
                stack.append((vertex, adjacent_vertex))

    return False


def mst_kruskal(graph):
    # Kruskal's algorithm explanation https://www.youtube.com/watch?v=71UQH7Pr9kU
    mst = Graph(False)
    min_edge_heap = []  # use as priority queue to select and edge with minimum weight

    # 1. Sort the edges in ascending order of weights
    for edge in graph.get_edges():
        heapq.heappush(min_edge_heap, edge)

    input_graph_num_vertices = len(graph.get_vertices())
    # 2. Keep adding edges until MST will reach all vertices
    while (len(min_edge_heap) > 0) and (len(mst.get_vertices()) < input_graph_num_vertices):
        # 3. Select an edge with minimum weight (greedy algorithm)
        min_edge = heapq.heappop(min_edge_heap)
        start_vertex = min_edge.get_start_vertex()
        end_vertex = min_edge.get_end_vertex()

        # 4. Add edge in MST and check if it form a cycle then remove edge, otherwise leave it in MST
        mst.add_vertex(start_vertex.get_label())
        mst.add_vertex(end_vertex.get_label())

        start_label = start_vertex.get_label()
        end_label = end_vertex.get_label()
        weight = min_edge.get_weight()
        mst.add_edge(start_label, end_label, weight)

        if has_cycle(mst):
            mst.remove_edge(start_label, end_label, weight)

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

    graph_visualizer.visualize(graph, "Input graph for Kruskal's algorithm")

    mst = mst_kruskal(graph)

    graph_visualizer.visualize(mst, "Minimum spanning tree")
