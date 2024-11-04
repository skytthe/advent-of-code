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
#include <cctype>

using namespace std;

/*
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
*/

struct player
{
    string name;
    int hitpoints;
    int damage;
    int armor;
};

struct item
{
    string name;
    int price;
    int damage;
    int armor;
};

/*
The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
*/
bool playGame(player p1, player p2, bool printing)
{
    int round = 0;
    while (true)
    {
        round++;
        if (printing)
        {
            cout << "round: " << round << endl;
        }
        int damage_to_p1 = max(1, p2.damage - p1.armor);
        int damage_to_p2 = max(1, p1.damage - p2.armor);
        p1.hitpoints -= damage_to_p1;
        p2.hitpoints -= damage_to_p2;

        if (printing)
        {
            cout << "\tThe player deals " << p1.damage << "-" << p2.armor << " = " << damage_to_p2 << " damage; the boss goes down to " << p2.hitpoints << " hit points." << endl;
        }
        if (p2.hitpoints <= 0)
        {
            return true;
        }
        if (printing)
        {
            cout << "\tThe boss deals " << p2.damage << "-" << p1.armor << " = " << damage_to_p1 << " damage; the boss goes down to " << p1.hitpoints << " hit points." << endl;
        }
        if (p1.hitpoints <= 0)
        {
            return false;
        }
    }
}

int main()
{
    /*
    For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:
    */
    // player you = {"player", 8, 5, 5};
    // player Boss = {"boss", 121, 7, 2};

    // cout << playGame(you, Boss, true) << endl;

    item weapons[] = {
        {"None", 0, 0, 0},
        {"Dagger", 8, 4, 0},
        {"Shortsword", 10, 5, 0},
        {"Warhammer", 25, 6, 0},
        {"Longsword", 40, 7, 0},
        {"Greataxe", 74, 8, 0},
    };
    item armors[] = {
        {"None", 0, 0, 0},
        {"Leather", 13, 0, 1},
        {"Chainmail", 31, 0, 2},
        {"Splintmail", 53, 0, 3},
        {"Bandedmail", 75, 0, 4},
        {"Platemail", 102, 0, 5},
    };
    item rings[] = {
        {"None", 0, 0, 0},
        {"Damage +1", 25, 1, 0},
        {"Damage +2", 50, 2, 0},
        {"Damage +3", 100, 3, 0},
        {"Defense +1", 20, 0, 1},
        {"Defense +2", 40, 0, 2},
        {"Defense +3", 80, 0, 3},
    };

    int boss_hitpoints = 103;
    int boss_damage = 9;
    int boss_armor = 2;
    int player_hitpoints = 100;

    player boss = {"boss", boss_hitpoints, boss_damage, boss_armor};

    int steps = 0;
    int min_cost = INT_MAX;
    for (const auto &w : weapons)
    {
        for (const auto &a : armors)
        {
            for (const auto &r1 : rings)
            {
                for (const auto &r2 : rings)
                {
                    steps++;
                    int damage = w.damage + r1.damage + r2.damage;
                    int armor = a.armor + r1.armor + r2.armor;
                    int cost = w.price + a.price + r1.price + r2.price;
                    player p1 = {"player", player_hitpoints, damage, armor};
                    if (playGame(p1, boss, false) && min_cost > cost)
                    {
                        min_cost = cost;
                    }
                }
            }
        }
    }

    std::cout << "Part 1:" << std::endl
              << min_cost << std::endl;

    return 0;
}