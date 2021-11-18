from PIL import Image,ImageFont,ImageDraw
from pyautogui import *
import pyautogui as pg
import keyboard as kb
import pyfiglet as pfg
from time import sleep
import os

pg.FAILSAFE = False

logo = pfg.figlet_format("Squash the bee.")
print(logo+"\n")
mode = int(input("Modes\n------\nTo select any mode given below, type its name\n0 - lets you create a new word pack\n1 - lets you practise any created pack\nPlease, select mode: "))

def CreateImage(pack,txt,name):
    width,height = 300,40
    img = Image.new("RGB",(width,height),"#28a745")
    font = ImageFont.truetype("Montserrat-Regular.ttf",20)
    w,h = font.getsize(txt)
    draw = ImageDraw.Draw(img)
    draw.text(((width-w)/2,(height-5-h)/2),txt,font=font,fill="#FFF")
    img.save(f"{pack}/{name}.png")

images = []
def CreateList(pack):
    global images
    directory = os.listdir(f"packs/{pack}")
    for file in directory:
        if file.endswith('.png'):
            images.append(file)

whichWindow = "left"
def Run(X,Y,window,img):
    global whichWindow
    global number_of_words

    pg.click(X,Y)
    text = (img.split("."))[0]
    pg.write(text)
    pg.press("enter")
    whichWindow = window

def checkForStop():
    global running
    if kb.is_pressed("*"):
        running = False

number_of_words,start_time = 0,0.0
def Stats(start):
    global start_time
    global number_of_words
    if start == True:
        start_time = time.time()
    else:
        text = pfg.figlet_format("Stats:")
        print(text)
        hours_run = round(60/60/(time.time() - start_time),2)
        print(f"Hours run: {hours_run}")
        print(f"Number of words: {number_of_words}")
        bonus = 0
        while number_of_words > 20:
            number_of_words /= 20
            bonus += 1
        number_of_points = ((number_of_words*2) + (bonus*20))*2
        print(f"Number of points: {number_of_points}")

    start_time = time.time()


# PACK CREATION MODE
if mode == 0:
    text = pfg.figlet_format("Pack creation")
    print(text)
    pack_name = input("Enter name of the pack you want to create\nName: ")
    if os.path.isdir("packs") == False:
        os.mkdir("packs")
    if os.path.isdir(f"packs/{pack_name}") == False:
        os.mkdir(f"packs/{pack_name}")
    words_ENG,words_SK = [],[]
    
    num_of_words = int(input("How many words does the pack contain?\nPlease type in the number of words: "))

    i = 0
    while i < num_of_words:
        print("------------\n")
        word_eng = input("word: ")
        word_sk = input("transl: ")

        CreateImage(f"packs/{pack_name}",word_sk,word_eng)
        CreateImage(f"packs/{pack_name}",word_eng,word_sk)
        i += 1
    print("To practise your newly created pack, please restart the bot.py file.")

# FARMING MODE
if mode == 1:
    text = pfg.figlet_format("Pack practise")
    print(text)
    print("List of available packs:\n")
    print("=========================\n")
    pack_num,pack_list = 1,[]
    for each in os.listdir("packs"):
        print(f" {pack_num}. {each}")
        pack_num += 1
        pack_list.append(each)
    pack_index = int(input("\nType the name of the pack you wish to practise: "))
    pack_name = pack_list[pack_index-1]
    CreateList(pack_name)
    double = int(input("Do you wish to run double mode?\n0 - no, 1 - yes: "))
    text = pfg.figlet_format("Running...")
    print(text)
    print("\nWhen you wish to shut down the bot, hold the star key ===> * <===\nShutting the bot down will most likely ruin your words in a row bonus.")
    
    if double == 0:
        pg.click(960,660)
        running = True
        Stats(True)

        while running == True:
            for image in images:
                if pg.locateOnScreen(f"packs/{pack_name}/{image}",confidence=0.65,region=(720,170,420,110)) != None:
                    Run(970,455,"left",image)
                    number_of_words += 1

                checkForStop()

    elif double == 1:
        pg.click(500,665)
        pg.click(1425,665)
        running = True
        First = False
        Stats(True)

        while running == True:
            if whichWindow == "left":
                for image in images:
                    if pg.locateOnScreen(f"packs/{pack_name}/{image}",confidence=0.65,region=(275,170,400,200)) != None:
                        Run(520,460,"right",image)
                        number_of_words += 1

                    checkForStop()

            elif whichWindow == "right":
                for image in images:
                    if pg.locateOnScreen(f"packs/{pack_name}/{image}",confidence=0.65,region=(1250,170,450,200)) != None:
                        Run(1430,460,"left",image)
            
                    checkForStop()

    if running == False:    
        if double == "yes":
            sleep(0.1)
            pg.click(500,665)
            sleep(0.1)
            pg.click(1425,665)
        elif double == "no":
            pg.click(960,660)
        text = pfg.figlet_format("Stopped.")
        print(text)
        input("Press any key to shutdown...")