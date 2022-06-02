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
    sum_index=list(filter(lambda x:x[1]==x[2],sum_index))
    return sum_index

if __name__=="__main__":
    print(get_pivot_index([1,7,3,6,5,6]))