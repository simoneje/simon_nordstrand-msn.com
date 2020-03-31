import os
import sys
import cv2
import numpy as np
import time
from PIL import Image
import face


def meny():
    print("This is the menu!")
    print("1. Face detection & Data gathering")
    print("2. Face training")
    print("3. Face recognition")
    print("5. Quit")
    reply = input("Choose an option: ")

    while not reply == "":
        if reply == "1":
            face.data_collect()
            tillbaka()
            break
        elif reply == "2":
            face.trainer()
            tillbaka()
            break
        elif reply == "3": 
            face.faceDetect()
            tillbaka()
            break 
        elif reply == "4":
            face.faceReco()
            tillbaka()
            break
        elif reply == "5": 
            sys.exit(0)            
            
def tillbaka():
    reply = input("Vill du gå tillbaka till menyn? Y/N: ")
    if reply == "Yes" or reply == "y" or reply == "Y" or reply =="yes":
        meny()
    else:
        sys.exit()        
        
if __name__ == "__main__":
    meny()
    