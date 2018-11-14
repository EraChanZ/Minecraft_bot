from PIL import ImageGrab, Image
import pyautogui
import keyboard
from numpy import *
from time import sleep
import random
clickRespawn = (533,529)
GravyImg = Image.open('./Gravy.png').load()
StoneImg = Image.open('./Stone.png').load()
ComeBack = Image.open('./afk.png').load()
trashItems = [GravyImg,StoneImg]
cases={}
throw = {}
def kick(num):
    global throw
    pyautogui.click(throw[num][0],throw[num][1])
    pyautogui.click(300,throw[num][1])
def click(x,y):
    pyautogui.click(x,y)
def TakePicture(x1,y1,x2,y2):
    tempIm = ImageGrab.grab(bbox=(x1,y1,x2,y2)).load()
    return tempIm
def SavePicture(x1,y1,x2,y2):
    tempIm = ImageGrab.grab(bbox=(x1,y1,x2,y2))
    tempIm.save('./'+str(random.randint(1,1000))+'.png','png')
    return tempIm
def CompareImg(A,B,width,height):
    diff=0
    for x in range(0, int(width/2)):
        for y in range(0,int(height/2)):
            (rA, gA, bA) = A[x*2,y*2]
            (rB, gB, bB) = B[x*2,y*2]
            diff += ((rA-rB) ** 2) + ((gA-gB) ** 2) + ((bA-bB) ** 2)
    return diff
def is_dead(Respawn):
    img = RespawnBtn()
    difference = CompareImg(img,Respawn,594,55)
    if difference < 1000:
        return True
    else:
        return Falsee
def find_all_cases():
    global cases
    dist = 36
    counter = 0
    for i in range(381, 705, dist):
        for k in range(537, 645, dist):
            counter += 1
            cases[counter] = [i,k]
    counter = 0
    for i in range(412, 736, dist):
        for k in range(554, 662, dist):
            counter += 1
            cases[counter].append(i)
            cases[counter].append(k)
            throw[counter] = [(cases[counter][0]+i)/2,(cases[counter][1]+k)/2]
find_all_cases()
print(cases)
def clean_inventory(trash):
    pyautogui.keyDown('e')
    sleep(0.05)
    pyautogui.keyUp('e')
    for case in cases:
        item = TakePicture(cases[case][0],cases[case][1],cases[case][2],cases[case][3])
        width = 31
        height = 17
        for ash in trash:
            differ = CompareImg(item,ash,width,height)
            if differ == 0:
                kick(case)
                break
    pyautogui.keyDown('e')
    sleep(0.05)
    pyautogui.keyUp('e')
cou = 0
while True:
    if keyboard.is_pressed('0'):
        clean_inventory(trashItems)
    if keyboard.is_pressed('k'):
        pyautogui.mouseDown(542,536)
        pyautogui.keyDown('w')
        sleep(1)
        pyautogui.keyUp('w')
        sleep(1)
    if cou % 100 == 0:
        pic = TakePicture(343,549,738,584)
        dif = CompareImg(ComeBack,pic,395,35)
        if dif == 0:
            print('Перезахожу')
            click((343+738)/2,(549+584)/2)
            pyautogui.doubleClick(380,179)
    cou += 1
