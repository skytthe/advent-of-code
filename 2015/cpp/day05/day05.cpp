#include <iostream>
#include <fstream>
#include <set>
#include <string>

using namespace std;

int main()
{
    ifstream file("2015/inputs/day05.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    string line;

    int nice_string_count = 0;

    set<char> vowels{'a', 'e', 'i', 'o', 'u'};
    int vowel_count = 0;
    bool is_double_letter = false;
    set<string> bad_strings{"ab", "cd", "pq", "xy"};
    bool is_bad_string = false;

    while (getline(file, line))
    {
        if (vowels.count(line.at(0)))
        {
            vowel_count++;
        }
        for (int i = 1; i < line.size(); i++)
        {
            if (vowels.count(line.at(i)))
            {
                vowel_count++;
            }
            if (line.at(i - 1) == line.at(i))
            {
                is_double_letter = true;
            }
            if (bad_strings.count(string(1, line.at(i - 1)) + line.at(i)))
            {
                is_bad_string = true;
            }
        }

        if (vowel_count >= 3 && is_double_letter && !is_bad_string)
        {
            nice_string_count++;
        }

        vowel_count = 0;
        is_double_letter = false;
        is_bad_string = false;
    }

    cout << "Part 1:" << endl
         << nice_string_count << endl;

    return 0;
}