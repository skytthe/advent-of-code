#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <numeric>
#include <algorithm>
#include <climits>
#include <cctype>
#include <cstdint>

using namespace std;

bool isDigit(const std::string &str)
{
    return !str.empty() && std::all_of(str.begin(), str.end(), ::isdigit);
}

std::uint16_t stoui16(const std::string &str)
{
    unsigned long tmp = std::stoul(str);

    if (tmp > std::numeric_limits<std::uint16_t>::max())
    {
        throw std::out_of_range("Value out of range for uint16_t");
    }

    std::uint16_t number = static_cast<std::uint16_t>(tmp);
    return number;
}

int main()
{
    ifstream file("2015/inputs/day07.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    queue<vector<string>> q;
    unordered_map<string, std::uint16_t> signals;

    string line;
    while (getline(file, line))
    {
        istringstream iss(line);
        vector<string> list;
        string tmp;
        while (getline(iss, tmp, ' '))
        {
            list.push_back(tmp);
        }

        if (list.size() == 3 && isDigit(list[0]))
        {
            signals[list[2]] = stoui16(list[0]);
            // cout << list[2] << " : " << list[0] << endl;
        }
        else
        {
            q.push(list);
        }
    }

    signals["1"] = 1;

    // while (!q.empty())
    while (signals.find("a") == signals.end())
    {
        vector<string> tmp = q.front();
        q.pop();
        // cout << q.size() << endl;

        // WIRE
        if (tmp.size() == 3)
        {
            if (signals.find(tmp[0]) != signals.end())
            {
                signals[tmp[2]] = signals[tmp[0]];
            }
            else
            {
                q.push(tmp);
            }
        }
        // NOT
        else if (tmp[0] == "NOT")
        {
            if (signals.find(tmp[1]) != signals.end())
            {
                signals[tmp[3]] = ~signals[tmp[1]];
            }
            else
            {
                q.push(tmp);
            }
        }
        // AND
        else if (tmp[1] == "AND")
        {
            if ((signals.find(tmp[0]) != signals.end()) &&
                (signals.find(tmp[2]) != signals.end()))
            {
                signals[tmp[4]] = signals[tmp[0]] & signals[tmp[2]];
            }
            else
            {
                q.push(tmp);
            }
        }
        // OR
        else if (tmp[1] == "OR")
        {
            if ((signals.find(tmp[0]) != signals.end()) &&
                (signals.find(tmp[2]) != signals.end()))
            {
                signals[tmp[4]] = signals[tmp[0]] | signals[tmp[2]];
            }
            else
            {
                q.push(tmp);
            }
        }
        // LSHIFT
        else if (tmp[1] == "LSHIFT")
        {
            // gz LSHIFT 15 -> hd
            if (signals.find(tmp[0]) != signals.end())
            {
                uint16_t shift = stoui16(tmp[2]);
                signals[tmp[4]] = signals[tmp[0]] << shift;
            }
            else
            {
                q.push(tmp);
            }
        }
        // RSHIFT
        else if (tmp[1] == "RSHIFT")
        {
            // he RSHIFT 3 -> hg
            if (signals.find(tmp[0]) != signals.end())
            {
                uint16_t shift = stoui16(tmp[2]);
                signals[tmp[4]] = signals[tmp[0]] >> shift;
            }
            else
            {
                q.push(tmp);
            }
        }
    }

    // for (const auto &[key, value] : signals)
    // {
    //     std::cout << key << ": " << value << "\n";
    // }

    cout << "Part 1:" << endl
         << signals["a"] << endl;

    return 0;
}