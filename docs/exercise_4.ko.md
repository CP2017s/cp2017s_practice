# Exercise 4

## 1. Constructor, Destructor & Vector

### 1-1. 설명

- 다음과 같은 구성을 지는 Member 클래스를 만들어라

```c++
class Member{
	private:
		string name;
		int age;
		string department;
	public:
		Member(string name, int age, string department);
		//~Member();
		//소멸자는 해당 개체의 scope에서 벗어나는 순간 암묵적으로 호출이 되며, 루프 문 안에서 벗어나는 경우 C++에서는 암묵적으로 소멸자를 부르게 되어 있습니다.
		string getName();
		int getAge();
		string getDept();
		void print();
};
```

- 멤버들의 정보를 입력받고, 객체 생성시 문구가 뜨도록 만들어라
- 멤버들의 정보는 vector를 이용하여 관리하라
- 멤버들의 이름은 서로 같지 않다


### 1-2. 입력 설명

- 입력하고 싶은 갯수 만큼 [이름, 나이, 부서] 순서로 입력을 받는다

- 이름, 나이, 부서를 하나씩 입력 받으면 그 즉시 인스턴스를 만들고 생성하라

- 이름이나 부서에 QUIT이 들어가거나, 나이에 0이 입력되면 입력을 종료한다

- 입력 종료 후에는 vector에서 차례대로 인스턴스의 내용을 print() 함수를 통해 인쇄한 뒤, vector 안에있는 인스턴스들을 소멸시켜라

- 인스턴스는 생성될 때 특정 문구를 인쇄한다.


### 1-3. 예제 입력 및 출력

- 입력 앞에 > 표시를 해두었다 (실제 구현에서는 하지 않는다)


		>Harry 37 Hogwarts
		Harry is 37 years old.
		>Viktor 41 Durmstrang
		Viktor is 41 years old.
		>Fleur 40 Beauxbatons
		Fleur is 40 years old.
		>QUIT 0 QUIT
		Harry : Hogwarts, 37 years old.
		Viktor : Durmstrang, 41 years old.
		Fleur : Beauxbatons, 40 years old.


---

## 2. Inheritance


### 2-1. 설명

- Person클래스를 상속하는 클래스 Student를 만드시오.

```cpp
class Person{
	protected:
		string name;
		int age;
		string gender;//Male or Female
		//상속될때에는 멤버 변수가 private변수로 구현되어 있을 경우 getter함수를 통해서만 가져와야 합니다(어떠한 범위로 상속받더라도 private은 보이지않음)
		//편의를 위하여 protected로 바꾸어서 구현해 보시기 바랍니다(자유)
	public:
		Person(...);
		~Person();
		string getName();
		int getAge();
		string getGender();
		void introduce();
};
```

- void introduce() 함수는 다음처럼 Person 클래스의 인스턴스 내용을 인쇄하는 함수이다(대문자는 변수명)

        NAME is AGE years old, and is GENDER

- Student 클래스는 멤버 변수로 학교 이름을 추가로 담는다

- Student의 void introduce() 함수는 다음처럼 Student 클래스의 인스턴스 내용을 인쇄하는 함수이다

        NAME is AGE years old, and is GENDER
        NAME is studying in SCHOOL



### 2-2. 입력 설명

- 첫 줄에는 입력하고자 하는 사람의 숫자(N)를 입력한다.

- 두번째 줄부터 N개의 줄 동안 사람의 이름,나이,성별을 입력한다.

- 이후 학교에 입학시킬 사람의 숫자(M)를 입력한다.

- 이후 M개의 줄 동안 학교에 입학시킬 사람들의 이름과 학교이름을 입력한다.

- 입력 완료 시, 입력한 사람 또는 학생의 introduce()함수를 수행한다. 순서는 person에 대한 정보를 받은 순서로 출력한다.


### 2-3. 예제 입력

	3
	HyunIl 24 Male
	Byunghoon 24 Male
	Jiwoo 24 Female
	2
	Jiwoo dcslab
	HyunIl dcslab

### 2-4. 예제 출력

	HyunIl is 24 years old, and is Male
	Hyunil is studying in dcslab
	Byunghoon is 24 years old, and is Male
	Jiwoo is 24 years old, and is Female
	Jiwoo is studying in dcslab
