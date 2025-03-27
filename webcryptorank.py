from template import *
import pyautogui as pg

link("https://cryptorank.io/earn")
tunggugambar("one/cryptorank.png")
pg.scroll(-2)
sleep(0.5)
# ambil koordinat gambar
x,y = koorgambar("one/cryptorank.png")
pg.mouseDown(68,378)
pg.moveTo(x+5, y, 1)
pg.mouseUp()
sleep(2)
pg.scroll(3)
klik(1024,238)
sleep(1)
teks = ambil_teks(752,359, 830,410)
kirim_tele(f"Crypto Rank: {teks} balance")