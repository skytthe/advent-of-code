#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <CommonCrypto/CommonDigest.h>
#include <string>

using namespace std;

std::string md5(const std::string &data)
{
    unsigned char digest[CC_MD5_DIGEST_LENGTH];

    CC_MD5(data.c_str(), static_cast<CC_LONG>(data.size()), digest);

    ostringstream md5string;
    md5string << std::hex << std::setfill('0');
    for (int i = 0; i < CC_MD5_DIGEST_LENGTH; ++i)
    {
        md5string << std::setw(2) << (int)digest[i];
    }

    return md5string.str();
}

int main()
{
    const std::string input = "ckczppom";

    std::string result1;
    std::string result2;

    string tmp;
    int step = 1;
    int part1 = -1;
    int part2 = -1;
    while (true)
    {
        tmp = input + to_string(step);

        result2 = md5(tmp);

        if (all_of(result2.begin(), result2.begin() + 5, [](char c)
                   { return c == '0'; }))
        {
            if (part1 == -1)
            {
                part1 = step;
                result1 = result2;
            }
            if (result2.at(5) == '0')
            {
                part2 = step;
                break;
            }
        }
        step++;
    }

    cout << "Part 1:" << endl
         << part1 << endl
         << "hash: " << result1 << endl;

    cout << "Part 2:" << endl
         << part2 << endl
         << "hash: " << result2 << endl;

    return 0;
}