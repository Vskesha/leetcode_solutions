from heapq import heappop, heappush


class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start: int, end: int) -> float:
        graph = [{} for _ in range(n)]
        for edge, probability in zip(edges, succProb):
            fr, to = edge
            graph[fr][to] = probability
            graph[to][fr] = probability

        visited = set()
        priority = [(-1, start)]

        while priority:
            probability, curr = heappop(priority)
            visited.add(curr)
            if curr == end:
                return -probability
            for neib, pr in graph[curr].items():
                if neib not in visited:
                    heappush(priority, (pr * probability, neib))
        return 0


def main():
    sol = Solution()
    print('0.25000 ===', sol.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2))
    print('0.30000 ===', sol.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.3], start=0, end=2))
    print('0 ===', sol.maxProbability(n=3, edges=[[0, 1]], succProb=[0.5], start=0, end=2))
    print('0 ===', sol.maxProbability(n=10, edges=[[0, 3], [1, 7], [1, 2], [0, 9]], succProb=[0.31, 0.9, 0.86, 0.36], start=2, end=3))


if __name__ == '__main__':
    main()
