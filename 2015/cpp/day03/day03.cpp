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
    set<string> visited;
    int x = 0;
    int y = 0;

    visited.insert(to_string(x) + "," + to_string(y));

    while (file.get(ch))
    {
        switch (ch)
        {
        case '^':
            y++;
            break;
        case 'v':
            y--;
            break;
        case '<':
            x--;
            break;
        case '>':
            x++;
            break;
        default:
            cerr << "Error: Unexpected Input." << endl;
            return 1;
        }
        visited.insert(to_string(x) + "," + to_string(y));
    }

    cout << "Part 1:" << endl
         << visited.size() << endl;

    return 0;
}