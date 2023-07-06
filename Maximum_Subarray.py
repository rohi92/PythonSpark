# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.


# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.


def sum_max(arr):
    max_prev=max_sum=0
    dict={}
    for i,j in zip(arr,range(len(arr))):
        if j>=0:
            max_prev=max(i,i+max_prev)
            max_sum=max(max_prev,max_sum)
            key="["+str(i)+","+str(j)+"]"
            dict[key]=max_prev
    return dict[max(dict, key=dict.get)]

if __name__=="__main__":
    arr=[5,4,-1,7,8]
    dict1=sum_max(arr)
    print(dict1)





