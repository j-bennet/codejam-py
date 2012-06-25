class robot:

    room = None
    position = 1
    command = -1
    target = None
    queue = []
    
    def __init__(self, room):
        self.room = room
        self.position = 1
        self.target = None
        self.command = -1
        self.queue = []

    def can_move(self):

        if self.target == None:
            self.target = self.dequeue()

        if self.target != None:
            if self.position == self.target[1]:
                self.command = self.target[0]

            return self.position != self.target[1]

        return False

    def execute(self):
        if self.target != None:
            self.command = -1
            self.target = self.dequeue()

    def move_step(self):
        if self.target == None or self.position == self.target[1]:
            return 0
        
        if self.position < self.target[1]:
            self.position += 1
        else:
            self.position -= 1

        if self.position == self.target[1]:
            self.command = self.target[0]

        return 1

    def enqueue(self, i, target):
        self.queue.append([i, target])

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        return self.queue.pop(0)

def process_cases(data):

    cases = int(data[0])

    for i in range(1, cases + 1):
        case = data[i].split()
        process_case(i, int(case[0]), case[1:])

def process_case(c, n, buttons):
    seconds = 0

    robots = {}
    robots['O'] = robot('O')
    robots['B'] = robot('B')
    
    for i in range(0, len(buttons) - 1, 2):
        room = buttons[i]
        button = int(buttons[i + 1])
        robots[room].enqueue(i / 2, button)

    time = 0
    current_command = 0

    while True:

        moved = False
        executed = False

        for k in robots:
            if robots[k].can_move():
                moved = True
                robots[k].move_step()
#               print 'Robot', k, 'moved to position', robots[k].position
            else:
                if robots[k].command == current_command and not executed:
                    executed = True
#                   print 'Robot', k, 'executed', robots[k].command
                    robots[k].execute()
                    current_command += 1

        if not (moved or executed): break

        time += 1

    print 'Case #%i: %i' % (c, time)

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
