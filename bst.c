//BINARY SEARCH TREE
#include <stdio.h>
#include <stdlib.h>
struct Node
{

struct Node *lchild;

int data;

struct Node *rchild;

} *root = NULL;

void
Insert (int key)
{

struct Node *t = root;

struct Node *r = NULL, *p;


if (root == NULL)

    {

p = (struct Node *) malloc (sizeof (struct Node));

p->data = key;

p->lchild = p->rchild = NULL;

root = p;

return;

}

while (t != NULL)

    {

r = t;

if (key < t->data)

t = t->lchild;

      else if (key > t->data)

t = t->rchild;

      else

return;

}

p = (struct Node *) malloc (sizeof (struct Node));

p->data = key;

p->lchild = p->rchild = NULL;


if (key < r->data)
    r->lchild = p;

  else
    r->rchild = p;

}


void
Inorder (struct Node *p)
{

if (p)

    {

Inorder (p->lchild);

printf ("%d ", p->data);

Inorder (p->rchild);

}

}


void
Preorder (struct Node *p)
{

if (p)

    {

printf ("%d ", p->data);

Preorder (p->lchild);

Preorder (p->rchild);

}

}


void
Postorder (struct Node *p)
{

if (p)

    {

Postorder (p->lchild);

Postorder (p->rchild);

printf ("%d ", p->data);

}

}


void
Smallest (struct Node *p)
{

if (p == NULL || p->lchild == NULL)

    {

printf ("%d\n", p->data);

}

  else

    {

Smallest (p->lchild);

}

}


void
Largest (struct Node *p)
{

if (p == NULL || p->rchild == NULL)

    {

printf ("%d\n", p->data);

}

  else

    {

Largest (p->rchild);

}

}


int
Totalnodes (struct Node *p)
{

int x, y;

if (p != NULL)

    {

x = Totalnodes (p->lchild);

y = Totalnodes (p->rchild);

return x + y + 1;

}

return 0;

}


int
Height (struct Node *p)
{

int lh, rh;


if (p == NULL)

    {

return 0;

}

  else

    {

lh = Height (p->lchild);

rh = Height (p->rchild);

if (lh > rh)

	{

return lh + 1;

}

      else

	{

return rh + 1;

}

}

}


int
Leafnodes (struct Node *p)
{

int x, y;

if (p != NULL)

    {

x = Leafnodes (p->lchild);

y = Leafnodes (p->rchild);

if (p->lchild == NULL && p->rchild == NULL)

	{

return x + y + 1;

}

      else

	{

return x + y;

}

}

return 0;

}


/*Non_Leafnodes (struct Node * p)
{
if (p == NULL || ((p->lchild == NULL) && (p->rchild == NULL)))
    {
printf ("0");
}
  else
    {
        int x=Non_Leafnodes (root->lchild);
        int y=Non_Leafnodes (root->rchild);
int c =
	1 + x + y;
printf ("%d", c);
}
}*/

void MirrorImage(struct Node *p)

{
    struct Node *temp;

    if(p!=NULL)

    {

        MirrorImage(p->lchild);

        MirrorImage(p->rchild);

        temp=p->lchild;

        p->lchild=p->rchild;

        p->rchild=temp;

    }

    return;

}

struct Node *InPre(struct Node *p)

{

    while(p && p->rchild!=NULL)

    p=p->rchild;

    return p;

}

struct Node *InSucc(struct Node *p)

{
    while(p && p->lchild!=NULL)

    p=p->lchild;

    return p;
}

struct Node *Delete(struct Node *p,int key)

{
  struct Node *q;

  if(p==NULL)

  return NULL;

  if(p->lchild==NULL && p->rchild==NULL)

  {

  if(p==root)

  root=NULL;

  free(p);

  return NULL;

  }

  if(key < p->data)

  p->lchild=Delete(p->lchild,key);

  else if(key > p->data)

  p->rchild=Delete(p->rchild,key);

  else

  {

  if(Height(p->lchild)>Height(p->rchild))

  {

  q=InPre(p->lchild);

  p->data=q->data;

  p->lchild=Delete(p->lchild,q->data);

  }

  else

  {

  q=InSucc(p->rchild);

  p->data=q->data;

  p->rchild=Delete(p->rchild,q->data);

  }

  }
  return p;}
int

main ()
{

Insert (50);

Insert (10);

Insert (40);

Insert (20);

Insert (30);

Insert (60);

Insert (70);

Insert (80);

Insert (90);

printf ("INORDER:\n");

Inorder (root);

printf ("\n");

printf ("PREORDER:\n");

Preorder (root);

printf ("\n");

printf ("POSTORDER:\n");

Postorder (root);

printf ("\n");

printf ("SMALLEST ELEMENT:\n");

Smallest (root);

printf ("LARGEST ELEMENT:\n");

Largest (root);

printf ("TOTAL NODES:\n");

int k = Totalnodes (root);

printf ("%d", k);

printf ("\nHEIGHT OF BST:");

int h = Height (root);

printf ("\n%d\n", h);

printf ("LEAF NODES:");

int ln = Leafnodes (root);

printf ("\n%d\n", ln);

//Non_Leafnodes (root);
printf("CONVERTIING BST TO ITS MIRROR IMAGE\n");

MirrorImage(root);

printf("INORDER OF MIRROR:\n");

Inorder(root);

printf("CONVERTIING MIRROR TO ITS BST AGAIN\n");

MirrorImage(root);

printf("INORDER OF ORIGINAL MIRROR:\n");

Inorder(root);

Delete(root,40);

printf("\nNORDER AFTER DELETING 40:\n");

Inorder(root);

Delete(root,60);

printf("\nINORDER AFTER DELETING 60:\n");

Inorder(root);

return 0;

}

