
from itertools import combinations
import itertools

def array_type(nums,t,k):
    l4 = list(itertools.combinations(enumerate(nums), 2))
    eff=[]
    for i in l4:
        for j in i:
            eff.append(j)
    l5=list(filter(lambda x: abs(x[1]-x[0])<=k,eff))
    l6=list(filter(lambda x : nums[x[1]]-nums[x[0]]<=t,l5))
    if len(l6)>0:
        return True
    else:
        return False





if __name__=="__main__":
    nums=[1,2,3,1]
    print(array_type(nums, 0, 3))
