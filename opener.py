# buat open chrome berbeda beda profill 
import os
from time import sleep
from template import  *
import pyautogui

idxProfile = 0
profileLocation = [[]]

os.system('chromium --profile-directory="/root/chromium/config/.config/chromium/Default/" --no-sandbox')
sleep(1)
# klik profile location
sleep(2)
pyautogui.typewrite("https://www.web.telegram.com")

# lanjutin pake swtichgame()