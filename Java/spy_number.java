import java.util.Scanner;  
public class SpyNumberExample2  
{  
//method to check the Spy number  
private static boolean isSpyNumber(int number)   
{  
int lastDigit = 0;  
int sum = 0;  
int product = 1;  
//executes until the condition returns true  
while(number != 0)   
{  
//determines the last digit of the given number  
lastDigit = number % 10;  
//adds the last digit to the variable sum  
sum = sum + lastDigit;  
//multiply last digit with product  
product = product * lastDigit;  
//removes the last digit of the given number  
number = number / 10;  
}  
//compares the variable sum with product and returns the result accordingly  
if(sum == product)  
return true;  
return false;  
}  
//driver code  
public static void main(String args[])   
{  
int lowerRange = 0, upperRange = 0;  
Scanner sc = new Scanner(System.in);  
System.out.print("Enter the lower range: ");  
//reads lower range  
lowerRange = sc.nextInt();  
System.out.print("Enter upper range: ");  
//reads the upper range   
upperRange = sc.nextInt();  
System.out.println("The Spy numbers between "+ lowerRange + " to "+ upperRange+" are: ");  
for(int i=lowerRange; i<=upperRange; i++)   
{  
//calling user-defined function that checks if the given number is spy or not  
if(isSpyNumber(i))  
//prints all the spy numbers  
System.out.print(i +" ");  
}  
}  
}  