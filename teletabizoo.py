#pylint:disable=E0401
from template import *
from time import sleep
import pyautogui as pg

udhdaily = False

# loop 9 jam
# play
switchgame("https://t.me/tabizoobot/tabizoo?startapp=tabizoo_tg_6184426572")
tungguklik("tabizoo/ingame.png")
sleep(1)
pg.scroll(-100)
sleep(1)
klik(544,802)
sleep(5)
if cekgambar("tabizoo/close.png"):
    klikgambar("tabizoo/close.png")
    sleep(2)

# spin
klik(702,830)
sleep(5)
for a in range(15):
    klik(538,685)
    sleep(7)

# upgrade
klik(380,826)
sleep(4)
if cekgambar("tabizoo/upg.png"):
    klik(608,281)
    sleep(3)
    klik(530,802)
    sleep(3)
    pg.hotkey("alt","left")
    sleep(2)

if udhdaily == False:
    # task daily
    klik(759,394)
    sleep(2.5)
    pg.scroll(-5)
    if cekgambar("tabizoo/daily.png"):
        klikgambar("tabizoo/daily.png")
        sleep(3)
        klik(537,748)
        sleep(2)
        klik(737,254)
    pg.hotkey("alt", "left")
    # draw
    klik(536,815)
    sleep(4)
    for a in range(6):
        klik(539,531)
        sleep(9)
        klik(545,775)
    sleep(2)