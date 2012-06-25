def process(data):
    for i in range(1, len(data)):
        print 'Case #%i: %s' % (i, spell(data[i]))

def spell(s):
    v = find_vowels(s)
    result = 'Nothing.'
    for i in range(len(v)-2):
        i_beg = v[i]
        i_mid = v[i+1] + 1
        i_end = v[i+2] + 1
        word = s[i_beg:i_mid]
        ix = s.find(word, i_end, len(s))
        if ix != -1:
            result = 'Spell!'
            break
    return result

def find_vowels(s):
    v = []
    vowels = list('aeiou')
    for i in range(len(s)):
        if s[i] in vowels:
            v.append(i)
    return v

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