#include<iostream>
using namespace std; 

class Node{
    public:
    int data;
    Node* next;

    Node(int data){
        this->data=data;
        this->next=NULL;
    }
    //destructor
    ~Node() {
        int value = this -> data;
        //memory free
        if(this->next != NULL) {
            delete next;
            this->next = NULL;
        }
        cout << " memory is free for node with data " << value << endl;
    }
    

};


void insertAtHead(Node* &head, int data){
    Node* temp = new Node(data);
    temp -> next=head;
    head = temp;
}
void insertAtTail(Node* &tail,int data){
    Node* temp = new Node(data);
    tail->next=temp;
    tail=temp;
}
void insertAtIndex(Node* &head, Node* & tail , int position, int data){

    if (position==1){
        insertAtHead(head,data);
        return;
    }

    Node* temp=head;


    int counter=1;
    while(counter<position-1){
        temp=temp->next;
        counter++;
    }

    if (temp->next==NULL){
        insertAtTail(tail,data);
        return;
    }

    Node* element = new Node(data);
    element->next=temp->next; 
    temp->next=element;

}
void deleteNode(Node* &head, int position){

    if(position==1){
        Node* temp=head;
        head=head->next;
        delete temp;
    }
    else{

        int counter=1;
        Node* pre=head;
        Node* current=head;
    
        while(counter<position){
            pre=current;
            current=current->next;
            counter++;
        }

        if(current->next==NULL){
            pre->next=NULL;
            current->next=NULL;
            delete current;
            return;
            
        }

        pre->next=current->next;
        current->next=NULL;
        delete current;


    }

    

}

void reverse(Node* &head, int data){
    
}

void printLL(Node* head){
    Node* temp=head;
    while(temp!=NULL){
        cout<<temp->data<<" ";
        temp=temp->next;
    }     
    cout<<endl;
}

int main()
{

    Node* node = new Node(0);
    Node* nodeTail= node;
    for(int i=1; i<=10; i++){
        insertAtTail(nodeTail, i);
    }

    insertAtIndex(node, node ,5, 99);
    printLL(node);     
    deleteNode(node , 12);
    printLL(node);     


 
    
    return 0;
}
