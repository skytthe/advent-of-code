#include <iostream>
#include <fstream>
#include <cctype>
#include <vector>

using namespace std;

struct level
{
    int level;
    int number = 0;
    int redFlag = false;
};

int main()
{
    ifstream file("2015/inputs/day12.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    char ch;
    string number;
    int new_number;
    int sum1 = 0;
    bool reading_number = false;

    int levelCounter = 0;
    string red = ":\"red";
    int redPointer = 0;
    bool reading_number_done = false;
    vector<level> levels;
    levels.push_back({0, 0, false});
    while (file.get(ch))
    {
        reading_number_done = false;
        if (isdigit(ch) || ch == '-')
        {
            reading_number = true;
            number += ch;
        }
        else if (reading_number)
        {
            new_number = stoi(number);
            sum1 += new_number;
            // cout << number << endl;
            number = "";
            reading_number = false;
            reading_number_done = true;
        }

        // part 2
        if (ch == red.at(redPointer))
        {
            if (redPointer < 4)
            {
                redPointer++;
            }
            else // red found
            {
                levels[levelCounter].redFlag = true;
                // for (size_t i = 0; i < levelCounter; i++)
                // {
                //     cout << "  ";
                // }
                // cout << "red (" << levelCounter << ")" << endl;
                redPointer = 0;
            }
        }
        else
        {
            redPointer = 0;
        }
        if (reading_number_done)
        {
            levels[levelCounter].number += new_number;
            // for (size_t i = 0; i < levelCounter; i++)
            // {
            //     cout << "  ";
            // }
            // cout << "#" << new_number << endl;
        }

        if (ch == '{')
        {
            levelCounter++;
            levels.push_back({levelCounter, 0, false});

            // for (size_t i = 0; i < levelCounter; i++)
            // {
            //     cout << "  ";
            // }

            // cout << levelCounter << endl;
        }
        else if (ch == '}')
        {
            // for (size_t i = 0; i < levelCounter; i++)
            // {
            //     cout << "  ";
            // }
            // cout << levelCounter << "  " << ((levels[levelCounter].redFlag) ? "true" : "false") << " : " << levels[levelCounter].number << endl;
            // cout << "\t\t" << levels[levelCounter - 1].number;

            if (!levels[levelCounter].redFlag)
            {
                levels[levelCounter - 1].number += levels[levelCounter].number;
            }

            // cout << "  ->  " << levels[levelCounter - 1].number << endl;

            levels.pop_back();
            levelCounter--;
        }
    }

    std::cout << "Part 1:" << std::endl
              << sum1 << std::endl;

    std::cout << "Part 2:" << std::endl
              << levels[0].number << std::endl;

    return 0;
}