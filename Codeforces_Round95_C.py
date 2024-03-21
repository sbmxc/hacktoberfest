for _ in range(int(input())):
    n=int(input())
    A=[int(_) for _ in input().split()]
    ans=0
    c=0
    if A[0]==1:
        ans+=1
    for _ in range(1,n):
        if A[_]==1:
            c+=1
        else:
            ans+=c//3
            c=0
    print(ans+c//3)