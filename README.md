# Neural-Data-Analysis-Tool

This Python script provides a way to perform a spectral analysis of EEG data using Python. The script reads EDF (European Data Format) files, applies band-pass filters to the raw data, computes the power spectral density (PSD) for each frequency band, and plots the result.

## Requirements

- Python 3.6 or higher
- [mne](https://mne.tools/stable/install/mne_python.html)
- [numpy](https://numpy.org/install/)
- [plotly](https://plotly.com/python/getting-started/)

## Overview

The script works by first defining the properties of a band-pass filter, including the Delta, Theta, Alpha, Beta, and Gamma bands. It then loads all EDF files from the current directory and applies the band-pass filter to each file's raw data.

For each band in each file, the script computes the power spectral density (PSD) using Welch's method. The PSD values are then averaged across channels and plotted on a graph. 

## How to Use

1. Ensure you have all the necessary Python libraries installed.
2. Place the script in the directory where your EDF files are located.
3. Run the script. 

The output will be a series of interactive plots, one for each EDF file in the directory. Each plot will display the averaged PSD values for each frequency band.

## Output

For each EDF file in the directory, a plot is displayed showing the Power Spectral Density (PSD) per frequency band. The x-axis represents the frequency (in Hz), and the y-axis represents the Power Spectral Density (in dB).

The plot title indicates the specific EDF file for which the PSDs were calculated. 

**Note:** This script processes all EDF files in the current directory. Ensure the directory contains only the EDF files you want to process.

## Disclaimer

This script is intended for EEG data processing and visualization. Please use it responsibly and ensure data privacy.
## Acknowledgments

- The MNE Python project for providing the powerful tools for EEG data processing.
- The creators of numpy and plotly for making the calculations and visualizations possible.
