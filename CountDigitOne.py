def countDigitOne(self, n):
    
    """
    :type n: int
    :rtype: int
    """
    count = 0
    if n >= 3000000:
        l1 = list(range(1, (n + 1 / 2), 1))
        l2 = list(map(lambda x: str(x), l1))
        l2 = list(filter(lambda x: '1' in x, l2))
        l3 = list(map(lambda x: x.count('1'), l2))
        count = count + sum(l3)
        l1 = list(range((n + 1 / 2), n, 1))
        l2 = list(map(lambda x: str(x), l1))
        l2 = list(filter(lambda x: '1' in x, l2))
        l3 = list(map(lambda x: x.count('1'), l2))
        count = count + sum(l3)
    else:
        l1 = list(range(1, n + 1, 1))
        l2 = list(map(lambda x: str(x), l1))
        l2 = list(filter(lambda x: '1' in x, l2))
        l3 = list(map(lambda x: x.count('1'), l2))
    count = sum(l3)

    return count

if __name__=="__main__":
    print(countDigitOne("self",13))
