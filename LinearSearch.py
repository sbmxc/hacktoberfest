list = []
a = int(input('Enter the length of your list = '))
for n in range(a):
    numbers = int(input('enter any no. = '))
    list.append(numbers)
b = int(input('enter any no. to search = '))
for i in range(len(list)):
    if list[i] == b :
        print('number found at position',i)
        break
else:
     print('number not found in the list')
input('press enter to exit')        

