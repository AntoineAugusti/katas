def getExtension(filename):
	# To lowercase
	filename = filename.lower()
	# Try to find the index of the last dot
	indexLastDot = filename.rfind(".")
	# If it was not found, return a dummy value
	if indexLastDot == -1:
		return "NOTFOUND"
	return filename[indexLastDot+1:]

# Number of elements which make up the association table.
N = int(raw_input())
# Number of file names to be analyzed.
nbFiles = int(raw_input())

# Read extensions => MIME type
extensions = dict()
for i in xrange(N):
	# ext: file extension
	# mime: MIME type.
	ext, mime = raw_input().split()
	extensions[ext.lower()] = mime

# Try to find the MIME type for each file
for i in xrange(nbFiles):
	filename = raw_input()
	extension = getExtension(filename)
	print extensions.get(extension, "UNKNOWN")