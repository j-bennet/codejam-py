import sys

def process_cases(data):
    cases = data[0]
    out = open(sys.argv[1] + '.txt', 'w')

    crypt = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv', 'yeqz']
    clear = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up', 'aozq']
    
    h = {}
    
    for i in range(len(clear)):
        for j in range(len(clear[i])):
            h[crypt[i][j]] = clear[i][j]
    
    for i in range(1, len(data)):
        case = list(data[i])
        case = map(lambda x: h[x], case)
        case = ''.join(case)
        out.write("Case #%d: %s\n" % (i, str(case)))

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
