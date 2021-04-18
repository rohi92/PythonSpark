
def nearestPalindromic(self,n):
    if n <10:
        return n-1
        i=1
        m=n-1
        j=0
        k=0
        while(j==0):
            if(str(m)==str(m)[::-1]):
                j=1
            else:
                m=m-1
                k=n+1
                j=0
                while(j==0):
                    if(str(k)==str(k)[::-1]):
                        j=1
                    else:
                        k=k+1
                        a1=abs(n-m)
                        a2=abs(k-n)
                        d=min(a1,a2)
                        if d==a1:
                            return m
                        else:
                            return k


if __name__=="__main__":
    print(nearestPalindromic("self",123))
