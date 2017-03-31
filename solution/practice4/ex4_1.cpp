#include<iostream>
#include<cstring>
#include<string>
#include<vector>

using namespace std;

class Member{
	private:
		string name;
		int age;
		string department;
	public:
		Member(string name, int age, string department);
		//~Member();
		//Destructor is called implicitly when the object is out of the scope it is called, so when finishing one loop, C++ compiler implicitly calls Destructor.
		string getName();
		int getAge();
		string getDept();
		void print();
};

Member::Member(string name, int age, string department):name(name),age(age),department(department){
  cout<<name<<" is "<<age<<" years old."<<endl;
}

string Member::getName(){
  return name;
}

int Member::getAge(){
  return age;
}

string Member::getDept(){
  return department;
}

void Member::print(){
  cout<<name<<" : "<<department<<", "<<age<<" years old."<<endl;
}



int main(){
  vector<Member> m_list;
  string input_name;
  int input_age;
  string input_department;
  bool out=false;
  int i;
  while(!out){
    cin>>input_name>>input_age>>input_department;
    if(input_name=="QUIT"||input_department=="QUIT"||input_age==0){
      out=true;
      continue;
    }
    Member newM(input_name,input_age,input_department);
    m_list.push_back(newM);
  }

  for(i=0;i<m_list.size();i++){
    m_list.at(i).print();//same as m_list[i].print()
  }

}


