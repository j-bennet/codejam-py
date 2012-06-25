def process(data):
    cases = data[0]
    for i in range(1, len(data) - 1, 2):
        n = data[i]
        follows = data[i + 1].split(' ')
        for j in range(len(follows)): follows[j] = int(follows[j])
        print 'Case #%i:' % ((i / 2) + (i % 2))
        #print follows
        process_followers(follows)

def process_followers(follows):
    for d in range(1, len(follows) + 1):
        c = count_followers(d, follows)
        print c

def count_followers(monk, follows):
    total = 0

    queue = [monk]
    visited = {}

    while len(queue) > 0:
        
        current = queue.pop()
        visited[current] = 1
        total += 1

        for i in range(len(follows)):
            if follows[i] == current:
                if (i + 1) not in visited:
                    queue.append(i + 1)
    
    return total

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
    process(data)
