from graph import Graph
from collections import deque


def dfs(graph, start_vertex):
    """"
    DFS(Depth-First Search) use stack to manage incoming vertices
    DFS can be used to generate a maze or to find cycles in a graph
    """
    # initially, the stack contains only the start vertex
    # and all vertices are not visited
    stack = deque()
    stack.append(start_vertex)
    visited_vertices = {}
    for vertex in graph.get_vertices():
        visited_vertices[vertex] = False

    result = []
    while len(stack) > 0:
        # 1. pop a vertex from the stack
        current_vertex = stack.pop()

        # 2. ignoring this vertex if it has been visited
        if visited_vertices[current_vertex.get_label()]:
            continue

        # 3. mark as visited, so we will not visit it anymore, DO some operation on vertex if necessary
        result.append(current_vertex.get_label())
        visited_vertices[current_vertex.get_label()] = True

        # 4. get all adjacent vertices which HAVE NOT been visited
        adjacent_vertices = []
        for edge in current_vertex.get_outbound_edges():
            if visited_vertices[edge.get_end_vertex().get_label()] is False:
                adjacent_vertices.append(edge.get_end_vertex())

        # if necessary we may do some manipulation with adjacent_vertices, e.g. sort them

        # 5. add all adjacent vertices to the queue(BFS)/stack(DFS)
        stack.extend(adjacent_vertices)

    return result


if __name__ == "__main__":

    # vertices
    graph = Graph()
    graph.add_vertex("Jhon")
    graph.add_vertex("Sophia")
    graph.add_vertex("Emma")
    graph.add_vertex("Mark")
    graph.add_vertex("Alice")
    graph.add_vertex("Jeff")
    graph.add_vertex("George")

    # edge Jhon --> Sophia
    # edge Jhon --> Emma
    # edge Jhon --> Mark
    graph.add_edge("Jhon", "Sophia")
    graph.add_edge("Jhon", "Emma")
    graph.add_edge("Jhon", "Mark")

    # edge Sophia --> Emma
    # edge Sophia --> Alice
    graph.add_edge("Sophia", "Emma")
    graph.add_edge("Sophia", "Alice")

    # edge Emma --> Sophia
    # edge Emma --> Jeff
    graph.add_edge("Emma", "Sophia")
    graph.add_edge("Emma", "Jeff")

    # edge Jeff --> George
    graph.add_edge("Jeff", "George")

    vertices = dfs(graph, graph.get_vertex("Jhon"))
    for vertex in vertices:
        print(vertex)
