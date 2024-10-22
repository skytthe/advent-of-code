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
    ifstream file("2015/inputs/day19_s.txt");
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
//                cout << tmp << endl;
                new_molecules.insert(tmp);
            }
        }
    }
    
    std::cout << "Part 1:" << std::endl
              << new_molecules.size() << std::endl;


    // Part 2
    string medicine = molecule;
    molecule = "e";

    set<string> molecules;
    molecules.insert(molecule);

    new_molecules.clear();
    int steps = 0;
    while (true)
    {
        steps++;
        for (auto m: molecules)
        {
            for (int i = 0; i < m.size(); i++)
            {
                left = m.substr(0,i);
                key = m[i];
                if (i < m.size() && islower(m[i+1]))
                {
                    key += m[i+1];
                    i++;
                }
                right = m.substr(i+1);

                auto idx = reaction_map.find(key);
                if (idx != reaction_map.end())
                {
                    for (auto e : idx->second)
                    {
                        tmp = left + e + right;
                        new_molecules.insert(tmp);
                    }
                }
            }
        }
        

        if(new_molecules.count(medicine)){
            break;
        }
        molecules = new_molecules;
        new_molecules.clear();

    }
    
    std::cout << "Part 2:" << std::endl
              << steps << std::endl;

    file.close();

    return 0;
}