import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
class DialogExample{
	Frame f;
	Dialog d;
	Label l;
	Button b;
	DialogExample(){
	f=new Frame();
	d=new Dialog(f);
	d.setLayout(new FlowLayout());
	l=new Label("Click That Button");
	l.setBounds(50,100,100,100);
	b=new Button("Click me");
	b.setBounds(60,100,100,100);
	b.addActionListener(new ActionListener(){
		public void actionPerformed(ActionEvent e){
		d.setVisible(false);
		}
	});
	d.add(l);
	d.add(b);
	d.setSize(400,400);
	d.setVisible(true);
	
	}
	public static void main(String args[]){
		new DialogExample();
	}
}