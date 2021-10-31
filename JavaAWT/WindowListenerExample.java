import java.awt.*;  
import java.awt.event.WindowEvent;  
import java.awt.event.WindowListener;  
class WindowListenerExample extends Frame implements WindowListener{  
    WindowListenerExample(){  
        addWindowListener(this);  
          
        setSize(400,400);  
        setLayout(null);  
        setVisible(true);  
    }  
      
public static void main(String[] args) {  
    new WindowListenerExample();  
}  
public void windowActivated(WindowEvent arg0) {  
    System.out.println("activated");  
}  
public void windowClosed(WindowEvent arg0) {  
    System.out.println("closed");  
}  
public void windowClosing(WindowEvent arg0) {  
    System.out.println("closing");  
    dispose();  
}  
public void windowDeactivated(WindowEvent arg0) {  
    System.out.println("deactivated");  
}  
public void windowDeiconified(WindowEvent arg0) {  
    System.out.println("deiconified");  
}  
public void windowIconified(WindowEvent arg0) {  
    System.out.println("iconified");  
}  
public void windowOpened(WindowEvent arg0) {  
    System.out.println("opened");  
}  
}  