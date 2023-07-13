class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        cycled = set()
        ans = set()

        def lead_to_cycle(node: int, track: set):
            if node in ans or node in cycled:
                return
            for neib in graph[node]:
                if neib in track:
                    cycled.add(node)
                    return
                track.add(neib)
                lead_to_cycle(neib, track)
                if neib in cycled:
                    cycled.add(node)
                    return
                track.remove(neib)
            ans.add(node)
            return

        for i in range(len(graph)):
            lead_to_cycle(i, {i})
        return sorted(ans)


def main():
    sol = Solution()
    print(' [2, 4, 5, 6]\n', sol.eventualSafeNodes(graph=[[1, 2], [2, 3], [5], [0], [5], [], []]))
    print(' [4]\n', sol.eventualSafeNodes(graph=[[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]))


if __name__ == '__main__':
    main()
