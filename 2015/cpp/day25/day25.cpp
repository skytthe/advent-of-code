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
#include <cfloat>
#include <cctype>

using namespace std;

long getGridValue(int row, int col)
{
    int start_value = 1 + (row * (row - 1)) / 2;
    long value = start_value + (col - 1) * row + ((col) * (col - 1)) / 2;
    return value;
}

int main()
{
    int row = 2978;
    int column = 3083;

    long itr = getGridValue(row, column) - 1;

    long init = 20151125L;
    long mult = 252533L;
    long div = 33554393L;

    long tmp = init;
    for (int i = 0; i < itr; i++)
    {
        tmp = (tmp * mult) % div;
    }

    cout << "Part 1:" << endl
         << tmp << endl;

    return 0;
}
