from itertools import combinations
def smallestDistancePair(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    list1 = (combinations(nums, 2))
    comb_dist = []
    for i in list1:
        comb_dist.append(abs(i[1] - i[0]))
    comb_dist.sort()
    return comb_dist[k - 1]
if __name__=="__main__":
    print(smallestDistancePair("self",[1,3,1],1))

