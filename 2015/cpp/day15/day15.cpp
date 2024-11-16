#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct ingredient
{
    string name;
    long capacity;
    long durability;
    long flavor;
    long texture;
    long calories;
};

void printIngredients(const vector<ingredient> &ingredients)
{
    cout << "Ingredients:\n";
    for (const auto &ing : ingredients)
    {
        cout << "Name: " << ing.name << '\n'
             << "Capacity: " << ing.capacity << '\n'
             << "Durability: " << ing.durability << '\n'
             << "Flavor: " << ing.flavor << '\n'
             << "Texture: " << ing.texture << '\n'
             << "Calories: " << ing.calories << "\n\n";
    }
}

void nestedLoop(vector<ingredient> ingredients, int max, vector<int> &indices, int idx, long &best1, long &best2)
{
    if (idx == ingredients.size())
    {
        int sum = accumulate(indices.begin(), indices.end(), 0);
        if (sum == max)
        {
            long capacity = 0;
            long durability = 0;
            long flavor = 0;
            long texture = 0;
            long calories = 0;
            for (int i = 0; i < ingredients.size(); i++)
            {
                capacity += indices[i] * ingredients[i].capacity;
                durability += indices[i] * ingredients[i].durability;
                flavor += indices[i] * ingredients[i].flavor;
                texture += indices[i] * ingredients[i].texture;
                calories += indices[i] * ingredients[i].calories;
            }
            long tmp = (capacity < 0 || durability < 0 || flavor < 0 || texture < 0)
                           ? 0
                           : capacity * durability * flavor * texture;

            if (tmp > best1)
            {
                best1 = tmp;
            }
            if (calories == 500 & tmp > best2)
            {
                best2 = tmp;
            }
        }
        return;
    }
    else
    {
        for (int i = 0; i < max; i++)
        {
            indices[idx] = i;
            nestedLoop(ingredients, max, indices, idx + 1, best1, best2);
        }
    }
}

int main()
{

    std::ifstream file("2015/inputs/day15.txt");
    if (!file.is_open())
    {
        std::cerr << "Error: Could not open the file." << std::endl;
        return 1;
    }

    vector<ingredient> ingredients;

    string line;
    while (getline(file, line))
    {
        stringstream iss(line);
        vector<string> list;
        string tmp;
        while (getline(iss, tmp, ' '))
        {
            list.push_back(tmp);
        }
        ingredients.push_back({list[0], stoi(list[2]), stoi(list[4]),
                               stoi(list[6]), stoi(list[8]), stoi(list[10])});
    }

    // printIngredients(ingredients);

#define TEASPOONS 100
    long best1 = 0;
    long best2 = 0;
    vector<int> indices(ingredients.size());
    nestedLoop(ingredients, TEASPOONS, indices, 0, best1, best2);

    std::cout << "Part 1:" << std::endl
              << best1 << std::endl;

    std::cout << "Part 2:" << std::endl
              << best2 << std::endl;

    return 0;
}
