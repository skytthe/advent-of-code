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

void nestedLoop(vector<ingredient> ingredients, int max, vector<int> &indices, int idx, long &best)
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
            for (int i = 0; i < ingredients.size(); i++)
            {
                capacity += indices[i] * ingredients[i].capacity;
                durability += indices[i] * ingredients[i].durability;
                flavor += indices[i] * ingredients[i].flavor;
                texture += indices[i] * ingredients[i].texture;
            }
            long tmp = (capacity < 0 || durability < 0 || flavor < 0 || texture < 0) ? 0 : capacity * durability * flavor * texture;

            if (tmp > best)
            {
                best = tmp;
            }
        }
        return;
    }
    else
    {
        for (int i = 0; i < max; i++)
        {
            indices[idx] = i;
            nestedLoop(ingredients, max, indices, idx + 1, best);
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
        ingredient ingr = {list[0], stoi(list[2]), stoi(list[4]),
                           stoi(list[6]), stoi(list[8]), stoi(list[10])};
        ingredients.push_back(ingr);
    }

    // printIngredients(ingredients);

#define TEASPOONS 100
    long best = 0;
    vector<int> indices(ingredients.size());
    nestedLoop(ingredients, TEASPOONS, indices, 0, best);

    std::cout << "Part 1:" << std::endl
              << best << std::endl;

    return 0;
}
