
def repeatedStringMatch(self, a, b):
    s1=set(a)
    s2=set(b)
    l1=list(map(lambda x:[x,a.count(x)],s1))
    l2 = list(map(lambda x:[x,b.count(x)], s2))
    if s1==s2:
        return l2[0][1]+1
    else:
        return -1



if __name__=="__main__":
    print(repeatedStringMatch("self","abc","wxyz"))
