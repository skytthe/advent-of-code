#include <iostream>
#include <fstream>
#include <cctype>

using namespace std;

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
    int sum = 0;
    bool reading_number = false;
    while (file.get(ch))
    {
        if (isdigit(ch) || ch == '-')
        {
            reading_number = true;
            number += ch;
        }
        else if (reading_number)
        {
            sum += stoi(number);
            // cout << number << endl;
            number = "";
            reading_number = false;
        }
    }

    std::cout << "Part 1:" << std::endl
              << sum << std::endl;

    return 0;
}