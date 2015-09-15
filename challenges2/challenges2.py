
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

def main():
	# Open & read a large line-based text file
	print "=== Example 1 ==="
	#func1()

	# Open & read a large non-line based file in chunks
	print "=== Example 2 ==="
	func2()


if __name__ == "__main__":
	main()