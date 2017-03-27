# HW1

**You do not have to think about any Exception Cases.**

## 1. Phone Book

### 1-1. 설명

- Always show prompt `CP-2017-12345>`(your student ID) at first and at the end of each task.
- If user inputs enter, show information about choices.
- If user inputs `exit`, end the program.

### 1-2. 예제 입력

	
	
### 1-3. 예제 출력

	Phone Book
	1. Add person
	2. Remove person
	3. Print phone book
	
---	
## 2. Add person

### 2-1. 설명

- User can add person from Add person menu.
- Each person stores his/her first, last name and phone number.
- There must be a space between the first and last names.
- User inputs only `02-xxxx-xxxx` or `010-xxxx-xxxx` as phone number.
- Person who is categorized in Work stores his/her team.
- Person who is categorized in Family stores his/her birthday.
- User inputs only `YYMMDD` as birthday.
- Person who is categorized in Friend stores his/her age.
- After the task is done, print `Successfully added new person`.

### 2-2. 예제 입력

	1
	
### 2-3. 예제 출력

	Select Type
	1. Person
	2. Work
	3. Family
	4. Friend
	
---
## 3. Remove person

### 3-1. 설명

- User removes information of person from Remove person menu.

### 3-2. 예제 입력

	2
	
### 3-3. 예제 출력

	Enter Index of person: 
       
### 3-4. 예제 입력

	10
	
### 3-5. 예제 출력

- If the index is available
	
		A person is successfully deleted from the Phone Book!
        
- If not

		Person does not exist!
               
---
## 4. Remove person

### 4-1. 설명

- User can print all the stored people and their information from Remove person menu.

### 4-2. 예제 입력

	3
	
### 4-3. 예제 출력

	Phone Book Print
	1. John doe_010-1234-5678_Warriors
	2. Stephen Curry_02-1234-5678_940101_261
       
