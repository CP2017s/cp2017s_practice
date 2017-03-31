#include <iostream>

using namespace std;

class Book {
private:
	int price;
	string name;

public:
	void setPrice(const int price);
	
	void setName(const string name);
	
	string getName() const;
	
	int getPrice() const;
};


void Book::setName(const string name) {
	this->name = name;
}

void Book::setPrice(const int price) {
	this->price = price;
}

string Book::getName() const {
	return this->name;
}

int Book::getPrice() const {
	return this->price;
}


int main() {
	int n;
	cin >> n;
	
	Book books[n];
	string tmpName;
	int tmpPrice;
	
	for (Book &book : books) {
		cin >> tmpName >> tmpPrice;
		
		book.setName(tmpName);
		book.setPrice(tmpPrice);
	}
	
	for (Book book:books) {
		cout << book.getName() << endl;
	}
	
	for (Book book:books) {
		cout << book.getPrice() << endl;
	}
}