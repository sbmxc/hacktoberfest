t=int(input())
while t>0:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i in range(n):
        if b[i]==0:
            c.append(a[i])
    c.sort(reverse=True)
    j=0
    for i in range(n):
        if b[i]==0:
            a[i]=c[j]
            j+=1
    print(*a)        