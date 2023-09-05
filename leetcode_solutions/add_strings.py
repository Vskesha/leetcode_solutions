class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        ml = max(l1, l2)
        num1 = '0' * (ml - l1) + num1
        num2 = '0' * (ml - l2) + num2
        ad = 0
        res = []
        
        for i in range(1, ml + 1):
            a = num1[-i]
            b = num2[-i]
            
            summ = ord(a) + ord(b) - 2 * ord('0') + ad
            ad = summ // 10
            summ %= 10
            res.append(chr(summ + ord('0')))
            
        if ad:
            res.append(chr(ad + ord('0')))
            
        return ''.join(res[::-1])
            
            
if __name__ == '__main__':
    sol = Solution()
    print('134 ===', sol.addStrings(num1 = "11", num2 = "123"))
    print('533 ===', sol.addStrings(num1 = "456", num2 = "77"))
    print('0 ===', sol.addStrings(num1 = "0", num2 = "0"))
    