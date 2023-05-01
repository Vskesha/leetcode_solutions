def candy(ratings: list[int]) -> int:
    lr = len(ratings)
    candies = [1] * lr
    for i in range(1, lr):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(lr-1, 0, -1):
        if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
            candies[i-1] = candies[i] + 1
    print(candies)
    return sum(candies)
    
    
if __name__ == '__main__':
    print('5 ===', candy([1, 0, 2]))
    print('4 ===', candy([1, 2, 2]))
    print('11 ===', candy([1,3,4,5,2]))