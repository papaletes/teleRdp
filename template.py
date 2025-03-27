import pyautogui as pg
from time import sleep
import os, mss, pytesseract, mss.tools, requests
from PIL import Image


def switchgame(link):
    for a in range(20): #kasi limit
        # Cek apakah "search.png" ada
        if cekgambar("one/search.png"):
            klik(196,257)
            sleep(1)
            pg.typewrite(link)  # Ketik URL
            sleep(1)
            pg.press("enter")  # Tekan Enter
            sleep(1)
            klik(592,773)
            sleep(1)
            pg.press("f6")
            sleep(0.5)
            pg.write("javascript:Object.assign(document.querySelector('#portals > div > div > div > div.modal-dialog').style, {left: '0px', top: '0px', maxWidth: '1072px', maxHeight: '789px'});", 0.08)
            sleep(1)
            pg.press("enter")
            break
        
        # Jika "search.png" tidak ada, klik (0, 0)
        klik(30,138)
        print("kembali")

        # Tunggu 2 detik
        sleep(2)

        # Cek apakah "confirmout.png" ada
        if cekgambar("one/closeanyway.png"):
            klikgambar("one/closeanyway.png")

def koorgambar(gambar, con=0.78):
    try:
        x, y = pg.locateCenterOnScreen(gambar, confidence=con)
        return x, y
    except Exception as e:
        print(e)

def tunggugambar(gambar_path, timeout=30, con=0.78):
    '''return koordinat tengah gambar'''
    timev = 0
    while True:
        try:
            lokasi = pg.locateOnScreen(gambar_path, confidence=con)
            
            if lokasi is not None:
                return pg.center(lokasi)  # Mengembalikan titik tengah gambar
        except Exception as e:
            pass
        # Cek apakah waktu timeout sudah terlewati
        if timev >= timeout:
            print(f"limit {timeout} gambar {gambar_path}")
            return None
        
        # Tunggu sebentar sebelum mencoba lagi
        sleep(1)
        timev += 1

def klikgambar(image_path, con=0.78):
    """Klik otomatis jika gambar ditemukan."""
    location = pg.locateCenterOnScreen(image_path, confidence=con)
    if location:
        pg.click(location)
        sleep(0.2)
        return True
    return False

def cekgambar(image_path, confidence=0.78):
    try:
        return bool(pg.locateOnScreen(image_path, confidence=confidence))
    except Exception as e:
        print(f"Gk nemu {image_path} - false {e}")
        return False

def tungguklik(image_path, timeout=30, click_offset=(0, 0)):
    """Menunggu hingga gambar muncul, lalu klik gambar tersebut."""
    location = tunggugambar(image_path, timeout)
    if location:
        x, y = location
        pg.click(x + click_offset[0], y + click_offset[1])
        return True
    return False

def tunggupixel(x,y,color, toler=5, limit=20):
    for a in range(limit):
        sleep(1)
        if pg.pixelMatchesColor(x,y,color, toler):
            print("pixel sama")
            return True
    print("pixel timeout")
    return False

def klik(x, y):
    pg.click(x, y)
    sleep(0.3)

# ambil teks di box tertentu di layar
def ambil_teks(x, y, width, height):
    with mss.mss() as sct:
        region = {"top": y, "left": x, "width": width-x, "height": height-y}
        screenshot = sct.grab(region)
        # Konversi ke PIL Image
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        # Gunakan pytesseract untuk OCR
        text = pytesseract.image_to_string(img)
    return text.strip()

# kirim pesan pake telebot
def kirim_tele(message, bot_token="8121568956:AAHfqyI2itEp1DMFnqCHR3ZEhWc0Oi1r0AE"):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": "6184426572",
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    
    return response.json()["ok"]
    
def link(link):
    pg.press("f6")
    sleep(0.5)
    pg.write(link)
    pg.press("enter")
