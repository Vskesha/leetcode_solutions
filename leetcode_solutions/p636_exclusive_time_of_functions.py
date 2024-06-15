from collections import deque
from typing import List


class Call:
    def __init__(self, pid=-1, times=None, prev=None):
        self.pid = pid
        self.times = times or []
        self.prev = prev


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        curr = Call()
        ans = [0] * n

        def get_total_time(times):
            return sum(times[i + 1] - times[i] for i in range(0, len(times), 2))

        for log in logs:
            pid, action, time = log.split(":")
            pid, time = int(pid), int(time)

            if action == "start":
                curr.times.append(time)
                curr = Call(pid, [time], curr)

            else:
                curr.times.append(time + 1)
                ans[curr.pid] += get_total_time(curr.times)
                curr = curr.prev
                curr.times.append(time + 1)

        return ans


class Solution2:  # revision, May 2024
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        ans, stack, prev_time = (
            [0] * n,
            deque(),
            0,
        )  # Example: ["0:start:0", "0:start:2", "0:end:5",
        #           "1:start:6", "1:end  :6", "0:end:7"]

        for log in logs:  #                time-
            id, action, timestamp = log.split(
                ":"
            )  #   id   action  stamp    ans    stack
            id, timestamp = int(id), int(
                timestamp
            )  #  ––––   ––––    ––––   –––––   –––––––––
            #    0    start     0    [0,0]   [0]
            if action == "start":  #    0    start     2    [2,0]   [0,0]
                if stack:  #    0     end      5    [6,0]   [0]
                    ans[stack[-1]] += (
                        timestamp - prev_time
                    )  #    1    start     6    [6,0]   [(0,1]
                stack.append(id)  #    1     end      6    [6,1]   [0]
                prev_time = timestamp  #    0     end      7    [7,1]   []
            else:
                ans[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1
            # print(id,action,timestamp, ans, stack)

        return ans


def test_exclusive_time():
    sol = Solution()

    print("Test 1... ", end="")
    assert sol.exclusiveTime(
        n=2, logs=["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    ) == [3, 4]
    print("OK")

    print("Test 2... ", end="")
    assert sol.exclusiveTime(
        n=1,
        logs=["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"],
    ) == [8]
    print("OK")

    print("Test 3... ", end="")
    assert sol.exclusiveTime(
        n=2,
        logs=["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"],
    ) == [7, 1]
    print("OK")

    print("Test 4... ", end="")
    assert sol.exclusiveTime(
        n=3,
        logs=[
            "1:start:0",
            "0:start:2",
            "1:start:3",
            "2:start:4",
            "2:end:4",
            "0:end:6",
            "1:end:7",
            "1:end:8",
        ],
    ) == [2, 6, 1]
    print("OK")


if __name__ == "__main__":
    test_exclusive_time()