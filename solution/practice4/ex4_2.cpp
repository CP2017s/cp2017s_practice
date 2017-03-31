#include<iostream>
#include<cstdio>
#include<string>
#include<vector>


using namespace std;

class Person{
	private:
		string name;
		int age;
		string gender;//Male or Female
	public:
		Person(string name, int age, string gender);
		~Person();
		string getName();
		int getAge();
		string getGender();
		void introduce();
};


class Student : public Person{
  private:
    string school;
  public:
    Student(string name, int age, string gender,string school);
    void introduce();
};


Person::Person(string name,int age, string gender):name(name),age(age),gender(gender){

}

Person::~Person(){
}


Student::Student(string name, int age, string gender,string school):Person(name,age,gender){
  Student::school=school;
}

string Person::getName(){
  return name;
}

string Person::getGender(){
  return gender;

}

int Person::getAge(){
  return age;
}

void Person::introduce(){
  cout<<name<<" is "<<age<<" years old, and is "<<gender<<endl;
}

void Student::introduce(){
  Person::introduce();
  cout<<getName()<<" is studying in "<<school<<endl;
}

int main(){

  vector<Person> p_list;
  vector<Student> s_list;
  vector<int> index_save;

  string name;
  int age;
  string gender;
  string school;

  int person_count;
  int student_count;
  int i,j;
  cin>>person_count;
  for(i=0;i<person_count;i++){
    cin>>name>>age>>gender;
    Person newP(name,age,gender);
    p_list.push_back(newP);

    index_save.push_back(-1);
  }

  cin>>student_count;
  for(i=0;i<student_count;i++){
    cin>>name>>school;
    for(j=0;j<p_list.size();j++){
      if(p_list.at(j).getName()==name){
        Student newS(name,p_list.at(j).getAge(),p_list.at(j).getGender(),school);
        s_list.push_back(newS);
        index_save.at(j)=i;
      }
    }
  }

  for(i=0;i<person_count;i++){
    if(index_save.at(i)==-1)
      p_list.at(i).introduce();
    else
      s_list.at(index_save.at(i)).introduce();
  }

  return 0;
}


