import java.io.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import java.applet.*;
public class KeyListenerExampleKeyChar extends Applet implements KeyListener{
	String str=" ";
	int x=50,y=50;
public void init(){
addKeyListener(this);
requestFocus();
}
public void keyPressed(KeyEvent e){
	showStatus("Key is pressed");
}
public void keyReleased(KeyEvent e){
	showStatus("Key is released");
}
public void keyTyped(KeyEvent e){
	str+=e.getKeyChar();
	repaint();
}
public void paint(Graphics g){
	g.drawString(str,x,y);
}
}
/*<applet width=500 height=500 code="KeyListenerExampleKeyChar.class"></applet>*/