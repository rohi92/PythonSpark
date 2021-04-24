
from typing import List
from functools import reduce
from operator import mul

def brute_force(nums: List[int]) -> int:
    i = j = 0
    while (j <= len(nums) and i <= len(nums)):
        yield nums[i:j + 1]
        j += 1
        if j == len(nums):
            i += 1
            j = i

def maxProduct(self, nums):
    a=brute_force(nums)
    mula=[]
    for i in list(a):
        l=reduce(mul, i, 1)
        mula.append([i,l])
        l1 = sorted(mula, key=lambda x: x[1], reverse=True)
    l2=list(filter(lambda x:len(x[0])>0,l1))
    return l2[0][1]


if __name__=="__main__":
    a=[2,3,-2,4]
    print(maxProduct("self",a))
