#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

struct reindeer
{
    string name;
    int speed;
    int fly_time;
    int rest_time;
};

int main()
{
    ifstream file("2015/inputs/day14.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    int duration = 2503;
    vector<reindeer> reindeers;

    string line;
    while (getline(file, line))
    {
        istringstream iss(line);
        vector<string> list;
        string tmp;
        while (getline(iss, tmp, ' '))
        {
            list.push_back(tmp);
        }
        reindeer r = {list[0], stoi(list[3]), stoi(list[6]), stoi(list[13])};
        reindeers.push_back(r);
    }

    // for (auto hans : reindeers)
    // {
    //     cout << "Reindeer Name: " << hans.name << endl;
    //     cout << "Speed: " << hans.speed << " km/h" << endl;
    //     cout << "Fly Time: " << hans.fly_time << " seconds" << endl;
    //     cout << "Rest Time: " << hans.rest_time << " seconds" << endl
    //          << endl;
    // }

    vector<int> travel_distances(reindeers.size());
    int max_travel_distances = 0;
    for (auto r : reindeers)
    {
        int divisor = duration / (r.fly_time + r.rest_time);
        int remainder = duration % (r.fly_time + r.rest_time);

        int travel_distance = r.speed * (divisor * r.fly_time + min(remainder, r.fly_time));
        travel_distances.push_back(travel_distance);

        max_travel_distances = max(max_travel_distances, travel_distance);
    }

    cout << "Part 1:" << endl
         << max_travel_distances << endl;

    return 0;
}