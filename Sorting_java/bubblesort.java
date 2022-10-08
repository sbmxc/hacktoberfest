import java.util.*;
class bubblesort
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the size of array");
        int n=sc.nextInt();
        int a[]=new int[n];
        for(int i=0;i<n;i++)
        {  System.out.println("Enter the element "+i);
            a[i]=sc.nextInt();
        }
        
        for(int i=0;i<n-1;i++)
        {
            for(int j=0;j<n-1;j++)//or for(int j=0;j<n-i-1;i++)
            {
                if(a[j]>a[j+1])
                {
                  int temp=a[j];
                    a[j]=a[j+1];
                    a[j+1]=temp;
                }
            }
        }
        for(int i=0;i<n;i++)
        {System.out.print(a[i]+" ");}
    }
}