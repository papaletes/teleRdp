#pylint:disable=E0401
from template import *
from time import sleep
import pyautogui as pg

wpos = 0
sleep(5)

# play
switchgame("https://t.me/catizenbot/bombie")
tungguklik("bombie/play.png")
tunggugambar("bombie/ingame.png")

# shop
if cekgambar("bombie/shop.png"):
    klikgambar("bombie/shop.png")
    sleep(1)
    # terusin...

# invite
if cekgambar("bombie/invite.png"):
    klikgambar("bombie/invite.png")
    sleep(2)
    # terusin...
  
# auto
# onkan autokan...
while not cekgambar("bombie/abis.png") and cekgambar("bombie/auto"):
    # klik truss
    sleep(5)
    
# rank
#...

# earn
if cekgambar("bombie/earn.png"):
    klikgambar("bombie/earn.png")
    # terusin...
    
# skill
if cekgambar("bombie/skill.png"):
    klikgambar("bombie/skill.png")
    # terusin...