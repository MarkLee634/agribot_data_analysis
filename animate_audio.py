import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from pydub import AudioSegment
from pydub.playback import play
import threading
import time
from datetime import timedelta

from numpy import load 
from scipy import signal

import librosa
import librosa.display
import librosa.core
import sys


# load path
path = "/home/marklee/IAM/vibration_project/umass/audio/umass1_audio/leaf1.wav"
leaf_npy, fs = librosa.load(path, mono=False)
xMax = leaf_npy.shape[1]
yMax = np.max(leaf_npy)
yMin = np.min(leaf_npy)

leaf_sound = AudioSegment.from_file(path)
sampling_rate = leaf_sound.frame_rate
song_length = leaf_sound.duration_seconds

# Setup a separate thread to play the music
music_thread = threading.Thread(target=play, args=(leaf_sound,))

# Build the figure
fig = plt.figure(figsize=(14, 6))
fig.suptitle('Audio Plot')
plt.style.use('seaborn-bright')
ax = plt.axes(xlim=[0, xMax], ylim=[yMin,yMax])

line1 = ax.axvline(0, ls='-', color='r', lw=1, zorder=10)
librosa.display.waveplot(leaf_npy[0],sr=fs)



# Matplotlib function to initialize animation
def init():
    global annotation1
    annotation1 = plt.annotate("Time: {}".format(""), xy=(0.2, 0.8), xycoords='figure fraction')
    return line1,


## ==================== animate ==================== \
def animate(i, vl, period):
    global music_start, annotation1

    if i == 0:
        music_thread.start()
        music_start = time.perf_counter()

    annotation1.set_text("Time: {}".format(timedelta(seconds=(time.perf_counter() - music_start))))

    t = i*period/1000
    line1.set_xdata([t,t])

    if i == int(song_length/0.1)-1:
        print(f"COMPLETED. EXIT")
        sys.exit()

    return line1,


refresh_period = 100
anim = animation.FuncAnimation(fig, animate, init_func=init, frames = int(song_length/0.1), fargs = (line1,refresh_period), interval=refresh_period)
plt.show()



