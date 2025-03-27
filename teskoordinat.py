from template import *
import pyautogui as pg

# HASIL DARI PAINT HARUS KOTAK dengan koordinat 100, 300
# klo gk sama, bisa pindahin pos window nya
link("https://paint.js.org/")
sleep(2)

pg.mouseDown(167,239)
sleep(2)
pg.moveTo(367, 239, 0.5)
sleep(2)
pg.moveTo(367, 439, 0.5)
sleep(2)
pg.moveTo(167, 439, 0.5)
sleep(2)
pg.moveTo(167,239)
pg.mouseUp()
