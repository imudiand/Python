import re

# re.search
def find_patterns():
	''' Find 1st occurance of pattern in text. '''

	patterns = ['this', 'that']
	text = 'Does this text match the pattern?'

	for pattern in patterns:
		# search() takes the pattern and text to scan, and returns a Match object
		# when the pattern is found. If the pattern is not found, search() returns None.
		print 'Looking for "%s" in "%s" ->' % (pattern, text),
		match = re.search(pattern, text)
		if match:
			start = match.start()
			end = match.end()-1
			print "Found a match from %d to %d" % (start, end)
		else:
			print 'No match.'

# re.compile
# re.search
def compiled_regex():
	''' Find 1st occurance of pattern in text using precompiled regex '''

	patterns = ['this', 'that']
	text = 'Does this text match the pattern?'

	re_patterns = [ re.compile(p) for p in patterns ]
	for regex in re_patterns:
		match = regex.search(text)
		if match:
			start = match.start()
			end = match.end()-1
			print "Found a match from %d to %d" % (start, end)
		else:
			print "No match."

# re.findall()
def find_all():
	''' Find all occurances of pattern in text. '''
	''' findall() only returns the matched text string '''

	pattern = 'ab'
	text = 'abbaaabbbbaaaaa'
	matches = re.findall(pattern, text)
	for match in matches:
		print "Found:", match

# re.finditer()
def find_iter():
	''' Find all occurances of pattern in text using finditer() '''
	''' Unlike findall(); finditer() returns an iterator that produces Match obj. '''

	pattern = 'ab'
	text = 'abbaaabbbbaaaaa'
	matches = re.finditer(pattern, text)
	for match in matches:
		print "Found %s at %d:%d" % (match.group(), match.start(), match.end()-1)


# This is a generator func
def character_position(func):
	def func_wrapper(pattern, text):
		# Show the character positions and input text
		print
		print ''.join(str(i/10 or ' ') for i in range(len(text)))
		print ''.join(str(i%10) for i in range(len(text)))
		print text

		func(pattern, text)
	return func_wrapper

@character_position
def test_patterns(patterns, text):
	''' Find all occurances of pattern in text using finditer() '''
	''' Unlike findall(); finditer() returns an iterator that produces Match obj. '''
	for pattern in patterns:
		print
		print 'Matching "%s"' % pattern
		matches = re.finditer(pattern, text)
		for match in matches:
			print "Found %s at %d:%d" % (match.group(), match.start(), match.end()-1)

def main():
	# A. Finding Patterns in Text
	print " === Example 1 === "
	find_patterns()

	# B. Compiling Expressions
	print " === Example 2 === "
	compiled_regex()

	# C. Multiple Matches
	print " === Example 3 === "
	find_all()

	print " === Example 4 === "
	find_iter()

	# D. Patter Syntax - Metacharacters

	# D1. Repetition
	# There are 5 ways to express repetition:
	# A pattern following by the below metacharacters
	# * --> pattern is repeated 0 to many times
	# + --> pattern is repeated 1 to many times
	# ? --> pattern appears 0 or 1 time only
	# {m} --> pattern appears m times
	# {m,n} --> pattern appears between min m & max n times

	print " === Example 5 === "
	test_patterns(['ab'], 'abbaaabbbbaaaaa')

	print " === Example 6 === "
	patterns = [ 'ab*',     # a followed by zero or more b
                'ab+',     # a followed by one or more b
                'ab?',     # a followed by zero or one b
                'ab{3}',   # a followed by three b
                'ab{2,3}', # a followed by two to three b
                ]
	test_patterns(patterns, 'abbaaabbbbaaaaa')

	print " === Example 7 === "
	# Disable greedy behaviour by following the repetition metachar
	# with a ? as below.
	# Now; for any substring where 0 occurances of b are allowed;
	# the matched substring doesnt include any b characters.
	patterns = [
		'ab*?',     # a followed by zero or more b
		'ab+?',     # a followed by one or more b
		'ab??',     # a followed by zero or one b
		'ab{3}?',   # a followed by three b
		'ab{2,3}?', # a followed by two to three b
	]
	test_patterns(patterns, 'abbaaabbbbaaaaa')


	# D2. Character Sets
	# [] --> match characters in []. Eg: [ab] matches either a OR b
	# ^ --> ignore characters. Eg: [^-. ] ignores sequences with -, . or a space.
	# [a-z] --> sequences of lower case letters
	# [A-Z] --> sequences of upper case letters
	# [a-zA-Z]+' --> sequences of lower or upper case letters
	# [A-Z][a-z]+' --> one upper case letter followed by lower case letters
	# . --> pattern should match any single character in that position

	print " === Example 8 === "
	patterns = [
		'[ab]',    # either a or b
		'a[ab]+',  # a followed by one or more a or b
		'a[ab]+?', # a followed by one or more a or b, not greedy
	]
	test_patterns(patterns, 'abbaaabbbbaaaaa')

	print " === Example 9 === "
	patterns = [
		'[^-. ]+',  # sequences without -, ., or space
	]
	test_patterns(patterns, 'This is some text -- with punctuation.')

	print " === Example 10 === "
	patterns = [
		'[a-z]+',      # sequences of lower case letters
		'[A-Z]+',      # sequences of upper case letters
		'[a-zA-Z]+',   # sequences of lower or upper case letters
		'[A-Z][a-z]+', # one upper case letter followed by lower case letters
	]
	test_patterns(patterns, 'This is some text -- with punctuation.')


	print " === Example 11 === "
	patterns = [
		'a.',   # a followed by any one character
		'b.',   # b followed by any one character
		'a.*b', # a followed by anything, ending in b
		'a.*?b', # a followed by anything (or nothing), ending in b
	]
	test_patterns(patterns, 'abbaaabbbbaaaaa')


if __name__ == "__main__":
	main()