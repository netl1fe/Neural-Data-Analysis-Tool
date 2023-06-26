# Neural Data Analysis Tool - EEG Spectral Analysis

This Python script offers an efficient method for performing spectral analysis of EEG (Electroencephalography) data. By reading EDF (European Data Format) files, applying band-pass filters, computing the Power Spectral Density (PSD) for each frequency band, and visualizing the results, this tool simplifies the process of EEG data exploration.

## Prerequisites

Ensure that you have:

- Python 3.6 or higher
- [mne](https://mne.tools/stable/install/mne_python.html)
- [numpy](https://numpy.org/install/)
- [plotly](https://plotly.com/python/getting-started/)

## Workflow Overview

The script initiates by specifying the properties of a band-pass filter, focusing on the Delta, Theta, Alpha, Beta, and Gamma bands. Subsequently, it loads all EDF files from the current directory and applies the band-pass filter to the raw data within each file.

Then, for each frequency band in each file, the script calculates the Power Spectral Density (PSD) using Welch's method. The resultant PSD values are averaged across channels and represented graphically. 

## Usage Guidelines

1. Ensure all required Python libraries are installed.
2. Place the script in the directory containing your EDF files.
3. Execute the script. 

The output is a collection of interactive plots, each corresponding to an EDF file in the directory. Each plot presents the averaged PSD values for each frequency band.

## Output Description

Each EDF file yields a plot exhibiting the Power Spectral Density (PSD) per frequency band. The x-axis represents the frequency (in Hz), and the y-axis illustrates the Power Spectral Density (in dB).

The title of the plot specifies the particular EDF file for which the PSDs have been computed. 

**Note:** This script processes all EDF files in the current directory. Ensure that the directory only includes the EDF files intended for processing.

## Caution

This script has been developed for the purposes of EEG data processing and visualization. Please use it responsibly, always ensuring data privacy.

## Acknowledgments

- The MNE Python project for providing robust tools for EEG data processing.
- The creators of numpy and plotly for facilitating precise computations and generating comprehensive visualizations.
