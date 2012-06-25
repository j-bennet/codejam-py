import sys, time

def process_cases(data):
    cases = data[0]
    out = open(sys.argv[1] + '.txt', 'w')
    
    ttm = time.time()
    
    for i in range(1, len(data)):
        tm = time.time()
        case = map(int, data[i].split())
        
        a = case[0]
        b = case[1]

        c = [j for j in range(a, b + 1, 1)]
        
        total = 0
        h = {}

        for x in c:
            for r in iter_rotate(x):
                if r > x and r >= a and r <= b:
                    if str(r) + str(x) not in h and str(x) + str(r) not in h:
                        total += 1
                        h[str(x) + str(r)] = True
                        print 'Duplicate:', x, r

        print "Case #%d: %d sec" % (i, time.time() - tm)

        out.write("Case #%d: %d\n" % (i, total))

    out.close()
    print 'Total time: %d sec' % (time.time() - ttm)

def iter_rotate(n):
    s = str(n)
    for i in range(1, len(s)):
        yield int(s[-i:] + s[:len(s)-i])

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
