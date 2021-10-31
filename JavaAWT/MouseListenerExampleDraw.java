import java.io.*;
import java.util.*;
import java.awt.*;
import java.applet.*;
import java.awt.event.*;
public class MouseListenerExampleDraw extends Applet implements MouseListener,MouseMotionListener{
	int last_x,last_y;
	public void init(){
		addMouseMotionListener(this);
		addMouseListener(this);
	}
	public void mousePressed(MouseEvent e){
		last_x=e.getX();
		last_y=e.getY();
	}
	public void mouseDragged(MouseEvent e){
		int x=e.getX(),y=e.getY();
		Graphics g=this.getGraphics();
		g.drawLine(last_x,last_y,x,y);
		last_x=x;
		last_y=y;
	}
	public void mouseClicked(MouseEvent e){
		showStatus("Mouse is clicked");
	}
	public void mouseReleased(MouseEvent e){
		showStatus("Mouse is mouseReleased");
		}
	public void mouseMoved(MouseEvent e){ 
			showStatus("Mouse is mouseMoved");
}
	public void mouseEntered(MouseEvent e){ 
			showStatus("Mouse is mouseEntered");
}
	public void mouseExited(MouseEvent e){ 
			showStatus("Mouse is mouseExited");
}
}
/*<applet width=300 height=300 code="MouseListenerExampleDraw.class"></applet>*/
		
	
