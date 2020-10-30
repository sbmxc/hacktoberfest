'''You will be given two arrays of integers and asked to determine all integers that satisfy the following two conditions:

The elements of the first array are all factors of the integer being considered
The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. You must determine how many such numbers exist'''

def getTotalX(a, b):
    new=[]
    new2=[]
    for i in range(a[0],b[0]+1):
        c=0
        for j in b:
            if j%i!=0:
                break
            else:
                c+=1
        if c==len(b):
            new.append(i)
    for i in new:
        for j in a:
            if i%j!=0:
                new2.append(i)
                break
    for i in new2:
        new.remove(i)
         
    return len(new)
        
        
a=[]
b=[]
a1=int(input("enter the umber of elements in the array a"))
b1=int(input("enter the number of elements in the array b"))
for i in range(0,a1):
    c=int(input("enter no."))
    a.append(c)
for i in range(0,b1):
    d=int(input("enter b no."))
    b.append(d)
print (getTotalX(a,b))

