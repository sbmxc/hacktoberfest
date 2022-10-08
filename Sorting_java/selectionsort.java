import java.util.*;
class selectionsort
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
        for(int i=0;i<n;i++)
        {
            int min=i;
            for(int j=i+1;j<n;j++)
            {
                if(a[j]<a[min])
                {min=j;}}
                int temp=a[i];
                a[i]=a[min];
                a[min]=temp;
            }
            System.out.println("The sorted array is");
            for(int i=0;i<n;i++)
            {System.out.print(a[i]+" ");}
        }
    }
