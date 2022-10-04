
def Operation(num1, num2, opt):
    match opt:
        case 1:
            return num1+num2
        case 2:
            return num1-num2
        case 3:
            return num1*num2
        case 4:
            if(num2==0):
                return "divide by 0 not possible"
            else:
                return num1/num2
        
    return 0

if __name__ == "__main__":

    while(True):
        num1 = int(input("Enter 1st number: "))
        num2 = int(input("Enter 2nd number: "))

        print("Choose one option:\n")
        print("1.Add\t2.Subtract\t3.Multiply\t4.Divide")

        opt = int(input())

        ans = Operation(num1, num2, opt)

        print("final answer:", ans)
        input1 = input("Want to continue?(y/n)")
        if(input1 == 'n'):
            exit()

    
