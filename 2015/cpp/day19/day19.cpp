#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <map>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    ifstream file("2015/inputs/day19.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    map<string, vector<string>> reaction_map;

    string line;
    while (getline(file, line))
    {
        if (line.empty())
        {
            break;
        }

        istringstream iss(line);
        vector<string> list;
        string tmp;
        while (getline(iss, tmp, ' '))
        {
            list.push_back(tmp);
        }
        if (reaction_map.find(list[0]) == reaction_map.end())
        {
            reaction_map[list[0]] = {};
        }
        reaction_map[list[0]].push_back(list[2]);
    }
    getline(file, line);

    string input_molecule = line;

    file.close();

    return 0;
}