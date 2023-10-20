import java.util.Arrays;
public class Binary_Search {

public static void main(String[] args) {
  int [] array={10,15,20,11,25,30,35};
Reverse_Array(array);
}
//Reverse an array

static void Reverse_Array(int[] array) {
int start=0,end=array.length-1;
for (int i = start; i <end; i++) {
int temp=array[i];
array[i]=array[end];
array[end]=temp;
end--;
}
System.out.println(Arrays.toString(array));
return;
}
}
