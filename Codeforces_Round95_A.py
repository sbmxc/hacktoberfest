t=int(input())
while t>0:
    t-=1
    x,y,k=map(int,input().split())
    s=k*y+k
    b=(s-1)
    if b%(x-1)==0:
        
        print(b//(x-1)+k)
    else:
        print(b//(x-1)+k+1)
        