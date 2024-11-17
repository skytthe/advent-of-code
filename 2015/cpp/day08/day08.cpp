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
    ifstream file("2015/inputs/day08.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    int sumMemory = 0;
    int sumCharacters = 0;

    string line;
    while (getline(file, line))
    {
        sumMemory += line.size();

        int count = 0;
        for (int i = 1; i < line.size() - 1; i++)
        {
            count++;
            if (line.at(i) == '\\')
            {
                if (line.at(i + 1) == 'x')
                {
                    i = i + 3;
                }
                else
                {
                    i = i + 1;
                }
            }
        }
        sumCharacters += count;
    }

    int total = sumMemory - sumCharacters;

    std::cout << "Part 1:" << std::endl
              << total << std::endl;

    file.close();
    return 0;
}