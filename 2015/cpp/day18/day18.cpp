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
    bool **matrix = new bool*[SIZE_Y];
    bool **next_matrix = new bool*[SIZE_Y];
    for (int i = 0; i < SIZE_Y; i++)
    {
        matrix[i] = new bool[SIZE_X];
        fill(matrix[i], matrix[i] + SIZE_X, false);

        next_matrix[i] = new bool[SIZE_X];
        fill(next_matrix[i], next_matrix[i] + SIZE_X, false);

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
                matrix[y][x] = true;
            }
        }
        y++;
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
                next_matrix[y][x] = false;
                int neighbors = 0;
                for (size_t i = 0; i < 8; i++)
                {
                    int tmpY = y + EightNeighbors[i][0];
                    int tmpX = x + EightNeighbors[i][1];
                    if (tmpY >= 0 && tmpY < SIZE_Y && tmpX >= 0 && tmpX < SIZE_X)
                    {
                        if(matrix[tmpY][tmpX]){
                            neighbors++;
                        } 
                    }            
                }
                if (matrix[y][x])
                {
                    next_matrix[y][x] = (neighbors == 2 || neighbors == 3);
                }
                else
                {           
                    next_matrix[y][x] = (neighbors == 3);
                }

            }    
        }
        for (int y = 0; y < SIZE_Y; y++)
        {
            for (int x = 0; x < SIZE_X; x++)
            {
                matrix[y][x] = next_matrix[y][x];
            }        
        }
        // cout << "After " << steps << " steps:" << endl;
        // dispay(SIZE_Y, SIZE_X, matrix);
    }
    
    int count_lights = 0;
    for (int y = 0; y < SIZE_Y; y++)
    {
        for (int x = 0; x < SIZE_X; x++)
        {
            if(matrix[y][x]){
                count_lights++;
            } 
            
        }        
    }

    cout << "Part 1:" << endl
         << count_lights << endl;


    for (int i = 0; i < SIZE_Y; i++)
    {
        delete[] matrix[i];
        delete[] next_matrix[i];
    }
    delete[] matrix;
    delete[] next_matrix;

    return 0;
}