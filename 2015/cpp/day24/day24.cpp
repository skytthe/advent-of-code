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
    int group_weight1 = sum / 3;
    int group_weight2 = sum / 4;

    // cout << "sum: " << sum << endl;
    // cout << "group_weight: " << group_weight << endl;

    vector<vector<int>> pset;
    pset.push_back(vector<int>());
    vector<vector<int>> goalset1;
    vector<vector<int>> goalset2;

    int goalset_lenght1 = packages.size();
    int goalset_lenght2 = packages.size();
    for (auto e : packages)
    {
        vector<vector<int>> new_subset;
        for (auto set : pset)
        {
            vector<int> tmp;
            tmp = set;
            tmp.push_back(e);
            int a = accumulate(tmp.begin(), tmp.end(), 0);
            if (a <= group_weight2 && tmp.size() < goalset_lenght2)
            {
                new_subset.push_back(tmp);
            }
            else if (a <= group_weight1 && tmp.size() < goalset_lenght1)
            {
                new_subset.push_back(tmp);
            }

            if (a == group_weight1 && tmp.size() <= goalset_lenght1)
            {
                if (tmp.size() < goalset_lenght1)
                {
                    goalset_lenght1 = tmp.size();
                    goalset1.clear();
                }
                goalset1.push_back(tmp);
            }
            if (a == group_weight2 && tmp.size() <= goalset_lenght2)
            {
                if (tmp.size() < goalset_lenght2)
                {
                    goalset_lenght2 = tmp.size();
                    goalset2.clear();
                }
                goalset2.push_back(tmp);
            }
        }
        pset.insert(pset.end(), new_subset.begin(), new_subset.end());
    }

    long long min_quantum_entanglement1 = LONG_MAX;
    for (auto set : goalset1)
    {
        long long tmp = accumulate(set.begin(), set.end(), 1LL, multiplies<long long>());
        if (tmp < min_quantum_entanglement1)
        {
            min_quantum_entanglement1 = tmp;
        }
    }
    cout << "Part 1:" << endl
         << min_quantum_entanglement1 << endl;

    long long min_quantum_entanglement2 = LONG_MAX;
    for (auto set : goalset2)
    {
        long long tmp = accumulate(set.begin(), set.end(), 1LL, multiplies<long long>());
        if (tmp < min_quantum_entanglement2)
        {
            min_quantum_entanglement2 = tmp;
        }
    }
    cout << "Part 2:" << endl
         << min_quantum_entanglement2 << endl;

    return 0;
}