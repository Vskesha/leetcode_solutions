class Graph:

    def __init__(self, nodes=None):
        self.nodes = nodes or {}

    def __repr__(self):
        return f"Graph({self.nodes})"

    def topological_sort(self):
        ans = []
        top_stack = []

        # filling stack with nodes with no incoming edges
        for node in self.nodes.values():  # node can be GraphNode or NodesGroup
            if node.income == 0:
                top_stack.append(node)
        nodes_left = len(self.nodes) - len(top_stack)
        while top_stack:
            # we pop one the node with no incoming edges
            # and decrease income of all neighboring vertices
            # and if it is zero we add this node to stack
            curr_node = top_stack.pop()
            for neib in curr_node.neighbours:
                neib.income -= 1
                if not neib.income:
                    top_stack.append(neib)
                    nodes_left -= 1

            # moving on the bottom level of graph
            if type(curr_node) is Graph:
                ans.extend(curr_node.topological_sort())
            elif type(curr_node) is NodesGroup:
                ans.extend(curr_node.topological_sort())
            elif type(curr_node) is GraphNode:
                ans.append(curr_node.value)
            else:
                raise ValueError(f"Incorrect value in {curr_node}")

        if nodes_left:  # there is a cycle in graph
            raise IndexError("It's impossible to sort")

        return ans


class GraphNode:

    def __init__(self, value=None, income=0, neighbours=None):
        self.value = value
        self.income = income
        self.neighbours = neighbours or []

    def __repr__(self):
        return f"GraphNode({self.value})"


class NodesGroup(Graph, GraphNode):

    def __init__(self, nodes=None, value=None, income=0, neighbours=None):
        super().__init__(nodes)
        super(Graph, self).__init__(value, income, neighbours)

    def __repr__(self):
        return f"NodeGroup({self.nodes})"


class Solution:
    def sortItems(
        self, n: int, m: int, group: list[int], beforeItems: list[list[int]]
    ) -> list[int]:
        # creating of graph with m empty groups
        graph = Graph()
        graph.nodes = {i: NodesGroup() for i in range(m)}

        # populating graph with GraphNodes in proper group
        over = m
        for i in range(n):
            if group[i] == -1:
                group[i] = over
                graph.nodes[over] = GraphNode(value=i)
                over += 1
            else:
                curr_nodes_group = graph.nodes[group[i]]
                curr_nodes_group.nodes[i] = GraphNode(i)

        # setting relations between groups and nodes in graph
        # using beforeItems and counting of incoming edges.
        # edges go from previous value to the following value
        for value in range(n):
            group_of_value = group[value]
            for value_before in beforeItems[value]:
                group_of_value_before = group[value_before]
                if group_of_value == group_of_value_before:
                    # value and value_before are in the same group
                    curr_nodes_group = graph.nodes[group_of_value]
                    node_after = curr_nodes_group.nodes[value]
                    node_before = curr_nodes_group.nodes[value_before]
                else:
                    node_after = graph.nodes[group_of_value]
                    node_before = graph.nodes[group_of_value_before]
                node_after.income += 1  # counting incoming edges
                node_before.neighbours.append(node_after)  # add edge

        # topological sorting
        try:
            return graph.topological_sort()
        except IndexError as e:  # there is a cycle in graph or in some group
            return []


def main():
    sol = Solution()
    print(
        " [6, 3, 4, 1, 5, 2, 0, 7]\n",
        sol.sortItems(
            n=8,
            m=2,
            group=[-1, -1, 1, 0, 0, 1, 0, -1],
            beforeItems=[[], [6], [5], [6], [3, 6], [], [], []],
        ),
    )
    print(
        " []\n",
        sol.sortItems(
            n=8,
            m=2,
            group=[-1, -1, 1, 0, 0, 1, 0, -1],
            beforeItems=[[], [6], [5], [6], [3], [], [4], []],
        ),
    )


if __name__ == "__main__":
    main()
