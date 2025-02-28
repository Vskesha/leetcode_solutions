from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for fr, to in sorted(tickets, reverse=True):
            graph[fr].append(to)

        itinerary = []

        def dfs(ap):
            while graph[ap]:
                dfs(graph[ap].pop())
            itinerary.append(ap)

        dfs('JFK')
        return itinerary[::-1]


class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        lt = len(tickets)
        itinerary = ['JFK']

        graph = defaultdict(list)
        for fr, to in tickets:
            graph[fr].append(to)
        for fr in graph:
            graph[fr].sort()

        def groups() -> int:
            roots = {}
            for fr in graph:
                if graph[fr]:
                    roots[fr] = fr
                for to in graph[fr]:
                    roots[to] = to

            ans = len(roots) or 1

            def find(node):
                if roots[node] == node:
                    return node
                roots[node] = find(roots[node])
                return roots[node]

            for fr in graph:
                for to in graph[fr]:
                    root1 = find(fr)
                    root2 = find(to)
                    if root1 != root2:
                        roots[root1] = root2
                        ans -= 1

            return ans

        def dfs(dep: str) -> None:
            if len(itinerary) == lt + 1:
                raise StopIteration('end')
            for i in range(len(graph[dep])):
                ar = graph[dep].pop(i)
                if groups() == 1:
                    itinerary.append(ar)
                    dfs(ar)
                    itinerary.pop()
                graph[dep].insert(i, ar)

        try:
            dfs('JFK')
        except StopIteration:
            pass
        return itinerary


def test():
    sol = Solution()
    print('Test 1 ... ', end='')
    assert sol.findItinerary(tickets=[["MUC", "LHR"],
                                      ["JFK", "MUC"],
                                      ["SFO", "SJC"],
                                      ["LHR", "SFO"]])\
           == ["JFK", "MUC", "LHR", "SFO", "SJC"]
    print('ok')
    print('Test 2 ... ', end='')
    assert sol.findItinerary(tickets=[["JFK", "SFO"],
                                      ["JFK", "ATL"],
                                      ["SFO", "ATL"],
                                      ["ATL", "JFK"],
                                      ["ATL", "SFO"]])\
           == ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    print('ok')
    print('Test 3 ... ', end='')
    assert sol.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "JFK"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"],
                              ["ATL", "AAA"], ["AAA", "BBB"], ["BBB", "ATL"]]) \
           == ['JFK', 'SFO', 'JFK', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB', 'ATL', 'AAA', 'BBB',
               'ATL']
    print('ok')


if __name__ == '__main__':
    test()
