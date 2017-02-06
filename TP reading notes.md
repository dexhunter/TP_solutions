# This is Dex's note of reading _Think Python_

[__Check out my Github__](https://github.com/DexHunter)

## Reading notes:

1. two kinds of programs process high level language into low level language: interpreter & compiler
2. source code -> interpreter -> outputx
3. source code -> compiler -> object code -> executor -> output
4. program: a program is a sequence of instructions that specifies how to perform a computation.
5. script: the contents stored in form of a file
6. value: one of the basic units of data, like a number or string, that a program manipulates.
7. type: a category of values.
8. variable: a name that refers to a value.
9. argument: the expression in parentheses

* question: why display the numbers start with 0 makes it bizarre?

* note: page 20 has many definitions

9. two types of partition table:
	(1)MBR: Master Boot Record
 	(2)GPT: GUID Partition Table
10. flow of execution: the order in which statement are executed
11. Function: a named sequence of statements that performs some useful operation. Functions may or may not take arguments and may or may not produce a result.
12. function definition: a statement that creates a new function, specifying its name, parameters, and the statements it excutes.
13. function object: a value created by a function definition. The name of the function is a variable that refers to a function object.
14. instance: a member of set
15. encapsulation: wrap a piece of code up in a function.
16. generaliztion: add a parameter to a function
17. interface of a function: a summary of how it is used: what are the parameters? What does the function do? And what is the return value? An interface is "clean" if it is "as simple as possible, but not simpler. (Einstein)"
18. A development plan: a process for writing programs.
	(1) Start by writing a small program with no function definitions.
	(2) Once you get the program working, encapsulate it in a function and give it a name.
	(3) Generalize the functionn by adding appropriate parameters.
	(4) Repeat steps 1-3 until you have a set of working functions. Copy and paste working code to aviod retyping( and re-bugging)
	(5) Loot for opportunities to improve the program by refactoring. For example, if you have similar code in several places, consider facotring it into an appropriately general function.

## V. Chapter 5

19. modulus operator: %
20. boolean expressions: either true or false
21. logical operators: and, or, not
22. conditional execution: if
23. alternative execution: else, elif
24. chained conditionals: 2+ branches
25. nested conditionals
26. recursion
27. stack diagram for recursive function.
    (1)n = 0, base case
	(2)
28. infinite recursion
29. keyboard input --> raw_input() 
30. guardian
31. debuging:
			there are three possiblities here:
				(1)There is something wrong with the arguments the function is getting; a precondition is violated.
				(2)There is something wrong with the function; a post condition is violated.
				(3)These is something wrong with the return value or the way it is being used.

## VI. Chapter 6

1. Return Values
2. Incremental Development
3. Composition
4. Boolean Functions
5. More Recursion
6. Leap of Faith
7. Checking Types
8. Debugging

## VII. Chapter 7 Iteration

1. Multiple Assignment: to distinguish between an assignment operation and a statement of equality
2. Updating Variables: (1)increment (2)decrement
3. The while Statement



## Chapter 11 Dictionaries

* key and values -> key-value pair (aka item)
* associative memories
* string and numbers can always be keys!!!
* keys are immutable
* Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key.
* list CANNOT be keys!!!!

# Chapter 12 Tuples

* The _ (undersocre) in python means:

_ has 3 main conventional uses in Python:

[source](http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python)
>
	
	1. To hold the result of the last executed statement in an interactive interpreter session. This precedent was set by the standard CPython interpreter, and other interpreters have followed suit
	
	2. For translation lookup in i18n (imported from the corresponding C conventions, I believe), as in code like: raise
	forms.ValidationError(_("Please enter a correct username"))
	
	3. As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored, as in code like: label, has_label, _ = text.partition(':')
	The latter two purposes can conflict, so it is necessary to avoid using _ as a throwaway variable in any code block that also uses it for i18n translation (many folks prefer a double-underscore, __, as their throwaway variable for exactly this reason).
>
* use 'in' to check whether a value is in the list


## Chapter 13 Case Study: Data Structure Selection

#### What is difference between `return` and `pass` in python? [Souce](http://stackoverflow.com/questions/7872611/in-python-what-is-the-difference-between-pass-and-return)

* `Return` exits the current function or method. `Pass` is a null operation and allows execution to continue at the next statement.

#### Rubber duck debugging

* Sometimes when you ask a question, you find the answer before you finish asking, then you don't need to ask a real person, you can just ask a rubber duck. It's a real thing called rubber duck debugging, you can just see the wikipedia.



## Chapter 14 Files

* persistence: run for a long time (or all the time), keep at least some of data in permanent storage
* trasience: run for a short time, when the program ends, data vanish as well

### Reading and Writing

* If the file already exists, opening it in write mode clears out the old data and starts
fresh, so be careful!

* When the first oprand is a string, % is a format operator
* relative path
* absolute path, starts wtih '/'
* dbm is a module in Python 3! 
* pipe object: an object representing a running program
* What is pickle? pickle is a module implements serializing and de-serializing a Python object structure. "Pickling" is the process whereby a Python object hierarchy is converted into a byte stream, and "unpickling" is the inverse operation

#### The % specifiers that you can use in ANSI C are:

##### Usual variable type Display

* %c char single character

* %d (%i) int signed integer

* %e (%E) float or double exponential format

* %f float or double signed decimal

* %g (%G) float or double use %f or %e as required
 
* %o int unsigned octal value

* %p pointer address stored in pointer

* %s array of char sequence of characters

* %u int unsigned decimal

* %x (%X) int unsigned hex value


## Chapter 15 Classes and Objects

* == operator for object will check the object identity as __is__ operator rather than object equvalence, 


## Chapter 17 Classes and Methods

* Object-oriented: represents relationship between programmer-defined types and functions

## Chapter 18 Inheritance
* veneer: a method or function that provide a different interface to another function without doing much computation

## Chapter 19 The Goodies