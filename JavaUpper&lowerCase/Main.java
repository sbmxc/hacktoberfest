package com.company;

import java.util.Scanner;

class Main {

    public static void main(String[] args) {
        String p;

        Scanner s=new Scanner(System.in);

        System.out.println("Enter string");
        p=s.nextLine();
       char[] c=p.toCharArray();
       for(int i=0;i<c.length;i++)
       {
           char ch=c[i];
           if(Character.isUpperCase(ch))
           {
               c[i]=Character.toLowerCase(ch);
           }
           else if(Character.isLowerCase(ch))
           {
               c[i]=Character.toUpperCase(ch);
           }

       }
       String n=new String(c);
        System.out.println(n);


    }
}
