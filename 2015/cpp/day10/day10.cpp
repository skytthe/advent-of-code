#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>
#include <algorithm>

std::string look_and_say(std::string input)
{
    std::string res;
    for (int i = 0; i < input.size(); i++)
    {
        char c = input.at(i);
        int count = 1;
        while ((i + 1) < input.size() && input.at(i + 1) == c)
        {
            count++;
            i++;
        }
        res += std::to_string(count) + c;
        // std::cout << c << ": " << count << std::endl;
    }

    return res;
}

int main()
{
    // std::string input = "1";
    std::string input = "3113322113";
    // int steps = 5;
    int steps = 40;

    std::string result = input;

    for (int i = 0; i < steps; i++)
    {
        result = look_and_say(result);
        // std::cout << "step: " << i << std::endl
        //           << "\t" << result << std::endl
        //           << "\tlen(" << result.size() << ")" << std::endl;
    }

    std::cout << "Part 1:" << std::endl
              << result.size() << std::endl;

    return 0;
}