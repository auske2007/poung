#zhonglin
#poung smart
#nov 6 2023

import os
import time
import keyboard
import threading
os.system("cls")

py = 10

WID = 100
HIT = 30
def creat_list(wid, hei):

    list = [[" " for i in range(wid+2)] for j in range(hei+2)]
    return list


def update(list):
    
    #space in front of the list
    for space in range(10):
        print(" ", end="")
    #top edge
    for edge in range(len(list[1])+4-2):
        print("█",end="")
    print()

    for x in range(len(list)-2):

        #space in front of the list
        for space in range(10):
            print(" ", end="")

        #left edge
        print("██", end="")

        #real list itself
        for y in range(len(list[x])-2):
            print(list[x][y],end="")
         

        #right edge
        print("██")

    #space
    for space in range(10):
        print(" ", end="")

    #bottom edge
    for edge in range(len(list[1])+4-2):
        print("█",end="")
    print()

    os.system("cls")
    

def ball(x,y,list):
    list[y][x] = "＠"
    list[y][x+1] = ""

def padle1_move(list):
    global py


    pv = 1
    if keyboard.read_key() == "w":
        list[py][10] = " "
        list[py-1][10] = " "
        list[py-2][10] = " "
        list[py-3][10] = " "
        list[py-4][10] = " "
  
        #print("up")
        if py < 3:
            pv = 0
        pv = pv*-1

    elif keyboard.read_key() == "s":
        list[py][10] = " "
        list[py-1][10] = " "
        list[py-2][10] = " "
        list[py-3][10] = " "
        list[py-4][10] = " "
        
        #print("down")
        if py > HIT-2:
            pv = 0
      

    py += pv
       
        
        
def paddle1(py,px, list):
    list[py][px] = "█"
    list[py-1][px] = "█"
    list[py-2][px] = "█"
    list[py-3][px] = "█"
    list[py-4][px] = "█"



    

def move(x, y, xv, yv,list):
    #hiting wall
    if x > len(list[0])-5 or x < 0:
        xv = xv * -1
    
    #hitting ground
    if y < 0 or y > HIT-1:
        yv = yv * -1

    # or x< 10 and x+xv == 11 or x> 10 and x+xv == 9
    if list[y+yv][x+xv] != " ":
        xv = xv*-1
#10,4 10,10 10,14

    list[y][x] = " "
    list[y][x+1] = " "
    #print(xv, yv)
    x += xv
    y -= yv


    return x, y,xv,yv 

def thread2():
    while True:
       
        paddle1(py, 10, list)
      
        time.sleep(0.001)
        padle1_move(list)




list = creat_list(WID,HIT)

def main():
   
    xv = 2
    yv = 1
    x = 20
    y = 15
    px = 10
  
    pyv = 1
  
    width = 0
    threading.Thread(target=thread2, args=[]).start()
    while True:
        
    
        x,y,xv,yv = move(x, y,xv,yv,list)
        #bounce(x,y,XV,YV)
        print(x, y)
        print(xv)
        #print(len(list[0]))
        #print(len(list[0])-4)
        print(py)
        ball(x,y,list)
        
        

        update(list)
        time.sleep(0.001)
  

main()

    


