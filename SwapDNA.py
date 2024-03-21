# A Program to swap DNA => RNA 

# Write your code here
string = input()
flag = True
out = ''
for s in string:
    if s == 'A':
        out += 'U'
    elif s == 'G':
        out += 'C'
    elif s == 'C':
        out += 'G'
    elif s == 'T':
        out += 'A'
    else:
        flag = False

if flag:
    print(out)
else:
    print("Invalid Input")
