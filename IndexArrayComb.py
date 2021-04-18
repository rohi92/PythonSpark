def solution(A, B):
   # write your code in Python 3.6
   a1=[]
   a2=[]
   b1=[]
   b2=[]
   l1=len(A)
   for i in range(1,l1,1):
       a1.append(A[0:i])
       a2.append(A[i:])
       b1.append(B[0:i])
       b2.append(B[i:])
   a1_sum=list(map(lambda x: sum(x),a1))
   a2_sum=list(map(lambda x: sum(x),a2))
   b1_sum=list(map(lambda x: sum(x),b1))
   b2_sum=list(map(lambda x: sum(x),b2))
   index_pos=0
   a=0
   for i,j,k,l in zip(a1_sum,a2_sum,b1_sum,b2_sum):
       if(i==j and j==k and k==l):
           a=a+1

   return a
if __name__=="__main__":
   print(solution ([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]))
