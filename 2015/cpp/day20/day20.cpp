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
    // ifstream file("2015/inputs/day20.txt");
    // if (!file.is_open())
    // {
    //     cerr << "Error: Could not open the file." << endl;
    //     return 1;
    // }
    int goal = 33100000;

    int house = 0;
    int presents = 0;

    // while (presents <= goal) // didn't really improve speed
    // {
    //     house++;
    //     presents = (house * (house + 1)) / (2);
    // }

    presents = 0;
    while (presents <= goal)
    {
        house++;
        presents = 0;

        set<int> divisors;
        for (int i = 1; i < sqrt(house); i++)
        {
            if (house % i == 0)
            {
                divisors.insert(i);
                divisors.insert(house / i);
            }
        }

        for (const auto &e : divisors)
        {
            presents += e * 10;
        }

        // cout << "House " << house << " got " << presents << " presents." << endl;
    }

    std::cout << "Part 1:" << std::endl
              << house << std::endl;

    // part 2
    presents = 0;
    house = 0;

    vector<int> visits(1000, 0);
    while (presents <= goal)
    {
        house++;
        presents = 0;
        if (house >= visits.size())
        {
            visits.resize(10 * visits.size(), 0);
        }

        set<int> divisors;
        for (int i = 1; i < sqrt(house); i++)
        {
            if (house % i == 0)
            {
                if (visits[i] < 50)
                {
                    visits[i]++;
                    divisors.insert(i);
                }
                if (visits[house / i] < 50)
                {
                    visits[house / i]++;
                    divisors.insert(house / i);
                }
            }
        }

        for (const auto &e : divisors)
        {
            presents += e * 11;
        }
    }

    std::cout << "Part 2:" << std::endl
              << house << std::endl;

    return 0;
}
