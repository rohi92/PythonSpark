def PhoneNumber(N):
    m = N.replace("?", "")
    m1 = N.count("?")
    n = list(m)
    n1 = list(map(lambda x: int(x), n))
    n2 = sum(n1) % 3
    n3 = abs(sum(n1) % 3 - 3)
    n4 = N.rfind("?")
    if n2 == 0:
        result = N.replace("?", "0")
    elif n3 == 1:
        N = N[:n4] + "1" + N[n4 + 1:]
        result = N.replace("?", "0")
    elif n3 == 2:
        N = N[:n4] + "2" + N[n4 + 1:]
        result = N.replace("?", "0")
    return result


# INPUT [uncomment & modify if required]
N ='5?9?3?????'

# OUTPUT [uncomment & modify if required]
print(PhoneNumber(N))