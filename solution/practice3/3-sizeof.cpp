#include <iostream>

using namespace std;

enum season { SPRING, SUMMER, FALL, WINTER };

class Student {
public:
	int id;
	int age;
};

int main() {
	season s = SPRING;
	Student student;
	
	cout << sizeof(long double) << endl;
	cout << sizeof(double) << endl;
	cout << sizeof(float) << endl;
	cout << sizeof(unsigned long int) << endl;
	cout << sizeof(long int) << endl;
	cout << sizeof(unsigned int) << endl;
	cout << sizeof(int) << endl;
	cout << sizeof(unsigned short int) << endl;
	cout << sizeof(short int) << endl;
	cout << sizeof(unsigned char) << endl;
	cout << sizeof(char) << endl;
	cout << sizeof(bool) << endl;
	cout << sizeof(s) << endl;
	cout << sizeof(student) << endl;
}