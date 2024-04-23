import os
import numpy as np
import pandas as pd
import mne
from mne.time_frequency import tfr_morlet
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.io as pio

bands = {
    'Delta': (0.5, 4),
    'Theta': (4, 8),
    'Alpha': (8, 12),
    'Beta': (12, 30),
    'Gamma': (30, 45)
}

current_dir = os.getcwd()

edf_files = [file for file in os.listdir(current_dir) if file.endswith(".edf")]

if not edf_files:
    print("No EDF file found in the current directory.")
    exit()

edf_file = edf_files[0]
print(f"Analyzing EDF file: {edf_file}")

file_path = os.path.join(current_dir, edf_file)
raw = mne.io.read_raw_edf(file_path, preload=True)

sfreq = raw.info['sfreq']
print(f"Sampling Frequency: {sfreq} Hz")
channels = raw.ch_names
print(f"Channels: {', '.join(channels)}")
duration = raw.times[-1]
print(f"Recording Duration: {duration:.2f} seconds")

events = np.array([[0, 0, 0]])
tmax = duration - 1 / sfreq
epochs = mne.Epochs(raw, events, tmin=0, tmax=tmax, baseline=None)

freqs = np.arange(0.5, 45.5, 0.5)
n_cycles = freqs / 2.
power = tfr_morlet(epochs, freqs=freqs, n_cycles=n_cycles, return_itc=False, average=False)

power_data = power.data.mean(axis=1)
times = power.times

fig = sp.make_subplots(rows=len(bands), cols=1, subplot_titles=list(bands.keys()), vertical_spacing=0.02)

for i, (band, (f_min, f_max)) in enumerate(bands.items(), 1):
    band_power = power_data[:, (freqs >= f_min) & (freqs <= f_max), :].mean(axis=1).squeeze()
    fig.add_trace(
        go.Scatter(x=times, y=10 * np.log10(band_power), mode='lines', name=band),
        row=i, col=1
    )

fig.update_layout(
    title=f"Brain Wave Power Over Time - {edf_file}",
    xaxis_title="Time (s)",
    yaxis_title="Power (dB)",
    height=1200,
    template="plotly_white"
)

fig.update_xaxes(matches='x', showspikes=True)
fig.update_yaxes(matches=None, showspikes=True)

output_filename = f"{edf_file}_power_over_time.html"
pio.write_html(fig, file=output_filename, auto_open=False)
print(f"Power over time plot saved as: {output_filename}")
