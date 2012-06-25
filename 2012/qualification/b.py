import sys

def process_cases(data):
    cases = data[0]
    out = open(sys.argv[1] + '.txt', 'w')
    
    for i in range(1, len(data)):
        case = map(int, data[i].split())
        n, s, p = case[0], case[1], case[2]
        totals = case[3:]

        qualify = 0
        
        if p == 0:
            qualify = n
        else:
            surprises = s

            min_total = 3 * p - 2
            if min_total < 0:
                min_total = p
        
            min_total_surprise = 3 * p - 4
            if min_total_surprise < 0:
                min_total_surprise = p

            for t in totals:
                if t >= min_total:
                    qualify += 1
                elif t >= min_total_surprise and surprises > 0:
                    qualify += 1
                    surprises -= 1

        out.write("Case #%d: %d\n" % (i, qualify))

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
