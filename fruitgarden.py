import random

colors = [0, 0, 0, 0, 0]

def GameSetup():
    global colors
    colors = [4,4,4,4,0]

def GameEnd():
    if (colors[0] + colors [1] + colors [2] + colors [3]) == 0:
        return 1
    elif colors[4] == 6:
        return 2
    else:
        return 0

def GameLoop():
    global colors
    GameSetup()
    while GameEnd() == 0:
        ' print(colors) '
        dice = random.randrange(0,6)
        ' print(dice) '
        if dice < 4:
            if colors[dice] > 0:
                colors[dice] -= 1
        elif dice == 4:
            colors[4] += 1
        elif dice == 5:
            ' WHAT TO DO ON BASKET'
            ''' pick abundant fruit 
            for i in range(0, 2):
                if colors[i] > colors[i+1]:
                    dummy = i
                else :
                    dummy = i+1 '''
            ''' pick rare fruit '''
            for i in range(0, 2):
                if colors[i] > colors[i+1]:
                    dummy = i
                else:
                    dummy = i+1

            colors[dummy] -= 1
    return GameEnd()


wins = 0
loss = 0
for i in range(1, 10000000):
    dummy = GameLoop()
    if dummy == 1:
        wins += 1
    elif dummy == 2:
        loss += 1
    if i%100 == 0:
        print(wins/(wins+loss))