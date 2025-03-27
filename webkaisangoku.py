from template import *
import pyautogui as pg

# setiap 8 jam
link("https://quest.kai-sangokushi-taisen.games/en")
tunggugambar("assets/kaisangoku/ingame.png")
# ambil rank
rank = ambil_teks(546,232, 628,248)
kirim_tele(f"KAI Sangoku: {rank}")
# quests 8 jam
sleep(4)
for a in range(3):
    klik(536,711)
    sleep(3.5)
    klikgambar("assets/kaisangoku/enemy.png", 0.70)
    sleep(14)
    if cekgambar("/assets/kaisangoku/ok.png"):
        klikgambar("/assets/kaisangoku/ok.png")

