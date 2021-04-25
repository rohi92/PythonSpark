
from typing import List

def brute_force(nums: List[int]) -> int:
 i = j = 0
 while (j <= len(nums) and i <= len(nums)):
     yield nums[i:j + 1]
     j += 1
     if j == len(nums):
         i += 1
         j = i
def longest_val_cont_series(l):
 l1 = l[1:]
 ctr=0
 l1.append(l[-1]-1)
 for i, j in zip(l, l1):
     if j - i == 1:
         ctr=ctr+1
 if ctr+1==len(l):
     return True
 else:
     return False

def longest_seq(a):
 ctr=0
 a.sort()
 m=list(brute_force(a))
 m=list(filter(lambda x: len(x)>1,m))
 m1=list(map(lambda x: [x,longest_val_cont_series(x)],m))
 m2 = list(filter(lambda x: x[1] == True, m1))
 m3 = list(map(lambda x: [x[0], len(x[0])], m2))
 m4 = sorted(m3, key=lambda x: x[1], reverse=True)
 return m4[0][1]



if __name__=="__main__":
 a=[1,9,3,10,4,20,2]
 print(longest_seq(a))
