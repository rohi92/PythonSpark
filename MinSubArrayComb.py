
from itertools import  combinations
def minSubarray(nums, p):
    """
    :type nums: List[int]
    :type p: int
    :rtype: int
    """
    suml = sum(nums)
    ctr = 0
    if suml % p == 0:
        return 0
    else:
        rem = suml % p
        if rem in nums:
            return 1
        else:
            nums1 = list(map(lambda x: x < rem, nums))
            k = 0
            i = 2
            while (k != 1):
                if i < len(nums1):
                    l1 = list(combinations(nums, i))
                    i = i + 1
                else:
                    k = 1
                l2 = list(filter(lambda x: sum(x) == rem, l1))
                if len(l2) > 0:
                    k = 1
        if len(l2) == 0:
            return -1
        else:
            return len(l2[0])

if __name__=="__main__":
    nums=[17,3,16,12,3,19,1,8,5,8]
    p=54
    print(minSubarray(nums, p))
