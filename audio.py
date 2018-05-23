import numpy as np
from pydub import AudioSegment
import python_speech_features



class Audio:
    def __init__(self):
        """
        Constructor of Audio class.
        """

    def read(self, path=None, format=None):
    	"""
    	Read audio file.
    	Args:
    		path (str) : Audio file path.
    		format (str) : Audio file format. (eg. 'wav')
    	"""
    	return AudioSegment.from_file(file=path, format=format)

    def countDuration(self, path=None):
        """
        Read audio file and return duration in seconds.

        Args:
            path (str) : Path of audio file.

        Returns:
            float : Duration of audio file in seconds.
        """
        audio = AudioSegment.from_file(path)
        return audio.duration_seconds


    def setProperties(self, signal=None, sample_width=None, frame_rate=None, channels=None):
    	"""
    	Set audio properties.

    	Args:
    		signal (np array) : Loaded audio signal.
    		sample_width (int) : Audio sample width (in bytes).
    		frame_rate (int) : Audio frame rate (in Hz).
    		channels (int) : number of channels (1 is Mono, 2 is Stereo).

    		https://github.com/jiaaro/pydub/blob/master/API.markdown

    	Returns:
    		An equivalent version of signal.

    	"""
    	if sample_width:
    		signal.set_sample_width(sample_width)
    	if frame_rate:
    		signal.set_frame_rate(frame_rate)
    	if channels:
    		signal.set_channels(channels)

    	return signal

    def mfcc(self, signal=None, samplerate=16000):
    	"""
    	Compute MFCC.

    	Args:
    		signal : Audio signal(pydub object).
    		samplerate (int) = sampling rate.

    	Returns:
    		list : 2D array.
    	"""
    	signal = np.array(signal.get_array_of_samples())
    	return python_speech_features.mfcc(signal=signal, samplerate=samplerate)
