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
		~Member();
		string getName();
		int getAge();
		string getDept();
		void print();
};
```

- 멤버들의 정보를 입력받고, 객체 생성,소멸시 문구가 뜨도록 만들어라
- 멤버들의 정보는 vector를 이용하여 관리하라


### 1-2. 입력 설명

- 입력하고 싶은 갯수 만큼 [이름, 나이, 부서] 순서로 입력을 받는다

- 이름, 나이, 부서를 하나씩 입력 받으면 그 즉시 인스턴스를 만들고 생성하라

- 만든 인스턴스는 vector에 담아둔다

- 이름이나 부서에 QUIT이 들어가거나, 나이에 0이 입력되면 입력을 종료한다

- 입력 종료 후에는 vector에서 차례대로 인스턴스의 내용을 print() 함수를 통해 인쇄한 뒤, vector 안에있는 인스턴스들을 소멸시켜라

- 인스턴스는 생성,소멸될 때 특정 문구를 인쇄한다.


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
        Harry is no longer in Hogwarts.
        Viktor is no longer in Durmstrang.
        Fleur is no longer in Beauxbatons.


---

## 2. Inheritance


### 2-1. 설명

- Person클래스를 상속하는 클래스 Student를 만드시오.

```cpp
class Person{
	private:
		string name;
		int age;
		string gender;//Male or Female
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

- 이후 입력한 사람들 중 학교에 입학시킬 사람의 숫자(M)를 입력한다.

- 이후 M개의 줄 동안 학교에 입학시킬 사람들의 이름과 학교이름을 입력한다.

- 입력 완료 시, 입력한 사람의 순서대로 introduce()함수를 실행시킨 후 종료한다.


### 2-3. 예제 입력

        3
        HyunIl 24 Male
        Byunghoon 24 Male
        Jiwoo 24 Female
        2
        Byunghoon dcslab
        Jiwoo dcslab

### 2-4. 예제 출력

        HyunIl is 24 years old, and is Male
        Byunghoon is 24 years old, and is Male
        Byunghoon is studying in dcslab
        Jiwoo is 24 years old, and is Female
        Jiwoo is studying in dcslab


