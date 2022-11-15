def right_justify(string):
    spaces = 70 - len(string)
    spaces = ' ' * spaces
    print(spaces + string)

right_justify('Jade is a weenie')
