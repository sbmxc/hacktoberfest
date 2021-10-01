number=int(input("Enter number:"))
rev=int(str(n)[::-1])
if(number==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")
