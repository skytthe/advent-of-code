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

enum instructionSet
{
    hlf,
    tpl,
    inc,
    jmp,
    jie,
    jio
};

instructionSet getInstruction(string s)
{
    static const map<string, instructionSet> instructionSetMap({{"hlf", hlf},
                                                                {"tpl", tpl},
                                                                {"inc", inc},
                                                                {"jmp", jmp},
                                                                {"jie", jie},
                                                                {"jio", jio}});
    auto idx = instructionSetMap.find(s);
    return idx->second;
}

std::string getInstructionString(instructionSet instruction)
{
    switch (instruction)
    {
    case hlf:
        return "hlf";
    case tpl:
        return "tpl";
    case inc:
        return "inc";
    case jmp:
        return "jmp";
    case jie:
        return "jie";
    case jio:
        return "jio";
    default:
        return "unknown"; // Return "unknown" if the instruction is not recognized
    }
}

struct instruction
{
    instructionSet instr;
    unsigned int *reg;
    int offset;
};

int main()
{
    ifstream file("2015/inputs/day23.txt");
    if (!file.is_open())
    {
        cerr << "Error: Could not open the file." << endl;
        return 1;
    }

    vector<instruction> program;
    unsigned int programCounter = 0;
    unsigned int a = 0;
    unsigned int b = 0;

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

        instruction inst = {getInstruction(list[0]), nullptr, 0};
        switch (inst.instr)
        {
        case hlf:
        case tpl:
        case inc:
            if (list[1].at(0) == 'a')
            {
                inst.reg = &a;
            }
            if (list[1].at(0) == 'b')
            {
                inst.reg = &b;
            }
            break;
        case jie:
        case jio:
            if (list[1].at(0) == 'a')
            {
                inst.reg = &a;
            }
            if (list[1].at(0) == 'b')
            {
                inst.reg = &b;
            }
            inst.offset = stoi(list[2]);
            break;
        case jmp:
            inst.offset = stoi(list[1]);
            break;
        default:
            break;
        }

        program.push_back(inst);
    }

    // for (int i = 0; i < program.size(); i++)
    // {
    //     cout << "line:  " << i << endl
    //          << "\t";
    //     cout << getInstructionString(program[i].instr) << endl
    //          << "\t" << program[i].reg << endl
    //          << "\t" << program[i].offset << endl;
    // }

    int step = 0;
    while (programCounter < program.size())
    {
        // step++;
        // cout << "step> " << step << endl;
        // cout << "  programCounter " << programCounter << endl;
        // cout << "  a " << a << endl;
        // cout << "  b " << b << endl;
        // cout << "  " << getInstructionString(program[programCounter].instr) << endl;
        switch (program[programCounter].instr)
        {
        case hlf:
            (*program[programCounter].reg) = (*program[programCounter].reg) / 2;
            programCounter++;
            break;
        case tpl:
            (*program[programCounter].reg) = (*program[programCounter].reg) * 3;
            programCounter++;
            break;
        case inc:
            (*program[programCounter].reg)++;
            programCounter++;
            break;
        case jmp:
            programCounter += program[programCounter].offset;
            break;
        case jie:
            if ((*program[programCounter].reg) % 2 == 0)
            {
                programCounter += program[programCounter].offset;
            }
            else
            {
                programCounter++;
            }
            break;
        case jio:
            if ((*program[programCounter].reg) == 1)
            {
                programCounter += program[programCounter].offset;
            }
            else
            {
                programCounter++;
            }
            break;
        default:
            break;
        }
    }
    // cout << endl
    //      << "DONE:" << endl;
    // cout << "step> " << step << endl;
    // cout << "  programCounter " << programCounter << endl;
    // cout << "  a " << a << endl;
    // cout << "  b " << b << endl;

    std::cout << "Part 1:" << std::endl
              << b << std::endl;

    file.close();
    return 0;
}