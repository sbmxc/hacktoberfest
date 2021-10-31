import java.awt.*;  
import java.awt.event.*;  
class PopupMenuExample implements ActionListener 
{  
Label l;
     PopupMenuExample(){  
        Frame f= new Frame("PopupMenu Example");  
        PopupMenu popupmenu = new PopupMenu("Edit"); 
		 l=new Label();
		 l.setBounds(30,100,120,120);
         MenuItem cut = new MenuItem("Cut");  
         cut.setActionCommand("Cut");  
         MenuItem copy = new MenuItem("Copy");  
         copy.setActionCommand("Copy");  
         MenuItem paste = new MenuItem("Paste");  
         paste.setActionCommand("Paste");      
         popupmenu.add(cut);  
         popupmenu.add(copy);  
         popupmenu.add(paste);        
         f.addMouseListener(new MouseAdapter() {  
            public void mouseClicked(MouseEvent e) {              
                popupmenu.show(f , e.getX(), e.getY());  
            }                 
         });  
		 cut.addActionListener(this);
		 copy.addActionListener(this);
		 paste.addActionListener(this);

		 f.add(l);
         f.add(popupmenu);   
         f.setSize(400,400);  
         f.setLayout(null);  
         f.setVisible(true);  
     }  
	 			 public void actionPerformed(ActionEvent e){
				 String com=e.getActionCommand();
			 if(com.equals("Cut")){
				 l.setText("The Action is cut");
			 }
			 else if(com=="Copy"){
				 l.setText("The Action is copy");
			 }
			 else{
				 l.setText("the Action is paste");
			 }
			 }
		
public static void main(String args[])  
{  
        new PopupMenuExample();  
}  
} 