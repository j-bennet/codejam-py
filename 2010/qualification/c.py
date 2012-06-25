import sys

def process_cases(data):
    cases = data[0]

    out = open(sys.argv[1] + '.txt', 'w')
    
    for i in range(1, len(data) - 1, 2):
        case_ix = i / 2 + 1

        r, k, n = map(int, data[i].split())
        q = map(int, data[i + 1].split())

        fits = {}

        total = 0
        head = 0
        
        rng = range(n*2 + 2)

        for ride in rng:
            fit = 0

            if head in fits:
                head, fit = fits[head][0], fits[head][1]
            else:
                tmp = head
                head, fit = calc_fit(head, k, n, q)
                fits[tmp] = [head, fit]

            total += fit

            #print 'n:', n, 'k:', k, 'ride:', ride + 1, 'fit:', fit

        out.write("Case #%d: %d\n" % (case_ix, total))

    out.close()

def calc_fit(head, k, n, q):
    fit = 0
    count = 0

    while count < n:
        if fit + q[head] <= k:
            fit += q[head]
            head = (head + 1) % n
            count += 1
        else:
            break

    return head, fit

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
