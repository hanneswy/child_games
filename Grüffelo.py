import random

animals = [0, 0, 0]
road = 0

def GameSetup():
    global animals, road
    animals = [0,0,0]
    road = 0

def GameEnd():
    if (animals[0] + animals [1] + animals [2]) == 15:
        return 2
    elif road >= 31:
        return 1
    else:
        return 0

def MouseBack():
    global road
    backstop = [3,6,11,13,16,20,23,26,30]
    road -= 1
    'print("MouseBack! => ", road)'
    for i in backstop:
        if road == i:
            road +=1
            'print("backstop! => ", road)'


def GameLoop():
    global animals, road
    GameSetup()
    while GameEnd() == 0:
        dice = random.randrange(0,6)
        if dice < 3:
            road = road + dice + 1
            'print("dice:", dice+1, " => road: ", road)'
        else:
            if animals[dice-3] < 5:
                animals[dice-3] += 1
            if animals[dice-3] >= 5:
                MouseBack()
            'print("dice:", dice+1, " => animals: ", animals)'
    return GameEnd()


'print(GameLoop())'
wins = 0
loss = 0
for i in range(1, 1000000):
    dummy = GameLoop()
    if dummy == 1:
        wins += 1
    elif dummy == 2:
        loss += 1
    if i%100 == 0:
        print(wins/(wins+loss))
print(wins/(wins+loss))