import sys

def process_cases(data):
    cases = data[0]
    out = open(sys.argv[1] + '.txt', 'w')
    
    for i in range(1, len(data)):
        case = map(int, data[i].split())[1:]
        out.write("Case #%d: %d\n" % (i, next - case[0]))

    out.close()

def readdata(filename):
    data = []
    f = open(filename, 'r')
    for line in f:
        data.append(line.strip())
    return data

if len(sys.argv) < 2:
    print 'Usage:', sys.argv[0], '<input_file_name>'
else:
    data = readdata(sys.argv[1])
    process_cases(data)
