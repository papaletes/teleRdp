from template import *
from time import sleep
import pyautogui as pg
import os, mss
wpos = 1
sleep(3)

link("https://sports.mtt.xyz/home/tourney")
tunggupixel(315,254,(170, 170, 170))
# pilih turney
klik(487,500)
if tunggupixel(884,566,(227, 94, 77)):
    klik(880,566)

#main