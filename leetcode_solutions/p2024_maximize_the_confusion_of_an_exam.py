class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        Ts = answerKey.count("T")
        if min(Ts, n - Ts) <= k:
            return n

        ans, Fs, Ts = 0, 0, 0

        for i, char in enumerate(answerKey):
            if char == "T":
                Ts += 1
            else:
                Fs += 1

            if min(Ts, Fs) <= k:
                ans += 1
            elif answerKey[i - ans] == "T":
                Ts -= 1
            else:
                Fs -= 1

        return ans


class Solution2:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        countT = answerKey.count("T")
        if countT <= k or len(answerKey) - countT <= k:
            return len(answerKey)

        stT, stF = 0, 0
        Finwin, Tinwin = 0, 0
        ans = 0

        for end, ch in enumerate(answerKey, 1):

            if ch == "T":
                Tinwin += 1
            else:
                Finwin += 1

            while Tinwin > k:
                if answerKey[stF] == "T":
                    Tinwin -= 1
                stF += 1

            while Finwin > k:
                if answerKey[stT] == "F":
                    Finwin -= 1
                stT += 1

            ans = max([ans, end - stF, end - stT])

        return ans


def main():
    sol = Solution()
    print("4 ===", sol.maxConsecutiveAnswers("TTFF", 2))
    print("3 ===", sol.maxConsecutiveAnswers("TFFT", 1))
    print("5 ===", sol.maxConsecutiveAnswers("TTFTTFTT", 1))


if __name__ == "__main__":
    main()
