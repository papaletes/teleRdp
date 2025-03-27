from template import *
import pyautogui as pg

link("https://coinmarketcap.com/account/my-diamonds/")
tungguklik("one/coingecko.png")
sleep(2)
a = ambil_teks(116,637, 220,676)
kirim_tele(f"CoinGecko: {a} candy")