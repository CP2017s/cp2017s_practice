# HW1

**You do not need to consider exceptions that are not mentioned in this document.**

**You have to print exactly same as sample outputs.**

## 1. Phone Book

### 1-1. constraints

- Always show prompt `CP-2017-12345>`(your student ID) before each task.
- In the initial state, when the user inputs empty line(just `\n`), it shows information about choices.
- In the initial state, when the user inputs `exit`, end the program.
- When each menu is finished, it returns to the initial state to wait another input of the user.

### 1-2. sample input

	
	
### 1-3. sample output

	Phone Book
	1. Add person
	2. Remove person
	3. Print phone book
	
---

## 2. Add person

### 2-1. constraints

- User can add person from the `Add person` menu.
- In the initial state, when the user inputs `1`, it enters the `Add person` menu and shows information about choices.


- Each person stores his/her first, last name and phone number.
- There must be a space between the first and last names.
- User inputs only `02-xxxx-xxxx` or `010-xxxx-xxxx` format as phone number.
- Person who is categorized in `Work` stores his/her team.
- Person who is categorized in `Family` stores his/her birthday.
- User inputs only `YYMMDD` format as birthday.
- Person who is categorized in `Friend` stores his/her age.
- After the task is done, print `Successfully added new person`.

### 2-2. sample input

	1
	
### 2-3. sample output

	Select Type
	1. Person
	2. Work
	3. Family
	4. Friend
	
---

## 3. Remove person

### 3-1. constraints

- User removes information of person from the `Remove person` menu.
- In the initial state, when the user inputs `2`, it enters the `Remove person` menu and asks index of person to remove.


- example of index policy
	- In the phone book with only one person, if user remove a person whose index is `0` and adds another person, the index of new person becomes `0`.

### 3-2. sample input

	2
	
### 3-3. sample output

	Enter Index of person: 
       
### 3-4. sample input

	10
	
### 3-5. sample output

- If the index is available
	
		A person is successfully deleted from the Phone Book!
        
- If not

		Person does not exist!
               
---

## 4. Print person

### 4-1. constraints

- User can print all the stored people and their information.
- In the initial state, when the user inputs `3`, it prints information of all persons.


- People who have been removed should not print.
- Output format is
	- `Person` class
	
		`{first name} {last name}_{phone number}`
		
	- `Work`, `Friend`

		`{first name} {last name}_{phone number}_{an addtional attribute}`
		
	- `Family`

		`{first name} {last name}_{phone number}_{birthday}_{D-day}`
			
		

### 4-2. sample input

	3
	
### 4-3. sample output

	Phone Book Print
	1. John doe_010-1234-5678_Warriors
	2. Stephen Curry_02-1234-5678_940101_261
	.
	.