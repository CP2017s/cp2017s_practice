#include <iostream>

using namespace std;

class Vending {
private:
	int price;
	int count;
public:
	int coffee(int money);
	
	void setPrice(const int price);
	
	void setCount(const int count);
};

int Vending::coffee(int money) {
	int val = money / price;
	
	if (val > count) {
		int tmpCount = count;
		count = 0;
		return tmpCount;
	}
	else {
		count -= val;
		return val;
	}
}

void Vending::setPrice(const int price) {
	this->price = price;
}

void Vending::setCount(const int count) {
	this->count = count;
}


int main() {
	int price, count;
	cin >> price >> count;
	
	Vending vending;
	vending.setPrice(price);
	vending.setCount(count);
	
	int money;
	cin >> money;
	
	cout << vending.coffee(money);
}