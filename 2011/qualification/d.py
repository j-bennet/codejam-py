def process_cases(data):
	for i in range(1, len(data) - 1, 2):
		ncase = data[i]
		case = data[i + 1].split()
		case = map(int, case)
		process_case(i/2 + 1, case)

def process_case(i, case):
	total = 0
	for j in range(len(case)):
		if case[j] != (j + 1):
			total += 1
	print 'Case #%i: %.6f' % (i, total)

def readdata(filename):
    data = []
    f = open(filename, 'r')
    for line in f:
        data.append(line.strip())
    return data

import sys

if len(sys.argv) < 2:
    print 'Usage:', sys.argv[0], '<input_file_name>'
else:
    data = readdata(sys.argv[1])
    process_cases(data)
