#include <iostream>
#include <fstream>
#include <string>
#include <set>

using namespace std;

int main()
{
    ifstream file("2015/inputs/day03.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    char ch;
    set<string> visited1;
    int x = 0;
    int y = 0;

    unsigned int steps = 0;
    set<string> visited2;
    int x1 = 0;
    int y1 = 0;
    int x2 = 0;
    int y2 = 0;

    visited1.insert(to_string(x) + "," + to_string(y));
    visited2.insert(to_string(x1) + "," + to_string(y1));

    while (file.get(ch))
    {
        switch (ch)
        {
        case '^':
            y++;
            (steps % 2 == 0) ? y1++ : y2++;
            break;
        case 'v':
            y--;
            (steps % 2 == 0) ? y1-- : y2--;
            break;
        case '<':
            x--;
            (steps % 2 == 0) ? x1-- : x2--;
            break;
        case '>':
            x++;
            (steps % 2 == 0) ? x1++ : x2++;
            break;
        default:
            cerr << "Error: Unexpected Input." << endl;
            return 1;
        }
        visited1.insert(to_string(x) + "," + to_string(y));

        string tmp = (steps % 2 == 0) ? to_string(x1) + "," + to_string(y1) : to_string(x2) + "," + to_string(y2);
        visited2.insert(tmp);
        steps++;
    }

    cout << "Part 1:" << endl
         << visited1.size() << endl;

    cout << "Part 2:" << endl
         << visited2.size() << endl;

    return 0;
}