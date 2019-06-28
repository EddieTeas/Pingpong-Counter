Team1 = input("Team1 name: ")
Team2 = input("Team2 name: ")
left = input("How many points does "+Team1+" side have? ")
right = input("How many points does "+Team2+" side have? ")
r = int(right)
le = int(left)
match = input("Q: for quick match. L: for long match ")

if match == 'l':
    points = 21
    switch = 5
else:
    points = 11
    switch = 2

def gamePoint(score, pts):
    if score == pts-1:
        print("\n*****Game Point******\n")
        
def winner(winner):
    print("*****************************************")
    print("\t   Winner is " + winner)
    print("*****************************************")
    print("")

def switchCheck(total, switch):
    if total % switch ==0:
        print("\n*****Switch*****\n")

count = 0
while le <= points or r <= points:
    if le == points:
        break
    elif r == points:
        break
    else:
        print(Team1+" (left): " + str(le) + " "+Team2+" (right): "+ str(r))
        goal = input("Who scored a point: l or r? ")
        print("")
        if goal == "l":
            le += 1
            gamePoint(le, points)
            switchCheck(le + r, switch)
                
        else:
            r += 1
            gamePoint(r, points)
            switchCheck(le+r, switch)

if le == points:
    winner(Team1)
else:
    winner(Team2)

print("\n\n Good Game")
