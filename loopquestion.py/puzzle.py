doors = [False] * 100  
for person in range(1, 101):
    for i in range(person - 1, 100, person):
        doors[i] = not doors[i]  
for i, door in enumerate(doors, start=1):
    status = "open" if door else "closed"
    print(f"Door {i} is {status}")
