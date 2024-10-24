import pygame
import mutagen
from mutagen.mp3 import MP3
import time

# Inicializa o mixer
pygame.mixer.init()

# Carrega a música
pygame.mixer.music.load("musica.mp3")

# Função para obter a duração da música usando mutagen
def get_music_length(filename):
    audio = MP3(filename)
    return audio.info.length

# Carrega a duração da música
music_length = get_music_length("musica.mp3")

# Toca a música
pygame.mixer.music.play()

# Exemplo de barra de progresso (simples)
while pygame.mixer.music.get_busy():
    current_pos = pygame.mixer.music.get_pos() / 1000  # Em segundos
    print(f"Tempo atual: {current_pos:.2f}s / {music_length:.2f}s", end='\r')
    time.sleep(1)  # Atualiza a cada 1 segundo