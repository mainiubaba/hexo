__author__ = 'Administrator'
# -*- coding: utf-8 -*-

import random
import time

def game():
    player = random.randint(1,6)
    print("You 的点数是=== " + str(player) )
    ai = random.randint(1,6)
    print("PC的点数是...." )
    time.sleep(2)
    print("PC机的点数是=== " + str(player) )
    if player > ai :
        print("You 赢了")  # notice indentation
    elif player == ai :
        print("持平")
    else:
        print("You 输了")
    print("Quit?? Y/N")
    cont = input()
    if cont == "Y" or cont == "y":
        exit()
    elif cont == "N" or cont == "n":
        pass
    else:
        print("没打对，重新输入Y还是N")

while True:
    print("比点游戏v0.1")
    game()
