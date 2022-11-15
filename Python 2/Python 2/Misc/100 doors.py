doors = []
for i in range(100):
    doors.insert(i, "closed")

print doors

counter = 1

while counter < 100:
    for i in range(0,100,counter):
        counter += 1
        if doors[i] == "closed":
            doors[i] = "open"
        else:
            doors[i] = "closed"

print doors

