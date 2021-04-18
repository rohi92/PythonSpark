def quote_append(input_str):
   l1=list(input_str)
   l2 = list(range(0, len(l1), 1))
   l3=[]
   for i,j in zip(l1,l2):
       l3.append([i,j])
   l4 = list(filter(lambda x: x[0] == "'", l3))
   l5=[]
   for i in range(0,len(l4),2):
       l5.append([l4[i][1],l4[i+1][1]])
   l5=list(map(lambda x:[x[0],x[1]+1],l5))
   l6=l5[:]
   r=list(range(0,len(l6)-1,1))
   for i,j in zip(l6,r):
       if i[1]+1!=l6[j+1][0]:
           l6.append([i[1]+1,l6[j+1][0]-1])

   l7=sorted(l6,key=lambda x:x[0])
   l8 = list(map(lambda x: input_str[x[0]:x[1]] if "'" in input_str[x[0]:x[1]] else str(input_str[x[0]:x[1]]).split(","),l7))
   l9=[]
   for i in l8:
       if type(i) is list:
           for j in i:
               l9.append(j)
       else:
           l9.append(i)
   append_list=[]
   end_pos=l5[-1][1]
   start_pos=l5[0][0]
   right=[]
   left=[]
   if end_pos<len(input_str)-1:
       right=str(input_str[end_pos+1:]).split(",")
   if start_pos>0:
       left = str(input_str[:start_pos-1]).split(",")
   if len(left)>0:
       l9=left+l9
   if len(right)>0:
       l9=l9+right
   l9=list(map(lambda x:str(x).replace("'",""),l9))
   l9.insert(0,"START")
   l9.append("END")
   return l9



def append(input_str):
   if "'" in input_str:
       m=quote_append(input_str)
   else:
       m=input_str.split(",")
       m.insert(0,"START")
       m.append("END")
   return m





if __name__=="__main__":
   input_str=",'discount',normal,'covid,area',toronto"
   print(append(input_str))
