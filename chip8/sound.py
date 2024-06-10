import numpy as np
from scipy import signal
import threading
import pygame
import matplotlib.pyplot as plt
class SquareWavePlayer:
    def __init__(self, frequency, amplitude=0.1, sample_rate=44100):
        pygame.mixer.init(sample_rate, 32, channels=2)
        # Genera los tiempos de las muestras


        # Genera una onda cuadrada
        self.square_wave = signal.square(2 * np.pi * np.arange(sample_rate) * frequency / sample_rate).astype(np.float32)
        self.square_wave=np.column_stack((self.square_wave,self.square_wave))
        self.sample_rate = sample_rate
        self.playing = False
        self.sound=pygame.sndarray.make_sound(self.square_wave)

    def start(self):
        self.playing = True
        self.thread = threading.Thread(target=self._play_in_loop)
        self.thread.daemon = True
        self.thread.start()

    def _play_in_loop(self):
        self.sound.play(-1)

    def stop(self):
        self.playing = False
        try:
            self.sound.stop()
        except Exception as e:
            print(e)
            pass
    def plot_wave(self):
        # Dibuja las primeras 1000 muestras de la onda cuadrada
        plt.plot(self.square_wave[:1000])
        plt.title('Square Wave')
        plt.ylabel('Amplitude')
        plt.show()
        

if __name__ == "__main__":
    player = SquareWavePlayer(440)
    #player.plot_wave()
    player.start()
    input("Press Enter to stop")
    player.stop()
    print("Stopped")
    input("Press Enter to exit")