from template import *
import pyautogui as pg
sleep(4)
# HASIL DARI PAINT HARUS KOTAK dengan koordinat 100,100 ke Ujung
# klo gk sama, bisa pindahin pos window nya
link("https://paint.js.org/")
sleep(2)

pg.mouseDown(267,262)
sleep(5)
pg.moveTo(1158, 262, 0.5)
sleep(5)
pg.moveTo(1158, 836, 0.5)
sleep(5)
pg.moveTo(267, 836, 0.5)
sleep(5)
pg.moveTo(267,262)
pg.mouseUp()
