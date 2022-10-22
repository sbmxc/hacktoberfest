#include<iostream>
using namespace std;

class Node{
    public:
    Node* next;
    Node* pre;
    int data;

    Node(int data){
        this->data=data;
        this->next=NULL;
        this->pre=NULL;
         
    }    
};


void InsertAtHead(Node* &head ,int data){

    Node* temp= new Node(data);

    temp->next=head;
    head ->pre=temp ;
    head=temp; 

}
void InsertAtTail(Node* &tail , int data){
    Node* temp=new Node(data);
   
    
    tail->next=temp;
    temp->pre=tail;
    tail=temp;

}
void InsertAtIndex(Node* &head ,Node* &tail, int position,int data){


    if (position==1){
        InsertAtHead(head,data);
        return;
    }
    Node* temp=head;

    int counter=1;
    while(counter<position-1){
        temp=temp->next;
        counter++;
    }

    if(temp->next==NULL){
        InsertAtTail(tail,data);
        return;
    }

    Node* InsertElement=new Node(data);

    InsertElement->next=temp->next;
    temp->next->pre=InsertElement;
    temp->next=InsertElement;
    InsertElement->pre=temp;    

}
void DeleteNode(Node* &head ,int position){ 
    if (position==1){
        Node* temp=head;
        temp->next->pre=NULL;
        head=temp->next;
        temp->next=NULL;
        delete temp;
    }

    else{

        Node* curr=head;
        Node* prev=NULL;

        int counter =1;
        
        while(counter<position){
            prev=curr;
            curr=curr->next;
            counter++;
         }

         prev->next=curr->next;
         //  curr->next->pre=curr->pre;
         curr->next=NULL; 
         curr->pre=NULL; 
         delete curr;




    }

}
void printNode(Node* &head ) {
    Node* temp=head;

    while (temp!=NULL){
        cout<<temp->data<<" ";
        temp=temp->next;
    }
    cout<<endl;
}

int main()
{

    Node* head =new Node(20);

    Node* Head=head;
    Node* Tail=head;

    InsertAtTail(Tail,101); 
    InsertAtTail(Tail,102);
    InsertAtTail(Tail,103);
    InsertAtTail(Tail,104);
    InsertAtTail(Tail,105);
    InsertAtIndex(Head,Tail,5 ,200);
    DeleteNode(Head,4);
    printNode(Head);
    
    return 0;
    
    }