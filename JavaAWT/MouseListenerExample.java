import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
public class MouseListenerExample implements MouseListener{
	Frame f;
	Label l;
	MouseListenerExample(){
		f=new Frame();
		l=new Label();
		l.setBounds(20,50,100,20);
		f.add(l);
		f.addMouseListener(this);
		f.setSize(500,500);
		f.setLayout(null);
		f.setVisible(true);
	}
	public void mouseClicked(MouseEvent e){
		l.setText("Mouse is Clicked");
	}
	public void mouseReleased(MouseEvent e){
		l.setText("Mouse is Released");
	}
	public void mouseEntered(MouseEvent e){
		l.setText("Mouse is Entered");
	}
	public void mouseExited(MouseEvent e){
		l.setText("Mouse is Exited");
	}
	public void mousePressed(MouseEvent e){
		l.setText("Mouse is Pressed");
	}
	public static void main(String args[]){
		new MouseListenerExample();
	}
}
