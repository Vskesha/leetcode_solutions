from bisect import bisect


def longest_obstacle_course(obstacles: list[int]):
    ans, dis = [], []
    for obstacle in obstacles:
        if not dis or obstacle >= dis[-1]:
            dis.append(obstacle)
            ans.append(len(dis))
        else:
            idx = bisect(dis, obstacle)
            dis[idx] = obstacle
            ans.append(idx + 1)
    return ans


def longest_obstacle_course2(obstacles: list[int]):
    l = len(obstacles)
    ans = [1] * l
    sorted_passed = [obstacles[0]]
    for i in range(1, l):
        pos = bisect(sorted_passed, obstacles[i])
        sorted_passed.insert(pos, obstacles[i])
        ans[i] = pos + 1
    return ans


if __name__ == '__main__':
    print('[1, 2, 3, 3] ===', longest_obstacle_course([1, 2, 3, 2]))
    print('[1, 2, 1] ===', longest_obstacle_course([2, 2, 1]))
    print('[1, 1, 2, 3, 2, 2] ===', longest_obstacle_course([3, 1, 5, 6, 4, 2]))
