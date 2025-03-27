import subprocess
import time

def get_mouse_position():
    # Jalankan perintah xdotool getmouselocation
    result = subprocess.run(['xdotool', 'getmouselocation'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8').strip()

    # Pisahkan output untuk mendapatkan nilai x dan y
    position = output.split()
    x = int(position[0].split(':')[1])
    y = int(position[1].split(':')[1])

    return x, y

def copy_to_clipboard(text):
    # Menyalin teks ke clipboard menggunakan xclip
    subprocess.run(['xclip', '-selection', 'clipboard'], input=text.encode())

# Ambil posisi mouse
x, y = get_mouse_position()

# Format koordinat dalam bentuk string
coordinates = f'klik({x},{y})'

# Tampilkan posisi mouse
print(coordinates)

# Salin koordinat ke clipboard
copy_to_clipboard(coordinates)
print('Koordinat telah disalin ke clipboard.')
