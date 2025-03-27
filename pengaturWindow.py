import os, time

time.sleep(5)

os.system(f"xdotool getactivewindow windowmove 0 0")
os.system(f"xdotool getactivewindow windowsize 1080 880")
