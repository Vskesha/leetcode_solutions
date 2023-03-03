class ExamRoom:

    def __init__(self, n: int):
        self.state = [0] * n
        self.n = n

    def seat(self) -> int:
        p = self.find_pos() if any(self.state) else 0
        self.state[p] = 1
        return p

    def leave(self, p: int) -> None:
        self.state[p] = 0

    def find_pos(self) -> int:

        # 2222222222222222222222222222222222222222222222222222222222222222222222222
        # pos = 0
        # i = self.state.index(1)
        # max_distance = i
        # while True:
        #     left = i
        #     try:
        #         d = self.state[i+1:].index(1) + 1
        #         i += d
        #         if max_distance < d // 2:
        #             max_distance = d // 2
        #             pos = left + max_distance
        #     except ValueError:
        #         d = self.n - left - 1
        #         if max_distance < d:
        #             pos = self.n - 1
        #         break
        # return pos
        # 1111111111111111111111111111111111111111111111111111111111111111111111111111
        # for i in range(self.n):
        #     if self.state[i]:
        #         if left == -1:  # There is noone on left. Take zero position
        #             max_distance = i
        #         elif max_distance < (i - left) // 2:  # place beetween left and right.
        #             max_distance = (i - left) // 2
        #             pos = left + max_distance
        #         left = i
        #     elif i == self.n - 1 and max_distance < self.n - left - 1:
        #         pos = self.n - 1  # Place in the end
        # return pos


if __name__ == '__main__':
    result = [None]
    # commands = ["ExamRoom","seat","seat","seat","leave","leave","seat","seat","seat","seat","seat","seat","seat"]
    # params = [[8], [], [], [], [0], [7], [], [], [], [], [], [], []]
    commands = ["ExamRoom","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","leave","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat","seat"]
    params = [[1000000],[],[],[],[],[],[],[],[],[],[],[],[624999],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    obj = ExamRoom(*params[0])
    for i in range(1, len(commands)):
        print(f'\rProcessing...  {i / (len(commands) - 1):.2%} completed', end='')
        eval(f'result.append(obj.{commands[i]}(*params[i]))')
    print(result)
