from graph import Graph

graph = {
    'A': ['B', 'E', 'H'],
    'B': ['C', 'D'],
    'E': ['F', 'G'],
    'H': ['G', 'I'],
    'C': [],
    'D': [],
    'F': [],
    'I': [],
    'G': []
}
if __name__ == '__main__':
    g = Graph()
    g.set_graph(graph)
    g.print_graph()
    print("Visited Nodes :", g.BFS('A', 'F'))
    print("path to goal :", g.path_to_goal('A', 'F'))
