package hello;
import java.util.*;

public class balanced_paranthesis {

	static boolean isbalanced(String exp)
	{
		Deque<Character> stack = new ArrayDeque<Character>(); //ArrayDeque is faster than stack
		for(int i=0;i<exp.length();i++)
		{
			char x = exp.charAt(i);
			if(x == '(' || x == '[' || x == '{')
			{
				stack.push(x);
				continue;
			}
			if(stack.isEmpty())
				return false;
			
			char check;
			switch(x)
			{
			case ')':
				check = stack.pop();
				if(check == '{' || check == '[')
					return false;
				break;
				
			case '}':
				check = stack.pop();
				if(check == '(' || check == '[')
					return false;
				break;
			
			case ']':
				check = stack.pop();
				if(check == '(' || check == '{')
					return false;
				break;
				
			}
		}
		return stack.isEmpty();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the String: ");
		String s = sc.nextLine();
		if(isbalanced(s))
		{
			System.out.println("balanced !");
		}
		else
		{
			System.out.println("not-balanced");
		}
	}

}
