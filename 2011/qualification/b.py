def process_cases(data):
	cases = int(data[0])

	for i in range(1, len(data)):
		case = data[i].split()
		
		ncombine = int(case[0])
		combine = []
		oppose = []

		for j in range(1, ncombine + 1):
			combine.append(case[j])

		noppose = int(case[ncombine + 1])
		start = ncombine + 2
		for j in range(start, start + noppose):
			oppose.append(case[j])

		invoke = list(case[len(case)-1])

	   	process_case(i, combine, oppose, invoke)

def process_case(i, combine, oppose, invoke):
	element = []

	while len(invoke) > 0:
		current = invoke.pop(0)

		is_combined = False
		is_opposed = False

		# can it be combined?
		if len(element) > 0:
			last = len(element) - 1
			for c in combine:
				if (c[0] == current and c[1] == element[last]) or (c[1] == current and c[0] == element[last]):
					element[last] = c[2]
					is_combined = True

		if not is_combined:
			for o in oppose:
				if (o[0] == current and o[1] in element) or (o[1] == current and o[0] in element):
					element = []
					is_opposed = True

		if (not is_combined) and (not is_opposed):
			element.append(current)

	s = str(element).replace('\'', '')
	print 'Case #%i: %s' % (i, s)
	
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
