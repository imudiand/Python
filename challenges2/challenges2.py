
def func1():
	''' Read a large line-based text file '''
	with open('largefile.txt', 'rb') as infile:
		# readlines reads one line at a time
		for line in infile.readlines():
			print line

def file_chunk_gen_func(infile, size):
	while(True):
		chunk = infile.read(size)
		if not chunk:
			break
		yield chunk

def func2():
	''' Read a large non line-based text file in chunks '''
	infile = open('largefile_no_lines.txt', 'rb')
	chunk_size = 1024
	reader = file_chunk_gen_func(infile, 1024)
	for chunk in reader:
		print chunk
		print "================"



'''
Question 3
You are given N mobile numbers. Sort them in ascending order after which print them in standard format.
+91 xxxxx xxxxx
The given mobile numbers may have +91 or 91 or 0 written before the actual 10 digit number. Alternatively, there maynot be any prefix at all. 

Input Format
An integer N followed by N mobile numbers.

Output Format
N mobile numbers printed in different lines in the required format.

Sample Input
4
07895462130
919875641230
9195969878
+919345563841

Sample Output
+91 78954 62130
+91 91959 69878
+91 98756 41230
'''

def formatter(func):
	def wrapper():
		return [ "+91 "+n[0:6]+" "+n[6:11] for n in func() ]
	return wrapper

@formatter
def func3():
	valid_num = []
	with open('mobile_nos.txt') as infile:
		for num in infile.readlines():
			_n = num[::-1][0:11]
			valid_num.append(_n[::-1])
	return valid_num

'''
Question 4
Square the numbers in string
'''
import re
def func4():
	string = "1 2 3 4 5 6 7 8 9"
	square = lambda match: str(int(match.group())**2)
	print re.sub(r'\d+?', square, string)


def func5():
	htmlstr = """
		<head>
			<title>HTML</title>
		</head>
		<object type="application/x-flash" 
			data="your-file.swf" 
			width="0" height="0">
			<!-- <param name="movie"  value="your-file.swf" /> -->
			<param name="quality" value="high"/>
		</object>
	"""

	print re.sub("<!--.*-->", "", htmlstr)

'''
Question:
You are given a text of N lines. The text contains && and || symbols. 
Your task is to modify :

&& => and
|| => or
Both && and || should have space " " on both sides.

Input Format

First line contains integer, N. 
Next N lines contains the text.

Constraints

0<N<100

Neither && nor || occur in start or end of each line.
'''
def func6():
	strtext = """
		a = 1;
		b = input();

		if a + b > 0 && a - b < 0:
		    start()
		elif a*b > 10 || a/b < 1:
		    stop()
		print set(list(a)) | set(list(b)) 
		#Note do not change &&& or ||| or & or |
		#Only change those '&&' which has space on both sides.
		#Only change those '|| which has space on both sides.
	"""
	res = re.sub("(?<= )&&(?= )", "and", strtext)
	print re.sub("(?<= )\|\|(?= )", "or", res) # NOTE: | needs escaping unlike &


def main():
	'''
	# Open & read a large line-based text file
	print "=== Example 1 ==="
	func1()

	# Open & read a large non-line based file in chunks
	print "=== Example 2 ==="
	func2()
	
	print "=== Example 3 === "
	nums = func3()
	print "\n".join(nums)

	print "=== Example 4 ==="
	func4()

	print "=== Example 5 ==="
	func5()
	
	print "=== Example 6 ==="
	func6()



if __name__ == "__main__":
	main()