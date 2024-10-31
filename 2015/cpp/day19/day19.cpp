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

double averageStringLength(const vector<string>& strings) {
    if (strings.empty()) {
        return 0.0;  
    }

    int sum = 0;
    for (const auto &s :strings)
    {
        sum += s.size();
    }
    
    return static_cast<double>(sum) / strings.size();
}


int main()
{
    ifstream file("2015/inputs/day19.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    map<string, vector<string>> reaction_map;
    vector<std::pair<string,string>> reverse_reactions;

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
        reverse_reactions.push_back({list[2],list[0]});
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
    /*
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
*/
    vector<string> molecules;
    molecules.push_back(molecule);
    new_molecules.clear();

    int steps = 0;
    bool found = false;
    while (true)       
    {
        steps++;
        // cout << "steps: " << steps << endl;
        for (const auto &m : molecules)
        {
            for (const auto &r : reverse_reactions)
            {
                size_t pos = m.find(r.first);
                while (pos != string::npos)
                {
                    tmp = m.substr(0,pos) + r.second + m.substr(pos+r.first.size());
                
                    if (r.second != "e" )
                    {
                        new_molecules.insert(tmp);
                    }                    
                    if(tmp == "e")
                    {
                        found = true;
                        break;
                    }
                    pos = m.find(r.first, pos+1);
                }
                
            }
        }
        if(found || steps == 210) {
            break;
        }

        molecules = vector<string>(new_molecules.begin(), new_molecules.end());
        sort(molecules.begin(), molecules.end(), [](const string& first, const string& second){return first.size() < second.size();});
        #define MOLECULES_TO_KEEP 1
        // #define MOLECULES_TO_KEEP 10    // Do not work!
        // #define MOLECULES_TO_KEEP 100
        if (molecules.size() >= MOLECULES_TO_KEEP)
        {
            molecules.resize(MOLECULES_TO_KEEP);
        }
        new_molecules.clear();

        // cout << "molecules size: " << molecules.size() << endl;
        // cout << "molecules avg len: " << averageStringLength(molecules) << endl << endl;
    }

    std::cout << "Part 2:" << std::endl
              << steps << std::endl;

    file.close();
    return 0;
}