class Solution:
    def add_to(self, graph, cycle):
        """
        adds all edges of cycle to the graph
        :param graph: list of achievable nodes from each node (index)
        :param cycle: list of ints-nodes which form cycle
        :return: None (only changes given graph)
        """
        for i in range(1, len(cycle)):
            fr = cycle[i - 1]
            to = cycle[i]
            graph[fr].append(to)

    def build_graph(
        self, n: int, requests: list[list[int]]
    ) -> list[list[int]]:
        """
        makes list of lists which represents the graph
        :param n: number of nodes
        :param requests: list of directed edges. Edge is a list
                        of two ints (first - from and second  - to)
        :return: list of achievable nodes from each node (index)
        """
        result = [[] for _ in range(n)]
        for fr, to in requests:
            result[fr].append(to)
        return result

    def choosing(self, graph, cycles: list[list[int]], i: int) -> int:
        if i == len(cycles):
            return 0
        cycle = cycles[i]
        if len(cycle) == 2 and self.is_present(cycle, graph):
            self.remove_from(graph, cycle)
            with_curr = 1 + self.choosing(graph, cycles, i + 1)
            self.add_to(graph, cycle)
            return with_curr
        without_curr = self.choosing(graph, cycles, i + 1)
        if self.is_present(cycle, graph):
            self.remove_from(graph, cycle)
            with_curr = len(cycle) - 1 + self.choosing(graph, cycles, i + 1)
            self.add_to(graph, cycle)
            return max(with_curr, without_curr)
        else:
            return without_curr

    def find_all_cycles(
        self, graph: list[list[int]], n: int
    ) -> list[list[int]]:
        """
        searches for and returns all cycled edges in given graph
        :param graph: list of achievable nodes from each node (index)
        :param n: number of nodes
        :return: list of all cycles inside the graph
        """
        cycles = []

        def traverse(node_from, node_to, graph, track, cycles):
            for neib in graph[node_from]:
                if neib == node_to:
                    cycles.append(track + [neib])
                    continue
                if neib in track or neib < node_to:
                    continue
                track.append(neib)
                traverse(neib, node_to, graph, track, cycles)
                track.pop()

        for node in range(n):
            traverse(node, node, graph, [node], cycles)

        return cycles

    def is_present(self, cycle, graph) -> bool:
        """
        checks if cycle is still in graph after deleting longer cycles
        :param cycle: list of ints-nodes which form cycle
        :param graph: list of achievable nodes from each node (index)
        :return: True if cycle is in graph else False
        """
        for i in range(1, len(cycle)):
            fr = cycle[i - 1]
            to = cycle[i]
            if to not in graph[fr]:
                return False
        return True

    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        """
        :param n: number of buildings (nodes in graph)
        :param requests: list of directed edges. Edge is a list
                        of two ints (first - from and second  - to)
        :return: maximal number of achievable requests
        """
        graph = self.build_graph(n, requests)
        cycles = self.find_all_cycles(graph, n)
        ans = self.choosing(graph, cycles, 0)
        return ans

    def remove_from(self, graph, cycle):
        """
        removes all edges from graph which form given cycle
        :param graph: list of achievable nodes from each node (index)
        :param cycle: list of ints-nodes which form cycle
        :return: None (only changes given graph)
        """
        for i in range(1, len(cycle)):
            fr = cycle[i - 1]
            to = cycle[i]
            graph[fr].remove(to)


class Solution2:

    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        ans = 0
        graph = [[] for _ in range(n)]
        for fr, to in requests:
            if fr == to:
                ans += 1
            else:
                graph[fr].append(to)

        cycles = []

        def traverse(node_from, node_to, track):
            for neib in graph[node_from]:
                if neib == node_to:
                    cycles.append(track + [neib])
                    continue
                if neib < node_to or neib in track:
                    continue
                track.append(neib)
                traverse(neib, node_to, track)
                track.pop()

        for node in range(n):
            traverse(node, node, [node])

        def backtrack(i: int) -> int:
            if i == len(cycles):
                return 0
            cycle = cycles[i]

            is_present = True
            for j in range(1, len(cycle)):
                if cycle[j] not in graph[cycle[j - 1]]:
                    is_present = False
                    break

            if is_present:
                for j in range(1, len(cycle)):
                    graph[cycle[j - 1]].remove(cycle[j])
                with_curr = len(cycle) - 1 + backtrack(i + 1)
                for j in range(1, len(cycle)):
                    graph[cycle[j - 1]].append(cycle[j])
                if len(cycle) == 2:
                    return with_curr
                else:
                    return max(with_curr, backtrack(i + 1))
            else:
                return backtrack(i + 1)

        ans += backtrack(0)
        return ans


class Solution3:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        state = [0] * n

        def backtrack(i):
            if i == len(requests):
                return -100 if any(state) else 0
            fr, to = requests[i]
            state[fr] -= 1
            state[to] += 1
            with_curr = 1 + backtrack(i + 1)
            state[fr] += 1
            state[to] -= 1
            if fr == to:
                return with_curr
            else:
                without_curr = backtrack(i + 1)
                return max(with_curr, without_curr)

        return backtrack(0)


def main():
    sol = Solution3()
    print("3 ===", sol.maximumRequests(3, [[0, 0], [1, 2], [2, 1]]))
    print("4 ===", sol.maximumRequests(4, [[0, 3], [3, 1], [1, 2], [2, 0]]))
    print(
        "5 ===",
        sol.maximumRequests(
            5, [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]
        ),
    )
    print(
        "3 ===",
        sol.maximumRequests(
            5, [[1, 2], [2, 1], [2, 3], [3, 1], [4, 3], [4, 0], [0, 1]]
        ),
    )
    print(
        "6 ===",
        sol.maximumRequests(
            5, [[1, 2], [2, 1], [2, 3], [3, 1], [4, 3], [1, 0], [0, 4]]
        ),
    )
    print(
        "8 ===",
        sol.maximumRequests(
            3,
            [
                [2, 2],
                [2, 0],
                [1, 1],
                [2, 1],
                [1, 1],
                [2, 2],
                [1, 0],
                [0, 2],
                [1, 2],
            ],
        ),
    )


if __name__ == "__main__":
    main()
