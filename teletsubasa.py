#pylint:disable=E0401
from template import *
from time import sleep
import pyautogui as pg

udhdaily = False
wpos = 0

# play
switchgame("https://t.me/TsubasaRivalsBot/start?startapp=inviter_id-6184426572", wpos)
sleep(12)
klik(595+wpos,171)
sleep(2)

# claim
klik(330+wpos,835)
sleep(2)

# upgrade

# daily
klik(432+wpos,859)
sleep(2)
klik(296+wpos,383)
sleep(2)
klik(321+wpos,835)