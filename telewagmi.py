#pylint:disable=E0401
from template import *
from time import sleep
import pyautogui as pg

udhdaily = False
wpos = 0

# play
switchgame("https://t.me/WAGMIHUB_BOT/game?startapp=cj1VYUprRk9Hd1ZTdnUmdT1yZWY=", wpos)
sleep(10)

# claim
klik(319+wpos,809)