import java.util.*;
class insertionsort
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
        for(int i=1;i<n;i++)
        {
            int current=a[i];
            int j=i-1;
            while(j>=0&&current<a[j])
            {
               a[j+1]=a[j];
               j--; 
            }
            //placement
            a[j+1]=current;
        }
        for(int i=0;i<n;i++)
        {
            System.out.print(a[i]+" ");
        }
    }
}