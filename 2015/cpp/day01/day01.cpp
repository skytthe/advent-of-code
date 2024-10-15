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
    int floor = 0;

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
    }

    cout << "Part 1:" << endl
         << floor << endl;

    file.close();

    return 0;
}