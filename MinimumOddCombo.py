
from itertools import combinations

def min_odd(num):
 comb=[]
 for i in range(1,len(num),1):
     for i in list(combinations(num,i)):
        comb.append(i)
 return comb

def count_odd(num):
 return len(list(filter(lambda x:x%2==1,num)))

if __name__=="__main__":
 num=[1,2,3,4]
 k=2
 a=min_odd(num)
 #count the odd in all the combs
 odd_cnt=list(map(lambda x:[x,count_odd(x)],a))
 odd_cnt=list(filter(lambda x:x[1]<=k,odd_cnt))
 print(len(odd_cnt))
