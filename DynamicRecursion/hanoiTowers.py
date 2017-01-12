def moveTower(height,storeTower1,storeTower2,hanoi):
    if height==1:
        move(height,storeTower1,hanoi)
    else:
        moveTower(height-1,storeTower1,hanoi,storeTower2)
        move(height,storeTower1,hanoi)
        moveTower(height-1,storeTower2,storeTower1,hanoi)

def move(height,st1,st2):
    print("move from ",st1,"to ",st2," height ", height)

moveTower(3,"A","B","C")
