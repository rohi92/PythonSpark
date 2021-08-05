from itertools import combinations
def threeSumClosest(nums, target):
    a = list(combinations(nums, 3))
    d = list(map(lambda x: [x, sum(x)], a))
    d = sorted(d, key=lambda d: d[1])
    d1 = list(map(lambda x: [x, abs(x[1] - target)], d))
    d1 = sorted(d1, key=lambda d: d[1], reverse=True)
    return d1[-1][0][1]


if __name__=='__main__':
    nums = [-1, 2, 1, -4]
    target = 1
    t=threeSumClosest(nums, target)
    print(t)