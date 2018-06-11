import numpy as np
import librosa
import soundfile as sf
from pydub import AudioSegment
import python_speech_features




def read(path, sr=16000, format=None):
    """
    Read audio file.

    Args:
    	path (str) : Audio file path.
        sr (int) : sampling rate.
    	format (str) : Audio file format. (eg. 'wav')

    Return:
        y : numpy array.
        sr (int) : sampling rate.

    """
    try:
        y, sr = sf.read(path, samplerate=sr)
    except:
        y, sr = librosa.load(path, sr=sr)
    
    return y, sr


def countDuration(path):
    """
    Read audio file and return duration in seconds.

    Args:
        path (str) : Path of audio file.

    Returns:
        float : Duration of audio file in seconds.
    """
    audio = AudioSegment.from_file(path)
    return audio.duration_seconds


def mfcc(signal, samplerate=16000):
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