import os
import numpy as np
import pandas as pd
import mne
from mne.time_frequency import psd_array_welch
import plotly.graph_objects as go
import plotly.io as pio

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

# Create a DataFrame to store average power for each band and each file
avg_power_df = pd.DataFrame(columns=['file'] + list(bands.keys()))

# Process each EDF file
for edf_file in edf_files:
    # Load the edf file
    file_path = os.path.join(current_dir, edf_file)
    raw = mne.io.read_raw_edf(file_path, preload=True)  # preload data

    # Create plotly graph object
    fig = go.Figure()

    avg_power = {'file': edf_file}

    # Iterate over the bands
    for band, (l_freq, h_freq) in bands.items():
        # Apply the bandpass filter to the raw data
        raw_band = raw.copy().filter(l_freq, h_freq)
        # Get the psd for this band
        psd, freqs = psd_array_welch(raw_band.get_data(), raw.info['sfreq'], fmin=l_freq, fmax=h_freq)
        # Average across channels
        psd_mean = psd.mean(axis=0)
        # Calculate average power for the band
        avg_power[band] = 10 * np.log10(psd_mean.mean())

        # Add to the plotly figure
        fig.add_trace(go.Scatter(x=freqs, y=10 * np.log10(psd_mean), mode='lines', name=band))

    # Set the title and axis labels
    fig.update_layout(title=f"Power Spectral Density (PSD) per frequency band - {edf_file}",
                      xaxis_title='Frequency (Hz)',
                      yaxis_title='Power Spectral Density (dB)')

    # Save the figure to a PNG file
    pio.write_image(fig, f"{edf_file}_psd.png")

    # Add the average power to the DataFrame
    avg_power_df = avg_power_df.append(avg_power, ignore_index=True)

# Save the DataFrame to a CSV file
avg_power_df.to_csv('avg_power.csv', index=False)

