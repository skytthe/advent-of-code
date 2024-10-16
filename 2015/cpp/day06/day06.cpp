#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

using namespace std;

#define SIZE_Y 1000
#define SIZE_X 1000

typedef enum
{
    TOGGLE,
    TURN_ON,
    TURN_OFF
} action;

int main()
{
    ifstream file("2015/inputs/day06.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    // false off, true on
    bool matrix1[SIZE_Y][SIZE_X] = {false};
    int matrix2[SIZE_Y][SIZE_X] = {false};

    string line;
    action act;
    while (getline(file, line))
    {
        if (line.substr(0, 6) == "toggle")
        {
            act = TOGGLE;
            line = line.substr(7);
        }
        else
        {
            if (line.substr(5, 2) == "on")
            {
                act = TURN_ON;
                line = line.substr(8);
            }
            else if (line.substr(5, 3) == "off")
            {
                act = TURN_OFF;
                line = line.substr(9);
            }
            else
            {
                cerr << "Error: unknwon action." << endl;
                return 1;
            }
        }
        line.replace(line.find(" through "), 9, ",");

        stringstream ss(line);
        string tmp;
        vector<int> box;
        while (getline(ss, tmp, ','))
        {
            box.push_back(stoi(tmp));
        }

        for (int y = box[1]; y <= box[3]; y++)
        {
            for (int x = box[0]; x <= box[2]; x++)
            {
                switch (act)
                {
                case TOGGLE:
                    matrix1[y][x] = !matrix1[y][x];
                    matrix2[y][x] += 2;
                    break;
                case TURN_ON:
                    matrix1[y][x] = true;
                    matrix2[y][x] += 1;
                    break;
                case TURN_OFF:
                    matrix1[y][x] = false;
                    if (matrix2[y][x] > 0)
                    {
                        matrix2[y][x] += -1;
                    }
                    break;
                default:
                    break;
                }
            }
        }
    }

    int count_lights1 = 0;
    int count_lights2 = 0;
    for (int y = 0; y < SIZE_Y; y++)
    {
        for (int x = 0; x < SIZE_X; x++)
        {
            if (matrix1[y][x])
            {
                count_lights1++;
            }

            count_lights2 += matrix2[y][x];
        }
    }

    cout << "Part 1:" << endl
         << count_lights1 << endl;

    cout << "Part 2:" << endl
         << count_lights2 << endl;

    file.close();

    return 0;
}