"""pos=-1
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return False


list=[5,8,4,6,9,2]
n=9
if search(list,n):
    print("Found at",pos)
else:
    print("Not Found")"""

pos=-1
def search(list,n):
    for i in range(0,len(list)):
        if list[i]==n:
            globals()['pos']=i
            i = i + 1
            return True


    return False
list=[]
n=int(input())
m=int(input())
for j in range(0,m):
    ele = int(input())
    list.append(ele)
    list=sorted(list)
print(list)
if search(list,n):
    pr
    int("Found at",pos)
else:
    print("Not Found")
