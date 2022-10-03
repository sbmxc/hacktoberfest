/*
Problem Link- https://leetcode.com/problems/sudoku-solver/
*/
class Solution
{
public:
    bool isValid(vector<vector<char>> &board, int i, int j, char k)
    {

        for (int i = 0; i < 9; i++)
            if (board[i][j] == k)
                return false;

        for (int j = 0; j < 9; j++)
            if (board[i][j] == k)
                return false;

        int r = (i / 3) * 3, c = (j / 3) * 3;

        for (int p = r; p < r + 3; p++)
        {
            for (int l = c; l < c + 3; l++)
            {
                if (board[p][l] == k)
                    return false;
            }
        }
        return true;
    }

    bool sudokuUtil(vector<vector<char>> &board)
    {

        for (int i = 0; i < board.size(); i++)
        {
            for (int j = 0; j < board[0].size(); j++)
            {

                if (board[i][j] == '.')
                {
                    for (char k = '1'; k <= '9'; k++)
                    {

                        if (isValid(board, i, j, k))
                        {
                            board[i][j] = k;
                            if (sudokuUtil(board))
                                return true;
                            else
                                board[i][j] = '.';
                        }
                    }
                    return false;
                }
            }
        }
        return true;
    }

    void solveSudoku(vector<vector<char>> &board)
    {
        sudokuUtil(board);
    }
};