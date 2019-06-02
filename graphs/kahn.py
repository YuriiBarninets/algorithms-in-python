from graph import Graph
from queue import Queue
import graph_visualizer


def topological_sorting(graph):
    zero_indegree_vertices = Queue()
    topological_order = []
    indegree_dict = {}

    # 1. calculate indegree for each vertex in graph
    for vertex_label in graph.get_vertices():
        indegree_dict[vertex_label] = graph.get_indegree(vertex_label)

        if indegree_dict[vertex_label] == 0:
            zero_indegree_vertices.put(vertex_label)

    while not zero_indegree_vertices.empty():
        vertex_label = zero_indegree_vertices.get()

        # 2. vertex with zero indegree must be added to topological order
        topological_order.append(vertex_label)

        # 3. zero indegree vertex has been added to topological order,
        # so decrement indegree for all adjacent vertices
        for edge in graph.get_vertex(vertex_label).get_outbound_edges():
            adjacent_vertex_label = edge.get_end_vertex().get_label()
            indegree_dict[adjacent_vertex_label] = indegree_dict[adjacent_vertex_label] - 1

            if indegree_dict[adjacent_vertex_label] == 0:
                zero_indegree_vertices.put(adjacent_vertex_label)

    if len(topological_order) != len(graph.get_vertices()):
        raise ValueError("This graph is cyclic")

    return topological_order


if __name__ == "__main__":
    dag = Graph()  # directed acyclic graph

    # vertices
    dag.add_vertex("0")
    dag.add_vertex("1")
    dag.add_vertex("2")
    dag.add_vertex("3")
    dag.add_vertex("4")
    dag.add_vertex("5")
    dag.add_vertex("6")
    dag.add_vertex("7")
    dag.add_vertex("8")

    # edges
    dag.add_edge("0", "1")
    dag.add_edge("1", "2")
    dag.add_edge("1", "5")
    dag.add_edge("2", "3")
    dag.add_edge("2", "4")
    dag.add_edge("3", "4")
    dag.add_edge("3", "6")
    dag.add_edge("5", "6")
    dag.add_edge("6", "8")
    dag.add_edge("8", "7")

    graph_visualizer.visualize(dag, "Input graph for Kahn's algorithm")

    topological_order = topological_sorting(dag)
    print(topological_order)
