#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <map>
#include <set>
#include <numeric>
#include <algorithm>
#include <climits>
#include <cctype>

using namespace std;

void dispay(int h, int w, bool **matrix){
    for (int y = 0; y < h; y++)
    {
        for (int x = 0; x < w; x++)
        {
            cout << ((matrix[y][x]) ? '#' : '.');
        }
        cout << endl;
    }
    
}

int main() 
{
   #define STEPS 100
    #define SIZE_Y 100
    #define SIZE_X 100
    ifstream file("2015/inputs/day18.txt");
    // #define STEPS 4
    // #define SIZE_Y 6
    // #define SIZE_X 6
    // ifstream file("2015/inputs/day18_s.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    // false off, true on
    bool **matrix1 = new bool*[SIZE_Y];
    bool **next_matrix1 = new bool*[SIZE_Y];
    for (int i = 0; i < SIZE_Y; i++)
    {
        matrix1[i] = new bool[SIZE_X];
        fill(matrix1[i], matrix1[i] + SIZE_X, false);

        next_matrix1[i] = new bool[SIZE_X];
        fill(next_matrix1[i], next_matrix1[i] + SIZE_X, false);

    }

    bool **matrix2 = new bool*[SIZE_Y];
    bool **next_matrix2 = new bool*[SIZE_Y];
    for (int i = 0; i < SIZE_Y; i++)
    {
        matrix2[i] = new bool[SIZE_X];
        fill(matrix2[i], matrix2[i] + SIZE_X, false);

        next_matrix2[i] = new bool[SIZE_X];
        fill(next_matrix2[i], next_matrix2[i] + SIZE_X, false);

    }


    string line;
    char ch;
    int y = 0;
    while (getline(file, line))
    {
        for (int x = 0; x < line.size(); x++)
        {
            if (line.at(x) == '#')
            {
                matrix1[y][x] = true;
                matrix2[y][x] = true;
            }
        }
        y++;
    }


    const int corners[4][2] = {{0,0},{SIZE_Y-1,0},{0,SIZE_X-1},{SIZE_Y-1,SIZE_X-1}};
    for(auto c : corners) 
    {
        matrix2[c[0]][c[1]] = true;
    }


    const int EightNeighbors[8][2] = {
        {-1, -1}, {-1, 0}, {-1, 1},
        { 0, -1},         { 0, 1},
        { 1, -1}, { 1, 0}, { 1, 1}
    };

    for (int steps = 0; steps < STEPS; steps++)
    {
        for (int y = 0; y < SIZE_Y; y++)
        {
            for (int x = 0; x < SIZE_X; x++)
            {
                next_matrix1[y][x] = false;
                next_matrix2[y][x] = false;
                int neighbors1 = 0;
                int neighbors2 = 0;
                for (size_t i = 0; i < 8; i++)
                {
                    int tmpY = y + EightNeighbors[i][0];
                    int tmpX = x + EightNeighbors[i][1];
                    if (tmpY >= 0 && tmpY < SIZE_Y && tmpX >= 0 && tmpX < SIZE_X)
                    {
                        if(matrix1[tmpY][tmpX]){
                            neighbors1++;
                        } 
                        if(matrix2[tmpY][tmpX]){
                            neighbors2++;
                        } 
                    }            
                }
                if (matrix1[y][x])
                {
                    next_matrix1[y][x] = (neighbors1 == 2 || neighbors1 == 3);
                }
                else
                {           
                    next_matrix1[y][x] = (neighbors1 == 3);
                }
                //part 2
                if (matrix2[y][x])
                {
                    next_matrix2[y][x] = (neighbors2 == 2 || neighbors2 == 3);
                }
                else
                {           
                    next_matrix2[y][x] = (neighbors2 == 3);
                }

            }    
        }
        for (int y = 0; y < SIZE_Y; y++)
        {
            for (int x = 0; x < SIZE_X; x++)
            {
                matrix1[y][x] = next_matrix1[y][x];
                matrix2[y][x] = next_matrix2[y][x];
            }        
        }
        matrix2[0][0] = true;
        matrix2[0][SIZE_X - 1] = true;
        matrix2[SIZE_Y - 1][0] = true;
        matrix2[SIZE_Y - 1][SIZE_X - 1] = true;
        // cout << "After " << steps << " steps:" << endl;
        // dispay(SIZE_Y, SIZE_X, matrix);
    }
    
    int count_lights1 = 0;
    int count_lights2 = 0;
    for (int y = 0; y < SIZE_Y; y++)
    {
        for (int x = 0; x < SIZE_X; x++)
        {
            if(matrix1[y][x]){
                count_lights1++;
            } 
            if(matrix2[y][x]){
                count_lights2++;
            } 
            
        }        
    }

    cout << "Part 1:" << endl
         << count_lights1 << endl;

    cout << "Part 2:" << endl
         << count_lights2 << endl;


    for (int i = 0; i < SIZE_Y; i++)
    {
        delete[] matrix1[i];
        delete[] next_matrix1[i];
    }
    delete[] matrix1;
    delete[] next_matrix1;

    return 0;
}