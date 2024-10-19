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

        cost_matrix[id_map[name1]][id_map[name2]];
    }

    // TODO: circular permutations

    return 0;
}