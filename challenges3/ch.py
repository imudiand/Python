import re
import time
import random


'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''
def func1():
	msg = raw_input("Enter name & age -->")

	data = re.split(',|/w', msg)
	current_year = int(time.strftime("%Y"))
	print "Hey %s ! You will turn 100 in the year %d" % (data[0], current_year + (100-int(data[1])))

'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?
'''
def func2():
	msg = raw_input("Enter a number-> ")
	num = re.split("\D", msg)
	if num:
		if int(num[0])%2:
			print "Odd number"
		else:
			print "Even number"

'''
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
'''
def func3():
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	print ','.join(str(_a) for _a in a if _a<5)

'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you dont know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
def func4():
	msg = raw_input("Enter a number ->")
	num = int(msg)
	divisors = [ str(i) for i in xrange(1,num+1) if num%i == 0]
	print ','.join(divisors)

'''
Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes.
'''
def func5():
	# Generate a list of random nos.
	a = random.sample(range(1,11), random.randint(0,9))
	b = random.sample(range(1,15), random.randint(0, 14))

	print a
	print b
	print list(set(a) | set(b))

'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
def func6():
	msg = raw_input("Enter a string ->")

	is_palindrome = lambda msg: msg == msg[::-1]
	if is_palindrome(msg):
		print "String IS a palindrome"
	else:
		print "String NOT a palindrome"

'''
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
'''
def func7():
	
	logic = {
		'rock': 'scissors',
		'scissors': 'paper',
		'paper': 'rock'
	}

	while(True):
		msg1 = raw_input("Player 1 ->")
		msg2 = raw_input("Player 2 ->")
		msg1 = re.split('\s,', msg1)
		play1 = msg1[0].lower()
		msg2 = re.split('\s,', msg2)
		play2 = msg2[0].lower()

		if play1 not in logic:
			print "Wrong input by player1"
		elif play2 not in logic:
			print "Wrong input by player2"
		elif play1 == play2:
			print "Its a Tie !"
		elif logic.get(play1) == play2:
			print "Player 1 wins !"
		elif logic.get(play2) == play1:
			print "Player 2 wins !"
		else:
			print "Cant decide who won"

		continue_game = raw_input("Continue Game ? (Y/N) ->")
		if continue_game.lower() == "n":
			break

def func8():
	num = random.randint(0,10)
	while(True):
		msg = raw_input("Guess a num b/w 0-9 ->")
		msg = re.split('\s,',msg)
		user_num = int(msg[0])
		if user_num == num:
			print "You win. The number is: {0}".format(num)
			break
		else:
			print "Try again"


def main():
	#func1()
	#func2()
	#func3()
	#func4()
	#func5()
	#func6()
	#func7()
	func8()
if __name__ == "__main__":
	main()