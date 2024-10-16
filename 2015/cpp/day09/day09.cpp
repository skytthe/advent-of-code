#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>
#include <algorithm>

int main()
{
    std::ifstream file("2015/inputs/day09.txt");
    if (!file.is_open())
    {
        std::cerr << "Error: Could not open the file." << std::endl;
        return 1;
    }

    std::unordered_map<std::string, int> city_id;
    int cost_graph[10][10] = {0};

    std::string line;
    while (getline(file, line))
    {
        std::stringstream iss(line);
        std::vector<std::string> list;
        std::string tmp;
        while (getline(iss, tmp, ' '))
        {
            list.push_back(tmp);
        }

        std::string city1 = list[0];
        std::string city2 = list[2];
        int cost = std::stoi(list[4]);

        if (city_id.find(city1) == city_id.end())
        {
            city_id[city1] = city_id.size();
        }
        if (city_id.find(city2) == city_id.end())
        {
            city_id[city2] = city_id.size();
        }

        cost_graph[city_id[city1]][city_id[city2]] = cost;
        cost_graph[city_id[city2]][city_id[city1]] = cost;
    }

    // Output city-to-ID mapping
    std::cout << "Contents of unordered_map:\n";
    for (const auto &pair : city_id)
    {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

    // Output the cost graph
    std::cout << "\nCost Graph:\n";
    for (size_t i = 0; i < 10; ++i)
    {
        for (size_t j = 0; j < 10; ++j)
        {
            std::cout << cost_graph[i][j] << " ";
        }
        std::cout << std::endl;
    }

    std::vector<int> range(city_id.size());
    std::iota(range.begin(), range.end(), 0);
    std::sort(range.begin(), range.end());

    std::vector<int> best_route;
    int lowest_cost = INT_MAX;

    std::vector<int> worst_route;
    int highest_cost = 0;

    int sum = 0;
    do
    {
        for (size_t i = 1; i < range.size(); i++)
        {
            sum += cost_graph[range[i]][range[i - 1]];
        }
        if (sum < lowest_cost)
        {
            lowest_cost = sum;
            best_route = range;
        }
        if (sum > highest_cost)
        {
            highest_cost = sum;
            worst_route = range;
        }

        sum = 0;
    } while (std::next_permutation(range.begin(), range.end()));

    std::cout << "Part 1:" << std::endl
              << lowest_cost << std::endl
              << "best route: " << std::endl;
    for (auto c : best_route)
    {
        std::cout << c << ": ";
        for (const auto &pair : city_id)
        {
            if (pair.second == c)
            {
                std::cout << pair.first << std::endl;
                break;
            }
        }
    }

    std::cout << "Part 2:" << std::endl
              << highest_cost << std::endl
              << "worst route: " << std::endl;
    for (auto c : worst_route)
    {
        std::cout << c << ": ";
        for (const auto &pair : city_id)
        {
            if (pair.second == c)
            {
                std::cout << pair.first << std::endl;
                break;
            }
        }
    }

    file.close();
    return 0;
}