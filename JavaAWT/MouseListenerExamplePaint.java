import java.io.*;
import java.util.*;
import java.applet.*;
import java.awt.*;
import java.awt.event.*;
public class MouseListenerExamplePaint extends Applet{
	int last_x,last_y;
	Color current_color=Color.black;
	Button clear_button;
	Choice color_choices;
	public void init(){
		this.setBackground(Color.white);
		clear_button=new Button("clear");
		clear_button.setForeground(Color.black);
		clear_button.setBackground(Color.lightGray);
		this.add(clear_button);
		color_choices=new Choice();
		color_choices.addItem("Black");
		color_choices.addItem("Red");
		color_choices.addItem("Yellow");
		color_choices.addItem("Green");
		color_choices.setBackground(Color.lightGray);
		color_choices.setForeground(Color.black);
		this.add(color_choices);
	}
	public boolean mouseDown(Event e,int x,int y){
		last_x=x;
		last_y=y;
		return true;
	}
	public boolean mouseDrag(Event e,int x,int y){
		Graphics g=this.getGraphics();
		g.setColor(current_color);
		g.drawLine(last_x,last_y,x,y);
		last_x=x;
		last_y=y;
		return true;
	}
	public boolean action(Event event ,Object arg){
		if(event.target==clear_button){
			Graphics g=this.getGraphics();
			Rectangle r=this.bounds();
			g.setColor(this.getBackground());
			g.fillRect(r.x,r.y,r.width,r.height);
			return true;
		}
		else if(event.target==color_choices){
			if(arg.equals("Black")){
				current_color=Color.black;
			}
			else if(arg.equals("Red")){
				current_color=Color.red;
			}
			else if(arg.equals("Yellow")){
				current_color=Color.yellow;
			}
			else if(arg.equals("Green")){
				current_color=Color.green;
			}
			return true;
		}
		else {
			return super.action(event,arg);
		}
	}
}
/*<applet width=500 height=500 code="MouseListenerExamplePaint.class"></applet>*/