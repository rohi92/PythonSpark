def isAnagram(self, s, t):
    s1 = set(s)
    s2 = set(t)
    c1 = list(map(lambda x: [x, s.count(x)], s1))
    c1 = sorted(c1, key=lambda x: x[0])
    c2 = list(map(lambda x: [x, t.count(x)], s2))
    c2 = sorted(c2, key=lambda x: x[0])
    eff_listc1=[]
    eff_listc2=[]
    for i in c1:
        if i not in eff_listc1:
            eff_listc1.append(i)
            for i in c2:
                if i not in eff_listc2:
                    eff_listc2.append(i)
                    if eff_listc1 == eff_listc2 :
                        return True
                    else:
                        return False

if __name__=="__main__":
    print(isAnagram("self","aa","a"))