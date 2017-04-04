# Exercise 5

## 1. Simple Calculator

### 1-1. Description

- Create a simple calculator that reads 2 numbers and operator.

- Your program should have a class 'Unit' as follows

'''java
class Unit{
  private int left;
  private int right;
  private char type;
  private int result;
  Unit(int left, int right,char type){
    //TODO
  }

  void calculate(){
    //TODO
  }
  String toString(){
    //TODO
  }
}
'''

- int left contains the first number you entered

- int right contains the second number you entered

- char type contains operator you entered

- int result contains the result of calculation

- toString() function expresses the calculation in an equation.

- You may decide access range of each functions, but the variable must be private.



### 1-2. Input & Output Example

2 4 +
2+4=6
3 5 *
3*5=15
6 4 /
6/4=1
16 5 %
16%5=1
3 10 -
3-10=-7
QUIT





---

## 2. Advanced Calculator

### 2-1. Description

- Create an advanced calculator with class 'Unit_Advanced', which inherits class 'Unit'.

- Class 'Unit_Advanced' will now read 1 token for deciding instance to compare or calculate, 2 numbers, and operator/inequality sign.

- Class 'Unit_Advanced' can compare two numbers based on inequality sign you entered, and save boolean value about inequality.

- Class 'Unit_Advanced' has additional member variable : boolean isCmp, boolean cmp_result, String cmp

- boolean isCmp shows whether this instance is about inequality or equation

- boolean cmp_result shows whether inequality is true/false

- String cmp shows which inequality sign you entered

- Class 'Unit_Advaned' has additional member function : void compare()

- void compare() compares 2 numbers with inequality sign you entered, and save result(boolean) in cmp_result

- Also, Class 'Unit_Advanced' can now calculate a^b, a<<b(represenetd as a<b), a>b(represented as a>b), a&b, a|b. 

- toString function express the instance to an inequality expression or an equation.


### 2-2. Input & Output Example

cal 2 4 +
2+4=6
cmp 2 4 <=
2<=4 : true
cmp 2 5 !=
2!=5 : true
cmp 2 4 ==
2==4 : false
cmp -10 > 5
-10>5 : false
cal 3 6 ^
3^6=729
cal 1 1 &
1&1=1
cal 2 1 |
2|1=3
cal 16 2 >
16>2=4
cal 8 2 <<
8<2=32
QUIT

---

## 3. Advanced Calculator with Memory

### 3-1. Description

- Your Advanced Calculate can now memorize all inputs you entered.

- When you enter "list", your program should print out all equation/inequality you have entered.


### 3-2. Input & Output Example


cal 2 4 +
2+4=6
cal 3 5 *
3*5=15
cal 6 4 /
6/4=1
cal 16 5 %
16%5=1
cal 3 10 -
3-10=-7
cal 2 4 +
2+4=6
cmp 2 4 <=
2<=4 : true
cmp 2 5 !=
2!=5 : true
cmp 2 4 ==
2==4 : false
cmp -10 > 5
-10>5 : false
cal 3 6 ^
3^6=729
cal 1 1 &
1&1=1
cal 2 1 |
2|1=3
cal 16 2 >>
16>>2=4
cal 8 2 <<
8<<2=32
list
2+4=6
3*5=15
6/4=1
16%5=1
3-10=-7
2+4=6
2<=4 : true
2!=5 : true
2==4 : false
-10>5 : false
3^6=729
1&1=1
2|1=3
16>>2=4
8<<2=32
QUIT
