
pos=-1
def sortarr(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
list=[]
m=int(input())
for j in range(0,m):
    ele = int(input())
    list.append(ele)
print(list)
sortarr(list)
print(list)