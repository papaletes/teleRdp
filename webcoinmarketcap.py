from template import *
import pyautogui as pg

link("https://coinmarketcap.com/account/my-diamonds/")
# daily
tunggugambar("one/webcmc.png")
a = ambil_teks(351,392, 456,514)
klikgambar("one/webcmc.png")
sleep(2)
kirim_tele(f"Coin Market Cap: {a} dm")