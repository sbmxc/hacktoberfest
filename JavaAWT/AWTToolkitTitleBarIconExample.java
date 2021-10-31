import java.io.*;
import java.util.*;
import java.awt.*;
class AWTToolkitTitleBarIconExample{
	Frame f;
	Image m;
	AWTToolkitTitleBarIconExample(){
		f=new Frame();
		m=Toolkit.getDefaultToolkit().getImage("C:\\Users\\Anju Priya V\\OneDrive\\Pictures\\Saved Pictures\\Calculator.png");
		f.setIconImage(m);
		f.setSize(300,300);
		f.setLayout(null);
		f.setVisible(true);
	}
	public static void main(String args[]){
		new AWTToolkitTitleBarIconExample();
	}
}
		