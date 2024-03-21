#include <iostream>

using namespace std;

void matMul(int mat1[][3], int mat2[][3], int result[][3])
{
	cout << "Matrix result is :" <<endl; 
	for(int i=0;i<3;i++)
	{
		for(int j=0;j<3;j++)
		{
			result[i][j] = 0;
			for(int a=0;a<3;a++)
			{	
				result[i][j] += mat1[i][a] * mat2[a][j];
			}
			
			cout << result[i][j] << "  ";
		}
		
		cout << endl;
	}
}

int main()
{
	int mat1[3][3] = {{2,4,5},{5,7,4},{8,7,7}};
	int mat2[3][3] = {{5,4,7},{8,11,5},{7,5,1}};
	int result[3][3];
	
	matMul(mat1, mat2, result);
}