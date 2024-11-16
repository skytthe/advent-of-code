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
#include <cfloat>
#include <cctype>

using namespace std;

int main()
{
    std::ifstream file("2015/inputs/day16.txt");
    if (!file.is_open())
    {
        std::cerr << "Error: Could not open the file." << std::endl;
        return 1;
    }

    int children = 3;
    int cats = 7;
    int samoyeds = 2;
    int pomeranians = 3;
    int akitas = 0;
    int vizslas = 0;
    int goldfish = 5;
    int trees = 3;
    int cars = 2;
    int perfumes = 1;

    map<string, int> suesCompounds{{"children", 3},
                                   {"cats", 7},
                                   {"samoyeds", 2},
                                   {"pomeranians", 3},
                                   {"akitas", 0},
                                   {"vizslas", 0},
                                   {"goldfish", 5},
                                   {"trees", 3},
                                   {"cars", 2},
                                   {"perfumes", 1}};
    int sueNumber = 0;

    string line;
    while (getline(file, line))
    {
        vector<pair<string, int>> compounds;

        istringstream iss(line);
        vector<string> list;
        string tmp;
        while (getline(iss, tmp, ' '))
        {
            list.push_back(tmp);
        }
        for (int i = 2; i < list.size(); i = i + 2)
        {
            compounds.push_back({list[i].substr(0, list[i].size() - 1), stoi(list[i + 1])});
        }

        // cout << list[0] << " " << list[1] << endl;
        // for (auto e : compounds)
        // {
        //     cout << "\t" << e.first << " " << e.second << endl;
        // }

        bool sueFlag = true;
        for (auto e : compounds)
        {
            auto idx = suesCompounds.find(e.first);
            if (idx == suesCompounds.end() || idx->second != e.second)
            {
                sueFlag = false;
                break;
            }
        }

        if (sueFlag)
        {
            sueNumber = stoi(list[1]);
            break;
        }
    }

    std::cout << "Part 1:" << std::endl
              << sueNumber << std::endl;

    return 0;
}