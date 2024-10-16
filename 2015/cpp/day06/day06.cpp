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
    bool matrix[SIZE_Y][SIZE_X] = {false};

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
                    matrix[y][x] = !matrix[y][x];
                    break;
                case TURN_ON:
                    matrix[y][x] = true;
                    break;
                case TURN_OFF:
                    matrix[y][x] = false;
                    break;
                default:
                    break;
                }
            }
        }
    }

    int count_lights = 0;
    for (int y = 0; y < SIZE_Y; y++)
    {
        for (int x = 0; x < SIZE_X; x++)
        {
            if (matrix[y][x])
            {
                count_lights++;
            }
        }
    }

    cout << "Part 1:" << endl
         << count_lights << endl;

    return 0;
}