import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
class AWTTextFieldExample{
	Frame f;
	TextField t1;
	TextField t2;
	TextField t3;
	Button b1;
	Button b2;
	Button b3;
	AWTTextFieldExample(){
		f=new Frame();
		t1=new TextField();
		t1.setBounds(50,50,150,20);
		t2=new TextField();
		t2.setBounds(50,100,150,20);
		t3=new TextField();
		t3.setBounds(50,150,150,20);
		t3.setEditable(false);
		b1=new Button("Add");
		b1.setBounds(50,200,50,50);
		b1.setActionCommand("Add");
		b1.addActionListener(new DoOperation());
		b2=new Button("Sub");
		b2.setBounds(190,200,50,50);
		b2.setActionCommand("Sub");
		b2.addActionListener(new DoOperation());
		b3=new Button("Mul");
		b3.setBounds(120,200,50,50);
		b3.setActionCommand("Mul");
		b3.addActionListener(new DoOperation());
		f.add(t1);
		f.add(t2);
		f.add(t3);
		f.add(b1);
		f.add(b2);
		f.add(b3);
		f.setSize(400,400);
		f.setLayout(null);
		f.setVisible(true);
		
	}
	public class DoOperation implements ActionListener{
		public void actionPerformed(ActionEvent e){
			String com=e.getActionCommand();
			if(com.equals("Add")){
			int value1,value2,result;
			String str1,str2,textResult;
			str1=t1.getText();
			value1=Integer.parseInt(str1);
			str2=t2.getText();
			value2=Integer.parseInt(str2);
			result=value1+value2;
			textResult=String.valueOf(result);
			t3.setText(textResult);
			}
			else if(com.equals("Mul")){
			int value1,value2,result;
			String str1,str2,textResult;
			str1=t1.getText();
			value1=Integer.parseInt(str1);
			str2=t2.getText();
			value2=Integer.parseInt(str2);
			result=value1*value2;
			textResult=String.valueOf(result);
			t3.setText(textResult);
			}
			else{
			int value1,value2,result;
			String str1,str2,textResult;
			str1=t1.getText();
			value1=Integer.parseInt(str1);
			str2=t2.getText();
			value2=Integer.parseInt(str2);
			result=value1-value2;
			textResult=String.valueOf(result);
			t3.setText(textResult);
			}
				
		}
	}
	public static void main(String args[]){
	new TextFieldExample();
	}
}
