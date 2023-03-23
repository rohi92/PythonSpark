# 123456-> 12,34,56
# 1234567->12,34,567
# 1234567.3456->12,34,567.3456
def insert_comma(input):
    output=""
    decimal_flag=""
    if "." not in str(input):
        input1=str(input)
        decimal_flag=False
    else:
        pos=str(input).rfind(".")
        input1=str(input)[0:pos]
        decimal_flag=True
    l1=[]
    for i,j in zip(input1,range(len(input1))):
        if j%2!=0 and j!=0:
            l1.append(j)
    for i, j in zip(l1,range(len(l1))):
        if j==0:
            output=output+input1[0:i+1]+","
        elif j!=len(l1)-1:
            output=output+input1[i-1:i+1]+","
        else:
            output=output+input1[i-1:]
    if decimal_flag:
        output=output+str(input)[pos:]
        return output
    else:
        return output















if __name__=="__main__":
    input=1234567.123456
    a=insert_comma(input)
    print(a)

