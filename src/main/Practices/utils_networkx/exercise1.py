import networkx as nx
from src.main.Practices.utils_networkx.style_graph import GraphStyle, build_graph, theme_palette

def get_graph_data():
    return [
        ("Z", "E", 3), ("Z", "F", 2),
        ("Z", "C", 1), ("F", "E", 1),
        ("F", "C", 1), ("E", "D", 2),
        ("C", "B", 5), ("D", "G", 1),
        ("B", "G", 1), ("B", "A", 4),
        ("G", "A", 2), ("D", "A", 5)
    ]

def draw_graph(graph):
    style = GraphStyle(node_color=theme_palette[2]["node"], edge_color=theme_palette[2]["edge"])
    style.draw_graph_pyvis(graph, "Exercise1 Dijkstra Graph")

def display_graph_info(graph):
    print("\nNumber of NODES:", graph.number_of_nodes())
    print("⤵️  All NODES ")
    print(graph.nodes())

    print("\nNumber of EDGES:", graph.number_of_edges())
    print("⤵️  All EDGES")
    for i, edge in enumerate(graph.edges(), start=1):
        if i % 2 == 0:
            print(edge)
        else:
            print(edge, end=' ')

    shortest_path = nx.dijkstra_path(graph, "Z", "A")
    path_length = nx.dijkstra_path_length(graph, "Z", "A")

    print("\n" + "=" * 60)
    print("⏹️  Shortest path from Z to A:", shortest_path)
    print("⏹️  Shortest path length:", path_length)
    print("=" * 60)

    adj_matrix = nx.adjacency_matrix(graph)
    print("\nAdjacency Matrix:")
    print(adj_matrix.todense())
    print()

    inc_matrix = nx.incidence_matrix(graph)
    print("Incidence Matrix:")
    print(inc_matrix.todense())
    print()

def run_exercise_1():
    print("\nUse Dijkstra’s algorithm to find the shortest path between")
    print("vertices Z and A in the given weighted graph. Draw the graph.")
    graph = build_graph(get_graph_data())
    draw_graph(graph)
    display_graph_info(graph)
