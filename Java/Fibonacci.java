import java.util.HashMap;
public class Fibonacci {
    static HashMap<Integer,Long> map=new HashMap<>();
    public static long fib(int n){
        if(n==1||n==2){
            return 1;
        }
        
        if(map.containsKey(n)){
            return map.get(n);
        }
        map.put(n,fib(n-1)+fib(n-2));
        return map.get(n);
    }
    public static void main(String[] args) {
        System.out.println(fib(50));
    }
}
//updated fib using hashmap basic dp