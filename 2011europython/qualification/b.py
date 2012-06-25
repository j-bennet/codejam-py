def process_cases(data):
    
    cases = int(data[0])
    ix = 1

    for i in range(cases):
        songs = int(data[ix])
        print 'Case #%i:' % (i + 1)
        collection = []
        for j in range(1, songs + 1):
            collection.append(data[ix + j])
        process_collection(collection)
        ix += songs + 1

def process_collection(data):
    if len(data) <= 1:
        print '""'
        return

    for i in range(len(data)):
        u = process_name(data, data[i], i)
        print u
    
def process_name(data, name, ix):
    #print ix, ':', name
    checked = {}
    unique = {}
    
    for l in range(1, len(name) + 1):
        for i in range(0, len(name)):
            s = name[i:i + l]
            #print 'length is', l, 'sub is', s, 'word is', name, 'len', len(name)
            if s not in checked:
                checked[s] = 1
                u = is_unique_match(data, s, ix)
                #print l, 'sub', s, 'of', name, 'is unique:', u
                if u:
                    unique[s.upper()] = 1

        if len(unique) > 0:
            break

    if len(unique) > 0:
        k = unique.keys()
        k.sort()
        #if len(k) > 1: print k # debug
        return '"' + k[0] + '"'

    return ':('

def is_unique_match(data, s, skip):
    unique = True
    for i in range(len(data)):
        if i != skip:
            ix = data[i].lower().find(s.lower())
            if ix != -1:
                unique = False
                break
    return unique

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