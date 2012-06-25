import sys, time

def process_cases(data):
    cases = data[0]
    out = open(sys.argv[1] + '.txt', 'w')
    
    ttm = time.time()
    
    tens = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000]
    
    for i in range(1, len(data)):
        tm = time.time()
        case = map(int, data[i].split())
        
        a = case[0]
        b = case[1]

        d = len(str(a))

        cnt = 0

        for x in range(a, b + 1):
            vals = [0 for j in range(d)]
            
            for ix in range(1, d):
                vals[ix] = x / tens[ix] + x % tens[ix] * tens[d - ix]
            
            vals = sorted(vals)
            # print x, vals
            
            for ix in range(1, d):
                if x < vals[ix] and vals[ix - 1] < vals[ix] and vals[ix] <= b:
                    cnt += 1

        print "Case #%d: %d sec" % (i, time.time() - tm)

        out.write("Case #%d: %d\n" % (i, cnt))

    out.close()
    print 'Total time: %d sec' % (time.time() - ttm)

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
