"""**Example1:**
```
Input: nums = [1,7,3,6,5,6]
Output: 3

Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
```
**Example2:**
```
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
```
**Example3:**
```
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
```"""

def get_pivot_index(nums):
    # *** write code here ***
    sum_index=[]
    l1=len(nums)
    l=range(1,len(nums)-1)
    for i in l:
      if i!=0 and i!=l1-1 and i!=1:
        sum_index.append([i,sum(nums[:i]),sum(nums[i+1:])])
      elif(i==1):
        sum_index.append([1,nums[0],sum(nums[2:])])
    if (sum(nums[1:]) == 0):
        sum_index.append([0, 0, 0])
    sum_index=list(filter(lambda x:x[1]==x[2],sum_index))
    return sum_index

if __name__=="__main__":
    print(get_pivot_index([1,7,3,6,5,6]))
