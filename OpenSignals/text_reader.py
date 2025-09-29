import matplotlib
matplotlib.use("TkAgg")  # Must be before pyplot import

def dummy_enable_gui(*args, **kwargs):
    pass

try:
    import IPython.core.interactiveshell as ipyshell
    ipyshell.InteractiveShell.enable_gui = dummy_enable_gui
except Exception:
    pass

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np
import biosignalsnotebooks as bsnb

print("Matplotlib backend in use:", matplotlib.get_backend())

signal_data = bsnb.load(r"C:\Users\diego\Github\ECG_project\ECG-study\Plux\SampleECG.txt")
ecg_signal = signal_data["CH1"]

window_size = 4000
init_start = 0
signal_len = len(ecg_signal)

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
line, = ax.plot(ecg_signal[init_start:init_start + window_size])
ax.set_ylim(min(ecg_signal), max(ecg_signal))
ax.set_xlim(init_start, init_start + window_size)
ax.set_title("ECG Signal Viewer")

ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Start', 0, signal_len - window_size, valinit=init_start, valstep=1)

def update(val):
    start = int(slider.val)
    line.set_ydata(ecg_signal[start:start + window_size])
    line.set_xdata(np.arange(start, start + window_size))
    ax.set_xlim(start, start + window_size)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()