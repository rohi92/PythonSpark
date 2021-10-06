def least_denom(a):
    if a>=10 and a<50 and a%10==0:
        return int(a/10)
    elif a>=50 and a<100 and a%50==0:
        return int(a/50)
    elif a >=100 and a % 100 == 0:
        return int(a/100)
    elif a ==2 or a==1 or a==5:
        return 1
    elif a>2 and a<5:
        return denom_two_five(a)
    elif a>5 and a<10:
        return denom_five_ten(a)
    elif a>10 and a<50:
        return denom_ten_fifty(a)
    elif a>50 and a<100:
        return denom_fifty_hundered(a)
    elif a>100:
        l1=int(a/100)
        l2=a%100
        if l2 == 1 or l2 == 2 or l2 == 5 or l2 == 10 or l2==50:
            return l1 + 1
        elif l2>50 and l2<100:
            return l1+denom_fifty_hundered(l2)
        elif l2 > 10 and l2 < 50:
            return l1 + denom_ten_fifty(l2)
        elif l2 > 5 and l2 < 10:
            return l1+denom_five_ten(l2)
        elif l2 > 2 and l2 < 5:
            return l1+denom_two_five(l2)



def denom_two_five(a):
    if a%5==0 and a>=5:
        return int(a/5)
    elif a%2==0:
        return int(a/2)
    else:
        return int(a/2)+int(a%2)
def denom_five_ten(a):
    l1=a%5
    return int(1+denom_two_five(l1))
def denom_ten_fifty(a):
    l1=int(a/10)
    l2=a%10
    if l2>5:
        return l1+denom_five_ten(l2)
    else:
        return l1+denom_two_five(l2)
def denom_fifty_hundered(a):
    l1=int(a/50)
    l2=a%50
    if l2==1 or l2==2 or l2==5 or l2==10:
        return l1+1
    elif l2<5 and l2>2:
        return denom_two_five(l2)+l1
    elif l2 < 10 and l2 > 5:
        return denom_five_ten(l2) + l1
    elif l2 < 50 and l2 > 10:
        return denom_ten_fifty(l2) + l1












if __name__=="__main__":
    print(least_denom(21542))
    #for i in range(1,50,1):
        #print(least_denom(i),i)
