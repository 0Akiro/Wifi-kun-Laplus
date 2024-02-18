import time
import subprocess
import pygame 

pygame.mixer.init()

wifi_kun = 'wifi-kun.mp3'

def check_connectivity(hostname="8.8.8.8"):
    response = subprocess.call(["ping", "-n", "1", hostname], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return response == 0

def play_mp3(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)

try:
    while True:
        if not check_connectivity():
            play_mp3(wifi_kun)
            time.sleep(10)
        else:
            time.sleep(5)
except KeyboardInterrupt:
    pygame.quit()
