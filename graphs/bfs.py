from packages.graph import Graph, display_graph
from collections import deque


def bfs(start_vertex):
    """"
    BFS(Breadth-First Search) use queue to manage incoming vertices
    BFS can be used to find the shortest path in unweighted graph
    """
    # initially, the queue contains only the start vertex and visited_vertices is empty
    queue = deque()
    queue.append(start_vertex)
    visited_vertices = set()

    result = []
    while len(queue) > 0:
        # 1. pop a vertex from the queue
        current_vertex = queue.popleft()

        # 2. ignoring this vertex if it has been visited
        if current_vertex in visited_vertices:
            continue

        # 3. mark as visited, so we will not visit it anymore
        visited_vertices.add(current_vertex)
        result.append(current_vertex.get_label())

        # 4. get all adjacent vertices which HAVE NOT been visited
        adjacent_vertices = []
        for edge in current_vertex.get_outbound_edges():
            adjacent_vertex = edge.get_end_vertex()
            if adjacent_vertex not in visited_vertices:
                adjacent_vertices.append(adjacent_vertex)

        # if necessary we may do some manipulation with adjacent_vertices, e.g. sort them
        # 5. add all adjacent vertices to the queue(BFS)
        queue.extend(adjacent_vertices)

    return result


if __name__ == "__main__":
    graph = Graph()

    graph.add_vertex("Jhon")
    graph.add_vertex("Sophia")
    graph.add_vertex("Emma")
    graph.add_vertex("Mark")
    graph.add_vertex("Alice")
    graph.add_vertex("Jeff")
    graph.add_vertex("George")

    graph.add_edge("Jhon", "Sophia")
    graph.add_edge("Jhon", "Emma")
    graph.add_edge("Jhon", "Mark")
    graph.add_edge("Sophia", "Emma")
    graph.add_edge("Sophia", "Alice")
    graph.add_edge("Emma", "Sophia")
    graph.add_edge("Emma", "Jeff")
    graph.add_edge("Jeff", "George")

    display_graph(graph, "Input graph for Breadth-First Search")

    vertices = bfs(graph.get_vertex("Jhon"))
    for vertex in vertices:
        print(vertex)
