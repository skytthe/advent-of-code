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

    int nice_string_count1 = 0;
    int nice_string_count2 = 0;

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
            nice_string_count1++;
        }

        vowel_count = 0;
        is_double_letter = false;
        is_bad_string = false;

        // part 2
        set<string> letter_pairs;
        bool is_letter_pair_rule = false;
        bool is_repeat_rule = false;

        for (int i = 2; i < line.size(); i++)
        {

            if (letter_pairs.count(string(1, line.at(i - 1)) + line.at(i)))
            {
                is_letter_pair_rule = true;
            }
            letter_pairs.insert(string(1, line.at(i - 2)) + line.at(i - 1));
            if (line.at(i - 2) == line.at(i))
            {
                is_repeat_rule = true;
            }
        }
        if (is_letter_pair_rule && is_repeat_rule)
        {
            nice_string_count2++;
        }
    }

    cout << "Part 1:" << endl
         << nice_string_count1 << endl;

    cout << "Part 2:" << endl
         << nice_string_count2 << endl;

    return 0;
}