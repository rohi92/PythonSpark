def group_anagram(lis):
    lis1=lis[:]
    lis2=[]
    d={}
    for i in lis:
        lis3 = []
        for j in lis1:
            if (set(i)==set(j) and i!=j):
                lis3.append(j)
                lis.remove(j)
                lis1.remove(j)
        lis.remove(i)
        lis3.append(i)
        lis2.append([lis3])
        if len(lis3) > 0:
            d[i] = lis3
        else:
            d[i] = ' '
        for i in lis1:
            lis3 = []
            if (set(i) == set(lis[-1]) and i != lis[-1]):
                lis3.append(i)
            lis3.append(lis[-1])
        lis2.append(lis3)










    return lis2

if __name__=="__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagram(strs))