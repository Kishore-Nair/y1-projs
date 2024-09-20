import os
import pygame
#used edge-tts
voice2 = 'en-GB-SoniaNeural'
voice = 'en-US-AnaNeural'
def speak(data):
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()

        pygame.mixer.quit()
# speak(f"I am {voice.split('-')[-1].split('Neural')[0]}!")