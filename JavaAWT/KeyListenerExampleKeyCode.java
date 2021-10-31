import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import java.applet.*;
public class KeyListenerExampleKeyCode extends Applet implements KeyListener{
	int x=50,y=50;
	String str=" ";
	public void init(){
		addKeyListener(this);
		requestFocus();
	}
	public void keyReleased(KeyEvent e){
		showStatus("Key is Released");
	}
	public void keyPressed(KeyEvent e){
		showStatus("Key is pressed");
		int code=e.getKeyCode();
		switch(code){
			case KeyEvent.VK_F1:str+="<F1>";
			break;
			case KeyEvent.VK_F2:str+="<F2>";
			break;
			case KeyEvent.VK_F3:str+="<F3>";
			break;
			case KeyEvent.VK_PAGE_UP: str+="<pgup>";
			break;
			case KeyEvent.VK_PAGE_DOWN:str+="<pgdn>";
			break;
			case KeyEvent.VK_LEFT: str+="<Left>";
			break;
			case KeyEvent.VK_RIGHT: str+="<Right>";
			break;
		}
		repaint();
	}
	public void keyTyped(KeyEvent e){
		showStatus("Key Typed");
		str+=e.getKeyChar();
		repaint();
	}
	public void paint(Graphics g){
		g.drawString(str,x,y);
	}
}
/*<applet width=300 height=300 code="KeyListenerExampleKeyCode"></applet>*/