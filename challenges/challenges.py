
# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
from math import sqrt
import re

'''
Question 1:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def func1(num1, num2):
	num_list = []
	for i in xrange(num1, num2+1):
		if i%7 == 0 and i%5 != 0:
			num_list.append(str(i))
	print(', '.join(num_list))


'''
Question 2:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320
'''
def fact(num):
	if num < 0:
		return -1

	if num < 2:
		return 1

	# n! = n * (n-1)!
	return (num * fact(num-1))

def func2(num):
	print "%d! is %d" % (num, fact(num))


'''
Question 3:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such
that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
def func3(num):
	d = dict()
	for i in xrange(1, num+1):
		d[i] = i*i
	print d



'''
Question 4
Level 1

Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
'''
def func4():
	inputs = raw_input("Enter comma-separated numbers->")
	_l = inputs.split(',')
	_t = tuple(_l)
	print _l
	print _t


'''
Question 5
Level 1

Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class Foo5(object):
	def __init__(self):
		self.str = ""

	def getString(self):
		self.str = raw_input("Enter String->")

	def printString(self):
		print self.str.upper()

def func5():
	item = Foo5()
	item.getString()
	item.printString()


'''
Question 6
Level 2

Question:
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24
'''
def func6():
	C, H = 50, 30
	msg = raw_input("Enter comma-separated numbers ->")
	D = map(int, msg.split(','))

	results = [ int(sqrt(2*C*d/H)) for d in D ]
	print ','.join(map(str, results))



'''
Question 7
Level 2

Question:
Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1,X-1; j=0,1,Y-1
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
'''
def func7():
	msg = raw_input("Enter 2 comma-separated digits X,Y ->")
	X,Y = map(int, msg.split(','))

	# NOTE: Initializing a 2D list
	results = [ [x*y for y in xrange(Y)] for x in xrange(X) ]
	print results

	'''
	# Lame way of solving this problem
	results = []
	for i in xrange(X):
		res = []
		for j in xrange(Y):
			res.append(i*j)
		results.append(res)
	print results
	'''


'''
Question 8
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a
comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''
def func8():
	msg = raw_input("Enter comma-separated words ->")
	results = msg.split(',')
	results.sort()
	print ','.join(results)


'''
Question 9
Level 2

Question
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT
'''
def func9():
	msg = raw_input("Enter comma-separated words ->")
	results = msg.split(',')
	results = [ word.capitalize() for word in results ]
	print ','.join(results)

'''
Question 10
Level 2

Question:
Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''
def func10():
	msg = raw_input("Enter whitespace-separated words ->")
	words = msg.split()
	words = list(set(words)) # Removes duplicates
	words.sort()
	print ' '.join(words)

'''
Question 11
Level 2

Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''
def func11():
	msg = raw_input("Enter comma-separated binary numbers ->")
	nums = msg.split(',')

	# NOTE: int(n, 2 ) converts base 2 input to integer
	results = [ n for n in nums if not int(n, 2)%5 ]
	'''
	results = []
	for item in nums:
		int_item = int(item, 2)
		if not int_item % 5:
			results.append(item)
	'''
	print ','.join(results)

'''
Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def is_all_even_digits(num):
	for d in str(num):
		if int(d)%2:
			return False
	return True

def func12():
	results = [ i  for i in xrange(1000, 3001) if is_all_even_digits(i) ]
	print ','.join(map(str, results))

'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''
def func13():
	msg = raw_input("Enter a string ->")
	num_of_alpha = 0
	num_of_digits = 0
	for c in msg:
		if c.isalpha():
			num_of_alpha += 1
		elif c.isdigit():
			num_of_digits += 1
	print "LETTERS", str(num_of_alpha)
	print "DIGITS", str(num_of_digits)

'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''
def func14():
	msg = raw_input("Enter a sentence ->")
	results = dict(upper=0, lower=0)

	for c in msg:
		if not c.isalpha():
			continue
		if c.isupper():
			results['upper'] += 1
		elif c.islower():
			results['lower'] += 1
 	
 	print "UPPER CASE", results['upper']
	print "LOWER CASE", results['lower']



'''
Question 15
Level 2

Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106
'''
def func15(num):
	eq = "{0}+{0}{0}+{0}{0}{0}+{0}{0}{0}{0}".format(num)
	nums = [ int(s) for s in eq.split('+')]
	print sum(nums)


'''
Question 16
Level 2

