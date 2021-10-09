	
#include<iostream>
using namespace std;

int main()
{
	int n, i, f, m, l, s;
	cout<<"\t\tBinary Search Demonstration";
	cout<<endl<<"Enter total number of elements you want in the array: ";
	cin>>n;
	
	int arr[n];
	cout<<"Enter "<<n<<" numbers: ";
	for (i=0; i<n; i++)
	{
		cin>>arr[i];
	}
	
	cout<<"Enter the number to find: ";
	cin>>s;
	
	f= 0;
	l= n-1;
	m= (f + l)/2;
	
	while(f <= l)
	{
	    if(arr[m] == s)
		{
			cout<<"Element "<<s<<" found at the location "<<m+1;
			break;
		}
		else if(arr[m] < s)
		{
			f = m + 1;
		}
		else
		{
			 l = m - 1;
		}
		m = (f + l)/2;
	}
	
	if(f > l)
	{
		cout<<"Element "<<s<<" is not present in the array.";
	}
	
	return 0;
}
