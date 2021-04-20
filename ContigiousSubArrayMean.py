
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from itertools import combinations
from typing import List


def brute_force(nums: List[int]) -> int:
 i = j = 0
 while j <= len(nums) and i <= len(nums):
     yield nums[i:j + 1]
     j += 1
     if j == len(nums):
        i += 1
        j = i


def solution(A, S):
 l1 = len(A)
 l3 = []
 for i in range(2, l1, 1):
     l2 = list(combinations(A, i))
     l3.append(list(filter(lambda x: sum(x) / len(x) == S, l2)))
 out = [item for t in l3 for item in t]
 out = list(map(lambda x: list(x), out))
 out1 = list(brute_force(A))
 final_list = list(filter(lambda x: x in out1, out))

 if S in A:
     final_list.append(S)
 if sum(A) / len(A) == S:
     final_list.append(A)
 return len(final_list)

if __name__=="__main__":
 print(solution([0,4,3,-1],2))


