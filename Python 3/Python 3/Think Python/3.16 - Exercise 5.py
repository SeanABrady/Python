def horizontal_line():
    for i in range(0,2):
        print('+ ', end='')
        for i in range(0,4):
            print('- ', end='')
    print('+', end='')
    print()

def vertical_line():
    for i in range(0,2):
        print('/ ', end='')
        for i in range(0,4):
            print('  ', end='')
    print('/', end='')
    print()

horizontal_line()
for i in range(0,4):
    vertical_line()
horizontal_line()
for i in range(0,4):
    vertical_line()
horizontal_line()
