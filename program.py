import pyautogui as pt
import time 
import random 
name = ['sweetheart','queen','soul','love','life','future wife'] #choose the random word
for i in range(1,100): #loop for 100 times
    time.sleep(2) # wait for 2 sec 
    rdm = random.choice(name)
    pt.typewrite(f'I love You my {rdm}') #type the text
    pt.press('enter') 




    