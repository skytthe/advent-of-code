#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    ifstream file("2015/inputs/day01.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    char ch;
    unsigned int step = 1;
    int floor = 0;
    unsigned int enter_basement = 0;

    while (file.get(ch))
    {
        if (ch == '(')
        {
            floor++;
        }
        else if (ch == ')')
        {
            floor--;
        }
        else
        {
            cerr << "Error: Unexpected Input." << endl;
            return 1;
        }

        if (enter_basement == 0 && floor < 0)
        {
            enter_basement = step;
        }

        step++;
    }

    cout << "Part 1:" << endl
         << floor << endl;

    cout << "Part 2:" << endl
         << enter_basement << endl;

    file.close();

    return 0;
}