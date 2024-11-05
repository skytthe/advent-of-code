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
    ifstream file("2015/inputs/day24.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    vector<int> packages;

    string line;
    while (getline(file, line))
    {
        packages.push_back(stoi(line));
    }

    int sum = accumulate(packages.begin(), packages.end(), 0);
    int group_weight = sum / 3;

    // cout << "sum: " << sum << endl;
    // cout << "group_weight: " << group_weight << endl;

    vector<vector<int>> pset;
    pset.push_back(vector<int>());
    vector<vector<int>> goalset;

    int goalset_lenght = packages.size();
    for (auto e : packages)
    {
        vector<vector<int>> new_subset;
        for (auto set : pset)
        {
            vector<int> tmp;
            tmp = set;
            tmp.push_back(e);
            int a = accumulate(tmp.begin(), tmp.end(), 0);
            if (a <= group_weight && tmp.size() < goalset_lenght)
            {
                new_subset.push_back(tmp);
            }
            if (a == group_weight && tmp.size() <= goalset_lenght)
            {
                if (tmp.size() < goalset_lenght)
                {
                    goalset_lenght = tmp.size();
                    goalset.clear();
                }
                goalset.push_back(tmp);
            }
        }
        pset.insert(pset.end(), new_subset.begin(), new_subset.end());
    }

    long long min_quantum_entanglement = LONG_MAX;
    for (auto set : goalset)
    {
        long long tmp = accumulate(set.begin(), set.end(), 1LL, multiplies<long long>());
        if (tmp < min_quantum_entanglement)
        {
            min_quantum_entanglement = tmp;
        }
    }

    cout << "Part 1:" << endl
         << min_quantum_entanglement << endl;

    return 0;
}