Question:
Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9
Then, the output should be:
1,9,25,49,81
'''
def func16():
	msg = raw_input("Enter comma-separated numbers ->")
	nums = msg.split(',')
	results = [ str(n**2) for n in map(int, nums) if n%2 ]
	print ','.join(results)

'''
Question 17
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from file input.
The transaction log format is shown as following:
D 100
W 200
D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
'''
def func17():
	balance = 0
	with open('transaction.txt', 'rb') as infile:
		for line in infile.readlines():
			trans = line.split()
			if trans[0] == 'D':
				balance += float(trans[1])
			elif trans[0] == 'W':
				balance -= float(trans[1])
	print balance


'''
Question 18
Level 3

Question:
A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria.
Passwords that match the criteria are to be printed, each separated by a comma.
Example
If the following passwords are given as input to the program:
ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
ABd1234@1
'''

def func18():
	msg = raw_input("Enter comma-separated passwords ->")
	msgs = msg.split(',')
	results = []
	for pw in msgs:
		if not re.search('[a-z]', pw):
			continue
		if not re.search('[0-9]', pw):
			continue
		if not re.search('[A-Z]', pw):
			continue
		if not re.search('[$#@]', pw):
			continue
		if len(pw) > 12 or len(pw) < 6:
			continue
		results.append(pw)
	print results

'''
Question 19
Level 3

Question:
You are required to write a program to sort the (name, age, height) tuples by ascending order where name
is string, age and height are numbers. The tuples are input by console. The sort criteria is:
1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.
The priority is that name > age > score.
If the following tuples are given as input to the program:
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
Then, the output of the program should be:
[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
'''
from operator import itemgetter
# NOTE: itemgetter is used to enable multiple sort keys.
def func19():
	persons = []
	with open("persons.txt", 'rb') as infile:
		for line in infile.readlines():
			persons.append(tuple(line.split(',')))

	print sorted(persons, key=itemgetter(0,1,2))


'''
Question 20
Level 3

Question:
Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
'''
def gen_func(n):
	for i in xrange(0,n):
		if i%7 == 0:
			yield i
		i += 1

def func20():
	results = []
	gen = gen_func(100)
	for i in gen:
		results.append(i)
	print ','.join(map(str, results))


'''
Question 21
Level 3

Question
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement
and original point. If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be:
2
'''
def func21():
	positions = []
	with open('robot.txt', 'rb') as infile:
		for line in infile.readlines():
			positions.append(line.split())

	pos = [0, 0]
	for position in positions:
		if position[0] == 'UP':
			pos[1] += int(position[1])
		elif position[0] == 'DOWN':
			pos[1] -= int(position[1])
		elif position[0] == 'RIGHT':
			pos[0] += int(position[1])
		elif position[0] == 'LEFT':
			pos[0] -= int(position[1])

	distance = int(round(sqrt(abs(pos[0])**2 + abs(pos[1])**2)))
	print distance


'''
Question 22
Level 3

Question:
Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
Suppose the following input is supplied to the program:
New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
Then, the output should be:
2:2
3.:1
3?:1
New:1
Python:5
Read:1
and:1
between:1
choosing:1
or:2
to:1
'''
def func22():
	msg = raw_input("Enter String ->")
	words = msg.split()
	result = {}
	for w in words:
		result[w] = result.get(w, 0) + 1

	print result





def main():
	'''
	print "\n --- Question 1 ---"
	func1(2000, 3200)
	print "\n --- Question 2 ---"
	func2(8)
	print "\n --- Question 3 ---"
	func3(8)
	print "\n --- Question 4 ---"
	func4()
	print "\n --- Question 5 ---"
	func5()
	print "\n --- Question 6 ---"
	func6()
	print "\n --- Question 7 ---"
	func7()
	print "\n --- Question 8 ---"
	func8()
	print "\n --- Question 9 ---"
	func9()
	print "\n --- Question 10 ---"
	func10()
	print "\n --- Question 11 ---"
	func11()
	print "\n --- Question 12 ---"
	func12()
	print "\n --- Question 13 ---"
	func13()
	print "\n --- Question 14 ---"
	func14()
	print "\n --- Question 15 ---"
	func15(9)
	print "\n --- Question 16 ---"
	func16()
	print "\n --- Question 17 ---"
	func17()
	print "\n --- Question 18 ---"
	func18()
	print "\n --- Question 19 ---"
	func19()
	print "\n --- Question 20 ---"
	func20()
	print "\n --- Question 21 ---"
	func21()
	'''
	print "\n --- Question 22 ---"
	func22()

if __name__ == "__main__":
	main()