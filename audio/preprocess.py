import numpy as np
from pydub import AudioSegment



class Properties():
    """
    audio properties.

    Args:
        audio (str) : audio file path.

        https://github.com/jiaaro/pydub/blob/master/API.markdown

    """
    def __init__(self, audio):
        self.audio = audio

    def set(self, file, sample_width=None, frame_rate=None, channels=None):
        """
        Set audio propertise and write.

        Args:
            file (str) : path to write.
            sample_width (int) : Audio sample width (in bytes).
            frame_rate (int) : Audio frame rate (in Hz).
            channels (int) : number of channels (1 is Mono, 2 is Stereo).
        """
        signal = AudioSegment.from_file(self.audio)
        if sample_width:
            signal.set_sample_width(sample_width)
        if frame_rate:
            signal.set_frame_rate(frame_rate)
        if channels:
            signal.set_channels(channels)

        signal.export(file)


    def get(self):
        """
        Return dictionary of audio propertise.(sample width, frame rate, channels)
        """
        signal = AudioSegment.from_file(self.audio)
        dict = {}
        dict['sample width'] = signal.sample_width
        dict['frame rate'] = signal.frame_rate
        dict['channels'] = signal.channels

        return dict
