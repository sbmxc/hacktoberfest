#include<iostream>
using namespace std;

class Node{
    public:
    Node *next; 
    int data;
    

    Node(int data){
        this->data=data;
        this->next=NULL;
    }

    ~Node(){
        int value=this->data;
        if(this->next!=NULL){
            next=NULL;
            delete next;
        }
        cout<<"Memory Free for value "<<data<<endl;
    }
};


// void insertAtHead(Node* &head,Node* &tail,int data){
//     Node* newnode=new Node(data); 
//     newnode->next=head;
//     tail->next=newnode;
//     head=newnode;
//}

void insertNode(Node* &tail,int element ,int data){
 
    if(tail == NULL){
        Node* newnode=new Node(data);
        tail=newnode;
        newnode->next=newnode;    
    }
    else{
        Node* curr=tail;

        while(curr->data!=element){
            curr=curr->next;
        }

        Node* newnode=new Node(data);
        newnode->next=curr->next;
        curr->next=newnode;
    }
}

void DeleteNode(Node* &tail, int element ){

    if(tail==NULL){
        cout<<"Empty LL"<<endl;
    }
    else{

        Node* previous=tail;
        Node* curr=previous->next;


        while(curr->data != element){
            previous=curr;
            curr=curr->next;
        }
        previous->next=curr->next;
        if(curr==previous){
            tail=NULL;
        }
        else if(tail==curr){
            tail=previous;
        }
        curr->next=NULL;
        delete curr;
    }
}

void printLL(Node* &tail){
    Node* temp=tail;
    do{    
        cout<<tail->data<<" ";
        tail=tail->next;
    }
    while(tail !=temp);
    cout<<endl;
}




int main()
{
    
    Node* tail=NULL;

    
    insertNode(tail,1,10);
    insertNode(tail,10,20);
    insertNode(tail,20,30);
    insertNode(tail,30,50);
    insertNode(tail,50,60);
    insertNode(tail,60,70);
    insertNode(tail,10,422);



    printLL(tail);

    DeleteNode(tail,10);

    printLL(tail);

    return 0;
}
