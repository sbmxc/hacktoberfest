import java.util.*;
public class CheckForTriangle {
    static void Istriangle(float x,float y,float z){
            System.out.println("Angle A1 : "+x);
            System.out.println("Angle A2 : "+y);
            System.out.println("Angle A3 : "+z);
            System.out.println("Sum of angle is "+ (x+y+z));
            if(x+y+z == 180)System.out.println("TRIANGLE");
            else System.out.println("Not a Triangle");

    }
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter angle A1 : ");
        float A1=sc.nextFloat();
        //System.out.println();
        System.out.print("Enter angle A2 : ");
        float A2=sc.nextFloat();
        //System.out.println();
        System.out.print("Enter angle A3 : ");
        float A3=sc.nextFloat();
        //System.out.println();
        Istriangle(A1,A2,A3);
    }   
}
