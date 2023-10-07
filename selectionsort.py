
pos=-1
def sortarr(list,):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j
        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp


    return False
list=[]
m=int(input())
for j in range(0,m):
    ele = int(input())
    list.append(ele)
print(list)
sortarr(list)
print(list)