from graph import *

# BFS use queue to manage incoming vertices
# DFS use stack to manage incoming vertices
# breadth first search
def bfs(graph, start_vertex):
    # Initially, the queue(BFS)/stack(DFS) contains the start vertex
    queue = [start_vertex]

    # All vertices are not visited
    visited_vertices = {}
    for vertex in graph.vertices:
        visited_vertices[vertex.label] = False

    result = []
    while len(queue) > 0:
        # 1. pop a vertex from the queue(BFS)/stack(DFS)
        current_vertex = queue.pop(0) # Change on queue.pop() and you get DFS

        # 2. ignoring this vertex if it has been visited
        if visited_vertices[current_vertex.label]:
            continue

        # 3. mark as visited, so we will not visit it anymore, DO some operation on vertex if necessary
        result.append(current_vertex.label)
        visited_vertices[current_vertex.label] = True

        # 4. get all adjacent vertices which HAVE NOT been visited
        adjacent_vertices = []
        for edge in current_vertex.outbound_edges:
            if visited_vertices[edge.end_vertex.label] is False:
                adjacent_vertices.append(edge.end_vertex)

        # if necessary we may do some manipulation with adjacent_vertices, e.g. sort them

        # 5. add all adjacent vertices to the queue(BFS)/stack(DFS)
        queue.extend(adjacent_vertices)

    return result


if __name__ == "__main__":
    # vertices
    Jhon = Vertex("Jhon")
    Sophia = Vertex("Sophia")
    Emma = Vertex("Emma")
    Mark = Vertex("Mark")
    Alice = Vertex("Alice")
    Jeff = Vertex("Jeff")
    George = Vertex("George")

    # edge Jhon --> Sophia
    # edge Jhon --> Emma
    # edge Jhon --> Mark
    Jhon.outbound_edges.append(Edge(Jhon, Sophia))
    Jhon.outbound_edges.append(Edge(Jhon, Emma))
    Jhon.outbound_edges.append(Edge(Jhon, Mark))

    # edge Sophia --> Emma
    # edge Sophia --> Alice
    Sophia.outbound_edges.append(Edge(Sophia, Emma))
    Sophia.outbound_edges.append(Edge(Sophia, Alice))

    # edge Emma --> Sophia
    # edge Emma --> Jeff
    Emma.outbound_edges.append(Edge(Emma, Sophia))
    Emma.outbound_edges.append(Edge(Emma, Jeff))

    # edge Jeff --> George
    Jeff.outbound_edges.append(Edge(Jeff, George))

    # graph
    vertices = [Jhon, Sophia, Emma, Alice, Jeff, Mark, George]
    edges = []

    for vertex in vertices:
        edges.extend(vertex.outbound_edges)

    graph = Graph(vertices, edges)

    labels = bfs(graph, Jhon)
    for label in labels:
        print(label)
