#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

int main()
{
    ifstream file("2015/inputs/day13.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    unordered_map<string, int> id_map;
    int cost_matrix[8][8];

    string line;
    while (getline(file, line))
    {
        vector<string> list;
        istringstream iss(line);
        string tmp;
        while (getline(iss, tmp, ' '))
        {
            list.push_back(tmp);
        }

        string name1 = list[0];
        string name2 = list[10];
        name2.pop_back(); // remove '.'
        int sign = (list[2] == "gain") ? 1 : -1;
        int happiness = sign * stoi(list[3]);

        if (id_map.find(name1) == id_map.end())
        {
            id_map[name1] = id_map.size();
        }
        if (id_map.find(name2) == id_map.end())
        {
            id_map[name2] = id_map.size();
        }

        cost_matrix[id_map[name1]][id_map[name2]] = happiness;
    }

    // circular permutations
    int n = id_map.size();
    vector<int> range(n);
    iota(range.begin(), range.end(), 0);
    vector<int> result(id_map.size());

    int max_happiness = INT_MIN;
    int sum = 0;
    do
    {
        for (int i = 0; i < n; i++)
        {
            sum += cost_matrix[range[i]][range[(i - 1 + n) % n]];
            sum += cost_matrix[range[i]][range[(i + 1) % n]];
        }
        max_happiness = max(sum, max_happiness);
        sum = 0;
    } while (next_permutation(range.begin() + 1, range.end()));

    cout << "Part 1:" << endl
         << max_happiness << endl;

    return 0;
}