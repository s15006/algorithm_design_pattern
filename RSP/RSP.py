#!/usr/bin/python3
LOOP_COUNT = 10000000

GU = 0
CHOKI = 1
PA = 2

DRAW = 0
LOSE = 1
WIN = 2

def RSPNine(player, npc):
    judge = 0
    if player == GU and npc == GU:
        judge = DRAW
    elif player == GU and npc == CHOKI:
        judge = WIN
    elif player == GU and npc == PA:
        judge = LOSE
    elif player == CHOKI and npc == GU:
        judge = LOSE
    elif player == CHOKI and npc == CHOKI:
        judge = DRAW
    elif player == CHOKI and npc == PA:
        judge = WIN
    elif player == PA and npc == GU:
        judge = WIN
    elif player == PA and npc == CHOKI:
        judge = LOSE
    elif player == PA and npc == PA:
        judge = DRAW

    if judge == DRAW:
        judge = 0
    elif judge == LOSE:
        judge = 0
    elif judge == WIN:
        judge = 0


def RSPThree(player, npc):
    judge = 0

    if player == npc:
        judge = DRAW
    elif (player == GU and npc == CHOKI) or (player == CHOKI and npc == PA) or (player == PA and npc == GU):
        judge = WIN
    else:
        judge = LOSE

    if judge == DRAW:
        judge = 0
    elif judge == LOSE:
        judge = 0
    elif judge == WIN:
        judge = 0

def RSPCalc(player, npc):
    judge = ((player - npc) + 3) % 3

    if judge == DRAW:
        judge = 0
    elif judge == LOSE:
        judge = 0
    elif judge == WIN:
        judge = 0

def RSPList(player, npc):
    judge = []
    judge.append([DRAW, WIN, LOSE])
    judge.append([LOSE, DRAW, WIN])
    judge.append([WIN, LOSE, DRAW])

    if judge[player][npc] == DRAW:
        judge = 0
    elif judge[player][npc] == LOSE:
        judge = 0
    elif judge[player][npc] == WIN:
        judge = 0

if __name__ == '__main__':
    import random
    import time

    player = random.randint(0, 3)
    npc = random.randint(0, 3)

    start = time.time()
    for i in range(LOOP_COUNT):
        RSPNine(player, npc)

    end = time.time()

    print('経過時間:',(end - start))
    start = time.time()
    for i in range(LOOP_COUNT):
        RSPThree(player, npc)

    end = time.time()

    print('経過時間:',(end - start))
    start = time.time()
    for i in range(LOOP_COUNT):
        RSPCalc(player, npc)

    end = time.time()

    print('経過時間:',(end - start))
    start = time.time()
    for i in range(LOOP_COUNT):
        RSPList(player, npc)

    end = time.time()
    print('経過時間:',(end - start))
