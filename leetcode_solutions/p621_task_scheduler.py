import heapq
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        l = Counter(tasks)
        return max(
            (n + 1) * (max(l.values()) - 1)
            + len([x for x in l.values() if x == max(l.values())]),
            len(tasks),
        )


class Solution2:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Build frequency map
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord("A")] += 1

        # Max heap to store frequencies
        pq = [-f for f in freq if f > 0]
        heapq.heapify(pq)

        time = 0
        # Process tasks until the heap is empty
        while pq:
            cycle = n + 1
            store = []
            task_count = 0
            # Execute tasks in each cycle
            while cycle > 0 and pq:
                current_freq = -heapq.heappop(pq)
                if current_freq > 1:
                    store.append(-(current_freq - 1))
                task_count += 1
                cycle -= 1
            # Restore updated frequencies to the heap
            for x in store:
                heapq.heappush(pq, x)
            # Add time for the completed cycle
            time += task_count if not pq else n + 1
        return time


def test_least_interval():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=2) == 8
    print("OK")

    print("Test 2... ", end="")
    assert sol.leastInterval(tasks=["A", "C", "A", "B", "D", "B"], n=1) == 6
    print("OK")

    print("Test 3... ", end="")
    assert sol.leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=3) == 10
    print("OK")


if __name__ == "__main__":
    test_least_interval()
