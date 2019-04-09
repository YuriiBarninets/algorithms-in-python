from graph import *

def bfs_shortest_path(graph, start, goal):
    """
    When we use BFS to find a shortest path we have to track path from source to goal.
    1. We may store parent vertex for each child, so this let us to get a path from goal to start
    when we hit a goal.
    2. We may store in queue list with path to vertex instead of single vertex, so the last item in list will
    represent a current vertex (we use this approach in the algorithm below)
    """
    if start == goal:
        return start

    # initially, queue contains only the list with start vertex
    queue = [[start]]

    # initially, all vertices are not visited
    visited_vertices = {}
    for vertex in graph.vertices:
        visited_vertices[vertex.label] = False

    while len(queue) > 0:
        # pop a vertex from the queue
        path_to_vertex = queue.pop(0)
        current_vertex = path_to_vertex[-1]

        # ignoring this vertex if it has been visited
        if visited_vertices[current_vertex.label] is True:
            continue

        # return path to vertex if we find goal vertex
        if current_vertex == goal:
            return path_to_vertex

        # mark as visited, so we will not visit it anymore
        visited_vertices[current_vertex.label] = True

        # get all adjacent vertices which HAVE NOT been visited
        adjacent_vertices = []
        for edge in current_vertex.outbound_edges:
            if visited_vertices[edge.end_vertex.label] is False:
                adjacent_vertices.append(edge.end_vertex)

        # push a list with path to each adjacent vertex in our queue
        for adjacent_vertex in adjacent_vertices:
            new_path = path_to_vertex.copy()
            new_path.append(adjacent_vertex)
            queue.append(new_path)

    # return None if there no a path between start and goal vertices
    return None


if __name__ == "__main__":
    # vertices
    a = Vertex("a")
    b = Vertex("b")
    c = Vertex("c")
    d = Vertex("d")
    e = Vertex("e")
    f = Vertex("f")

    # a --> b, a --> c, a --> d
    a.outbound_edges.append(Edge(a, b))
    a.outbound_edges.append(Edge(a, c))
    a.outbound_edges.append(Edge(a, d))

    # b --> c, b --> f
    b.outbound_edges.append(Edge(b, c))
    b.outbound_edges.append(Edge(b, f))

    # c --> d
    c.outbound_edges.append(Edge(c, d))

    # d --> e
    d.outbound_edges.append(Edge(d, e))

    # e --> f
    e.outbound_edges.append(Edge(e, f))

    # graph
    vertices = [a, b, c, d, e, f]
    all_edges = []

    for vertex in vertices:
        all_edges.extend(vertex.outbound_edges)

    graph = Graph(vertices, all_edges)

    shortest_path = bfs_shortest_path(graph, a, f)

    if shortest_path:
        for vertex in shortest_path:
            print(vertex)
    else:
        print("There no path between {0} & {1}".format(a.label, f.label))
