class Graph:

    def __init__(self):
        # make private instances
        print("Graph Constructor has been called\n")
        self.__frontier = []  # list
        self.__visited = []  # list
        self.__graph = {}  # dictionary
        self.__parent = {}  # dictionary

    def get_frontier(self):  # get frontier --> return the queue
        return self.__frontier

    def get_visited(self):  # get visited  ---> return the visiting nodes
        return self.__visited

    def __push_node(self, node):  # push node in frontier
        self.__frontier.append(node)

    def __pop_node(self):  # remove a node from frontier
        return self.__frontier.pop(0)

    def set_graph(self, g):  # set the graph
        self.__graph = g

    def get_graph(self):  # get graph
        return self.__graph

    def print_graph(self):  # display graph
        print(self.__graph)

    # path to goal finder
    def path_to_goal(self, start_node, end_node):
        path = [end_node]
        while path[-1] != start_node:
            path.append(self.__parent[path[-1]])
        path.reverse()
        return path

    def BFS(self, start_state, goal_state):   # breath first search
        self.__push_node(start_state)
        node = self.__pop_node()

        while node != goal_state:
            self.__visited.append(node)
            neighbours = self.__graph[node]
            for nodes in neighbours:
                if nodes not in self.__visited:
                    if nodes not in self.__frontier:
                        self.__parent[nodes] = node
                        self.__push_node(nodes)

            node = self.__pop_node()
            if node == goal_state:
                print("goal found")

        return self.__visited
