import re


def most_frequent(paragraph: str, banned: list[str]):
    banned = set(banned)
    counter = {}
    for word in re.split(r'\W+', paragraph.lower()):
        if word not in banned:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return max(counter, key = counter.get)


if __name__ == '__main__':
    print(most_frequent(paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
    