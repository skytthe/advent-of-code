#include <iostream>
#include <fstream>



bool testPassword(std::string p){
	// std::cout << "input: " << p << std::endl;

	char alphabetSequence = 0;
	for (int i = 0; i < p.size()-2; i++)
	{
		alphabetSequence += (p.at(i) == p.at(i+1)-1) && (p.at(i) == p.at(i+2)-2); 
	}

	char iol= 0;
	for (int i = 0; i < p.size(); i++)
	{
		iol += (p.at(i) == 'i') + (p.at(i) == 'o') + (p.at(i) == 'l'); 
	}
	
	char letterPair = 0;
	bool tmp;
	for (int i = 0; i < p.size()-1; i++)
	{
		tmp =(p.at(i) == p.at(i+1));
		letterPair += tmp;
		i += tmp;
	}

	// std::cout << "alphabetSequence: " << (int)	alphabetSequence << std::endl;
	// std::cout << "iol: " << (int)	iol << std::endl;
	// std::cout << "letterPair " << (int)	letterPair << std::endl << std::endl;

	return (bool)(alphabetSequence && !iol && (letterPair >= 2));
}


int main() {
	// std::ifstream file("2015/inputs/day11.txt");
	// if(!file.is_open()) {
    //     	std::cerr << "Error: Could not open the file." << std::endl;
    //     	return 1;
	// }
	
	// std::string input = "abcdefgh";
	// std::string input = "ghijklmn";
	std::string input = "hepxcrrq";

	std::string newPassword;
	newPassword = input;

	while (!testPassword(newPassword))
	{
		char carry = 1;
		for (int i = newPassword.size()-1; (i >= 0 && carry == 1); i--)
		{
			char c = newPassword.at(i);
			c = (c - 'a' + carry)%26 + 'a';
			carry = (c == 'a');
			newPassword[i] = c;
		}
	}

    std::cout << "Part 1:" << std::endl
              << newPassword << std::endl;

	return 0;
}
