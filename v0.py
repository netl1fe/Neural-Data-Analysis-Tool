import mne
from mne.preprocessing import ICA
import matplotlib.pyplot as plt

class NeuralDataAnalysisTool:
    def __init__(self, file_path):
        self.raw = mne.io.read_raw_edf(file_path, preload=True)
        
    def visualize_raw_data(self, start=0, duration=10):
        """Visualize the first `duration` seconds of the recording."""
        self.raw.plot(duration=duration, start=start)
        
    def plot_psd(self, fmin=0, fmax=50):
        """Compute and plot the power spectral density (PSD)."""
        self.raw.plot_psd(fmin=fmin, fmax=fmax)
        
    def perform_ica(self, n_components=0.95):
        """
        Perform Independent Component Analysis (ICA) to identify components
        corresponding to eye blinks or other artifacts.
        """
        ica = ICA(n_components=n_components, method='fastica')
        ica.fit(self.raw)
        
        # Plot the independent components
        ica.plot_components(outlines='head', ch_type='eeg')
        
        # Plot properties of the first five independent components
        ica.plot_properties(self.raw, picks=range(5))

# Usage
tool = NeuralDataAnalysisTool('path_to_your_data.edf')
tool.visualize_raw_data()
tool.plot_psd()
tool.perform_ica()
