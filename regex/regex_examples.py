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





def main():
	func1()
	func2()


if __name__ == "__main__":
	main()