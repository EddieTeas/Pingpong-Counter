left = input("How many points does left side have? ")
right = input("How many points does right side have? ")
r = int(right)
le = int(left)
match = input("Q: for quick match. L: for long match ")

if match == 'l':
    points = 21
    switch = 5
else:
    points = 11
    switch = 2

count = 0
while le <= points or r <= points:
    if le == points:
        break
    elif r == points:
        break
    else:
        print("left: " + str(le) + " Right: " + str(r))
        scored = input("Who scored a point: l or r? ")
        count += 1
        print("")
        if scored  == "l":
            le += 1

            if le == points-1:
                print("")
                print("Game Point")
                print()
        else:
            r += 1
            if r == points-1:
                print("")
                print("Game Point")
                print()

if le == points:
    print("*****************************************")
    print("\t   Winner is Left")
    print("*****************************************")
    print("")
else:
    print("*****************************************")
    print("\t   Winner is Right")
    print("*****************************************")
    print("")



print("\n\n Good Game")