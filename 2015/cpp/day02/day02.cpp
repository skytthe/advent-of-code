#include <algorithm>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream file("2015/inputs/day02.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    unsigned int paper = 0;
    int box_dim[3];

    string line;
    string tmp;
    while (getline(file, line))
    {
        stringstream ss(line);
        getline(ss, tmp, 'x');
        box_dim[0] = stoi(tmp);
        getline(ss, tmp, 'x');
        box_dim[1] = stoi(tmp);
        getline(ss, tmp, 'x');
        box_dim[2] = stoi(tmp);

        paper += 2 * box_dim[0] * box_dim[1] + 2 * box_dim[1] * box_dim[2] +
                 2 * box_dim[2] * box_dim[0];

        sort(box_dim, box_dim + 3);

        paper += box_dim[0] * box_dim[1];
    }

    cout << "Part 1:" << endl
         << paper << endl;

    file.close();

    return 0;
}
