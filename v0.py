import os
import numpy as np
import mne
from mne.time_frequency import psd_array_welch
import plotly.graph_objects as go

# Define the band-pass filter properties
bands = {'Delta': (0.5, 4),
         'Theta': (4, 8),
         'Alpha': (8, 15),
         'Beta': (15, 30),
         'Gamma': (30, 45)}

# Get the current directory
current_dir = os.getcwd()

# Get all files in the current directory
files = os.listdir(current_dir)

# Filter EDF files
edf_files = [file for file in files if file.endswith(".edf")]

# Process each EDF file
for edf_file in edf_files:
    # Load the edf file
    file_path = os.path.join(current_dir, edf_file)
    raw = mne.io.read_raw_edf(file_path, preload=True)  # preload data

    # Apply the bandpass filter to the raw data
    raw_filt = {band: raw.copy().filter(l_freq, h_freq) for band, (l_freq, h_freq) in bands.items()}

    # Create plotly graph object
    fig = go.Figure()

    # Iterate over the bands and add to the plot
    for band, raw_band in raw_filt.items():
        # Get the psd for this band
        psd, freqs = psd_array_welch(raw_band.get_data(), raw.info['sfreq'], fmin=0.5, fmax=45.)

        # Average across channels
        psd_mean = psd.mean(axis=0)

        # Add to the plotly figure
        fig.add_trace(go.Scatter(x=freqs, y=10 * np.log10(psd_mean), mode='lines', name=band))

    # Set the title and axis labels
    fig.update_layout(title=f"Power Spectral Density (PSD) per frequency band - {edf_file}",
                      xaxis_title='Frequency (Hz)',
                      yaxis_title='Power Spectral Density (dB)')

    # Display the figure
    fig.show()
