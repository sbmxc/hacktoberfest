#include<iostream>
#include<bits/stdc++.h>
#include<vector>
using namespace std;

int main(){
	int n,q,s,w,pos,num;
	cout<<"Enter total no. of arrays: ";
	cin>>n;
	cout<<"Enter no of queries to be performed: ";
	cin>>q;

	vector<vector<int> > vec;
	for(int i=0;i<n;i++){
		cout<<"Enter size of array: ";
		cin>>s;

		vector<int> innervec;
		for(int i=0;i<s;i++){
			cin>>num;
			innervec.push_back(num);
		}
		vec.push_back(innervec);
	}
	for(int i=0;i<q;i++){
		cout<<"which array: ";
		cin>>w;
		cout<<"which position: ";
		cin>>pos;
		cout<<vec[w][pos]<<endl;
	}
}