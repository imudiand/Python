import re

def func1():
	s = '100 NORTH MAIN ROAD'
	print re.sub("ROAD", "RD.", s)

	s = '100 NORTH BROAD ROAD'
	print re.sub("ROAD$", "RD.", s)

	s = '100 BROAD'
	print re.sub(r"\bROAD$", "RD.", s)

	s = '100 BROAD ROAD APT. 3'
	print re.sub(r"\bROAD\b", "RD.", s)

def func2():
	"""
		U.S phone numbers regex
	"""

	nums = '''
		800-555-1212
		800 555 1212
		800.555.1212
		(800) 555-1212
		1-800-555-1212
		800-555-1212-1234
		800-555-1212x1234
		800-555-1212 ext. 1234
		work 1-(800) 555.1212 #1234
	'''

	pattern = r"(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$"
	regex = re.compile(pattern)

	print regex.search("800-555-1212").groups()
	print regex.search("800 555 1212").groups()
	print regex.search("800.555.1212").groups()

	print regex.search("(800) 555-1212").groups()
	print regex.search("1-800-555-1212").groups()

	print regex.search("800-555-1212-1234").groups()
	print regex.search("800-555-1212x1234").groups()

	print regex.search("800-555-1212 ext. 1234").groups()
	print regex.search("work 1-(800) 555.1212 #1234").groups()


def func3():
	""" IP address regex """
	ip_address = "255.255.255.255"


	num = r"([0-9]|[1-9][0-9]|1[0,9]{2}|2[0,4][0,9]|25[0-5])"
	pattern = r"^{0}\.{0}\.{0}\.{0}$".format(num)
	regex = re.compile(pattern)

	match = regex.match(ip_address)
	if match:
		print "%s is an ip address" % (match.group())
	else:
		print "%s is not an ip address" % (ip_address)


def main():
	#func1()
	#func2()
	func3()

if __name__ == "__main__":
	main()