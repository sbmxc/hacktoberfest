import java.util.regex.Pattern;  
import java.util.Scanner;  
import java.util.regex.Matcher;    
public class RegexExample{    
    public static void main(String[] args){    
        Scanner sc=new Scanner(System.in);  
        while (true) {    
            System.out.println("Enter regex pattern:");  
            Pattern pattern = Pattern.compile(sc.nextLine());    
            System.out.println("Enter text:");  
            Matcher matcher = pattern.matcher(sc.nextLine());    
            boolean found = false;    
            while (matcher.find()) {    
                System.out.println("I found the text "+matcher.group()+" starting at index "+    
                 matcher.start()+" and ending at index "+matcher.end());    
                found = true;    
            }    
            if(!found){    
                System.out.println("No match found.");    
            }    
        }    
    }    
}  