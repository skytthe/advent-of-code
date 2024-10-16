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

    std::string result;

    string tmp;
    int step = 1;
    while (true)
    {
        tmp = input + to_string(step);

        result = md5(tmp);

        if (all_of(result.begin(), result.begin() + 5, [](char c)
                   { return c == '0'; }))
        {
            break;
        }
        step++;
    }

    cout << "Part 1:" << endl
         << step << endl
         << "hash: " << result << endl;

    return 0;
}