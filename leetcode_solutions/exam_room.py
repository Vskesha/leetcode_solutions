class ExamRoom:

    def __init__(self, n: int):
        self.st = [0] * n
        self.n = n

    def seat(self) -> int:
        max_dis = 0
        pos = 0
        l = -3 * self.n
        r = self.st.index(1) + l + 1 if sum(self.st) else 2 * self.n
        for i in range(self.n):
            print(f'i = {i}')
            if self.st[i] == 1:
                l = i
                r = self.st[l + 1:].index(1) + l + 1 if sum(self.st[l + 1:]) else 2 * self.n
                print(f'left = {l}, right = {r}')
                continue
            dis = min(i - l, r - i)
            if max_dis < dis:
                max_dis = dis
                pos = i
                print(f'pos = {pos}, max_dis = {max_dis}')
        self.st[pos] = 1
        print(self.st)
        return pos

    def leave(self, p: int) -> None:
        self.st[p] = 0
        print(self.st)

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)


if __name__ == '__main__':
    result = [None]
    commands = ["ExamRoom","seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat"]
    params = [[8], [], [], [], [0], [7], [], [], [], [], [], [], []]
    obj = ExamRoom(*params[0])
    for i in range(1, len(commands)):
        eval(f'result.append(obj.{commands[i]}(*params[i]))')
    print(result)
