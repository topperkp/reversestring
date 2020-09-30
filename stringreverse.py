s = input()

def reverse(st):
    s1=''
    i=len(st)
    while i>=1:
        s1= s1+st[i-1]
        i-=1
    return s1    

ans = reverse(s)
print(ans)
        
        
print("Method 2")

def reverse2(st):
    s=''
    for i in st:
        s = s+ i
    return st

ans2= reverse2(s)
print(ans2)
