/*
Given an integer X, find its square root. If X is not a perfect square, 
then return floor(√x).

Time Complexity: O(√X)
Auxiliary Space: O(1)*/
class Squareroot {
 
    static int floorSqrt(int x)
    {
        
        if (x == 0 || x == 1)
            return x;
 
        int i = 1, result = 1;
 
        while (result <= x) {
            i++;
            result = i * i;
        }
        return i - 1;
    }
 
    
    public static void main(String[] args)
    {
        int x = 11;
        System.out.print(floorSqrt(x));
    }
}