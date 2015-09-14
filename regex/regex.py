# https://pymotw.com/2/re/

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
	# Escape codes - are a compact representation for pre-defined character sets
	# 	\d - a digit
	#	\D - a non-digit
	#	\w - alphanumeric (i.e. not only alphabets - it matches alphabets + numbers)
	#	\w - non-alphanumeric
	#	\s - whitespace (tab, space, newline)
	#	\S - non-whitespace

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

	print " === Example 12 === "

	# Escapes are indicated by prefixing the character with a backslash (\).
	# Unfortunately, a backslash must itself be escaped in normal Python strings,
	# and that results in expressions that are difficult to read.
	# Using raw strings, created by prefixing the literal value with r, for creating regular expressions
	# eliminates this problem and maintains readability.

	patterns = [
		r'\d+', # sequence of digits
		r'\D+', # sequence of non-digits
		r'\w+', # sequence of alphanumeric
		r'\W+', # sequence of non-alphanumeric (not only alphabets)
		r'\s+', # sequence of whitespace
		r'\S+'  # sequence of non-whitespace
	]
	test_patterns(patterns, 'This is a prime #1 example!')


	print " === Example 13 === "

	# To match the characters that are part of the regular expression syntax,
	# escape the characters in the search pattern.
	patterns = [
		r'\\d\+', # escapes \ and + metacharacters
		r'\\D\+', # escapes \ and + metacharacters
		r'\\s\+', # escapes \ and + metacharacters
		r'\\S\+', # escapes \ and + metacharacters
		r'\\w\+', # escapes \ and + metacharacters
		r'\\W\+', # escapes \ and + metacharacters
	]
	test_patterns(patterns, r'\d+ \D+ \s+ \S+ \w+ \W+')



	# D3. Anchoring
	# Instead of describing the contents of the pattern to match;
	# you can also specify the relative location in the input text
	# where the pattern should appear using anchoring instructions.
	# ^ - start of string or line
	# $ - end of string or line
	# \A - start of string
	# \Z - end of string
	# \b - empty string at the beginning or end of a word
	# \B - empty string not at the beginning or end of a word
	print " === Example 13 === "
	patterns = [
		r'^\w+',     # word at start of string
		r'\A\w+',    # word at start of string
		r'\w+\S*$',  # word at end of string, with optional punctuation
		r'\w+\S*\Z', # word at end of string, with optional punctuation
		r'\w*t\w*',  # word containing 't'
		r'\bt\w+',   # 't' at start of word
		r'\w+t\b',   # 't' at end of word
		r'\Bt\B',    # 't', not start or end of word
	]
	test_patterns(patterns, 'This is some text -- with punctuation.')

	# D4. Constraining the Search

	# D4.1
	# match looks to see if pattern exists at start of text.
	# search looks to see if pattern exists anywhere in text.
	print " === Example 14 === "
	text = 'This is some text -- with punctuation.'
	pattern = 'is'

	m = re.match(pattern, text)
	print 'Match: Found', m

	match = re.search(pattern, text)
	print 'Search: Found %s at %d:%d' % (match.group(), match.start(), match.end())

	# D4.2
	# The search() method of a compiled regular expression accepts optional start and end position
	# parameters to limit the search to a substring of the input.
	print " === Example 15 === "
	text = 'This is some text -- with punctuation.'
	pattern = re.compile(r'\b\w*is\w*\b')
	print 'Text:', text
	print

	pos = 0
	while True:
		match = pattern.search(text, pos)
		if not match:
			break
		s = match.start()
		e = match.end()
		print '  %2d : %2d = "%s"' % \
			(s, e-1, text[s:e])
		# Move forward in text for the next search
		pos = e


	# E - Dissecting Matches with Groups
	# E1. use parantheses to group items together.
	print " === Example 15 === "
	patterns = [
		'a(ab)',    # 'a' followed by literal 'ab'
		'a(a*b*)',  # 'a' followed by 0-n 'a' and 0-n 'b'
		'a(ab)*',   # 'a' followed by 0-n 'ab'
		'a(ab)+',   # 'a' followed by 1-n 'ab'
	]
	test_patterns(patterns, 'abbaaabbbbaaaaa')

	# E2. To access the substrings matched by the individual groups within a pattern,
	# 		use the groups() method of the Match objectself.
	print " === Example 16 === "
	text = 'This is some text -- with punctuation.'
	patterns = [ r'^(\w+)',           # word at start of string
		r'(\w+)\S*$',        # word at end of string, with optional punctuation
		r'(\bt\w+)\W+(\w+)', # word starting with 't' then another word
		r'(\w+t)\b',         # word ending with 't'
	]

	for pattern in patterns:
		regex = re.compile(pattern)
		match = regex.search(text)
		print 'Matching "%s"' % pattern
		print '  ', match.groups()
		print

	# E3 - If you are using grouping to find parts of the string; but dont need all
	# of the parts matched by groups, you can ask for the match of only a single group with group().
	text = 'This is some text -- with punctuation.'
	print 'Input text            :', text

	# word starting with 't' then another word
	regex = re.compile(r'(\bt\w+)\W+(\w+)')
	print 'Pattern               :', regex.pattern

	match = regex.search(text)
	print 'Entire match          :', match.group(0)
	print 'Word starting with "t":', match.group(1)
	print 'Word after "t" word   :', match.group(2)

	print 'Words in match.groups()   :', match.groups()
	print 'Word in match.group()   :', match.group()

if __name__ == "__main__":
	main()
