
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import List


def brute_force(nums: List[int]) -> int:
 i = j = 0
 while (j <= len(nums) and i <= len(nums)):
     yield nums[i:j + 1]
     j += 1
     if j == len(nums):
         i += 1
         j = i


def solution(A):
 # write your code in Python 3.6
 out = list(brute_force(A))
 set1 = set(A)
 l1 = list(filter(lambda x: set(x) == set(A), out))
 l2 = list(map(lambda x: [x, len(x)], l1))
 l2 = sorted(l2, key=lambda x: x[1])
 return l2[0][1]
if __name__=="__main__":
 print(solution([7,5,2,7,2,7,4,7]))
