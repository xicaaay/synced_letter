import time
import pygame
# ==========================
# FUNCIÓN TIPO "MÁQUINA DE ESCRIBIR"
# ==========================

def escribir_tipeado(texto, velocidad=0.03):
    for caracter in texto:
        print(caracter, end="", flush=True)
        time.sleep(velocidad)
    print()

# ==========================
# LETRA DE LA CANCIÓN
# ==========================

letra = [
    "I can´t walk away, (oh)",
    "Even though we´re going through it",
    "And it makes you feel alone, (alone)",
    "Just know that I would died for you"
]

# ==========================
# TIEMPOS EN SEGUNDOS
# ==========================

tiempos = [0, 3.2, 6.7, 10.1]

# ==========================
# MOTOR DE KARAOKE
# ==========================
pygame.mixer.init()
pygame.mixer.music.load("mp3/test.mp3")
pygame.mixer.music.play()

inicio = time.time()

for i in range(len(letra)):
    tiempo_objetivo = tiempos[i]

    # esperar hasta el tiempo exacto
    while time.time() - inicio < tiempo_objetivo:
        pass

    # escribir la línea con efecto typing
    escribir_tipeado(letra[i], velocidad=0.03)