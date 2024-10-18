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
    int point;
    int distance;
};

ostream &operator<<(ostream &os, const reindeer &r)
{
    os << "Reindeer Name: " << r.name << endl;
    os << "   Speed: " << r.speed << " km/h" << endl;
    os << "   Fly Time: " << r.fly_time << " seconds" << endl;
    os << "   Rest Time: " << r.rest_time << " seconds" << endl;
    os << "   Points: " << r.point << endl;
    os << "   Distance: " << r.distance << " km" << endl;
    return os;
}

int main()
{
    ifstream file("2015/inputs/day14.txt");

    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    int duration = 2503;
    //    duration = 1000;
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
        reindeer r = {list[0], stoi(list[3]), stoi(list[6]), stoi(list[13]), 0, 0};
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
    for (auto &r : reindeers)
    {
        int divisor = duration / (r.fly_time + r.rest_time);
        int remainder = duration % (r.fly_time + r.rest_time);

        int travel_distance = r.speed * (divisor * r.fly_time + min(remainder, r.fly_time));
        travel_distances.push_back(travel_distance);

        max_travel_distances = max(max_travel_distances, travel_distance);
    }

    cout << "Part 1:" << endl
         << max_travel_distances << endl;

    // PART 2
    int itr_max_distance = 0;
    for (int i = 1; i <= duration; i++)
    {
        // cout << "-----------------" << endl;
        // cout << "-----------------" << endl;
        // cout << "step: " << i << endl;
        // cout << "-----------------" << endl;
        for (auto &r : reindeers)
        {
            int remainder = i % (r.fly_time + r.rest_time);
            r.distance += (remainder != 0 && remainder <= r.fly_time) ? r.speed : 0;
            itr_max_distance = max(itr_max_distance, r.distance);
        }
        // cout << endl;
        // cout << itr_max_distance << endl;
        // cout << "-----------------" << endl;
        for (auto &r : reindeers)
        {
            if (r.distance == itr_max_distance)
            {
                r.point++;
            }
            // cout << r << endl;
        }
        itr_max_distance = 0;
    }

    int max_point = -1;
    for (auto &r : reindeers)
    {
        //        cout << r << endl;
        max_point = max(max_point, r.point);
    }
    cout << "Part 2:" << endl
         << max_point << endl;

    return 0;
}