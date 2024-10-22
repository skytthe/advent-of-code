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

    string molecule = line;

    set<string> new_molecules;
    string key;
    string left, right, tmp;
    for (int i = 0; i < molecule.size(); i++)
    {
        left = molecule.substr(0,i);
        key = molecule[i];
        if (i < molecule.size() && islower(molecule[i+1]))
        {
            key += molecule[i+1];
            i++;
        }
        right = molecule.substr(i+1);

        auto idx = reaction_map.find(key);
        if (idx != reaction_map.end())
        {
            for (auto e : idx->second)
            {
                tmp = left + e + right;
                cout << tmp << endl;
                new_molecules.insert(tmp);
            }
        }
    }
    
    std::cout << "Part 1:" << std::endl
              << new_molecules.size() << std::endl;


    file.close();

    return 0;
}