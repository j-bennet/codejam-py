import sys

def process_cases(data):
    cases = data[0]
    out = open(sys.argv[1] + '.txt', 'w')
    
    for i in range(1, len(data)):
        case = map(int, data[i].split())
        
        n = case[0]
        k = case[1]
        
        sk = bin(k)[2:]
        sk = sk.zfill(n)

        sk = sk[-n:]
        # print n, len(sk)
        sk = list(sk)

        r = 'ON'
        if '0' in sk:
            r = 'OFF'

        out.write('Case #%i: %s\n' % (i, r))

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
