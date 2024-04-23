# Neural Data Analysis

This script analyzes EEG data from `.edf` files, performs frequency analysis using Morlet wavelets, and visualizes the average power of different brainwave bands over time in an interactive HTML output.

## Requirements

- Python 3.8+
- Libraries: `os`, `numpy`, `pandas`, `mne`, `plotly`

## Usage

1. Place the script in the directory containing your `.edf` files.
2. Run the script using Python:
   ```bash
   python edfgraph.py
   ```
3. View the generated HTML file (`<filename>_power_over_time.html`) for interactive visualizations of EEG data.

## Output

The script will generate an HTML file with interactive line graphs representing the power over time for each of the following frequency bands:

- Delta (0.5-4 Hz)
- Theta (4-8 Hz)
- Alpha (8-12 Hz)
- Beta (12-30 Hz)
- Gamma (30-45 Hz)

You can zoom and pan through each graph for detailed inspection.

example edf scan >> https://www.teuniz.net/edf_bdf_testfiles/
