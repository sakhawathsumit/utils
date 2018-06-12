from utils.audio import file

import librosa
import numpy as np
from pydub import AudioSegment


class PitchPerturb():
	"""
	Pitch-shift the waveform by `n_steps` half-steps
	
	Params:
		audio (str) : path of audio file.
		n_steps (float) : how many (fractional) half-steps to shift `y`.

	Returns:
		numpy array of transform audio and sampling rate.
	"""
	def __init__(self, audio, n_steps):
		self.audio = audio
		self.n_steps = n_steps

	def transformAudio(self):
		"""
		Shift audio.
		"""
		y, sr = file.read(self.audio)
		return librosa.effects.pitch_shift(y=y, sr=sr, n_steps=self.n_steps), sr



class TimePerturb():
	"""
	Time-stretch an audio series by a fixed rate.
	
	Params:
		audio (str) : path of audio file.
		rate (float) : Stretch factor.  If `rate > 1`, then the signal is sped up.
					   If `rate < 1`, then the signal is slowed down.
	Returns:
		numpy array of transform audio and sampling rate.
	"""
	def __init__(self, audio, rate):
		self.audio = audio
		self.rate = rate

	def transformAudio(self):
		y, sr = file.read(self.audio)
		return librosa.effects.time_stretch(y=y, rate=self.rate), sr



class VolumePerturb():
	"""
	Change volume.

	Params:
		audio (str) : path of audio file.
		dBFS (float) : gain in dBFS.

	Returns:
		numpy array of transform audio and sampling rate.
	"""
	def __init__(self, audio, dBFS):
		self.dBFS = dBFS
		self.signal = AudioSegment.from_file(audio)
		self.sr = self.signal.frame_rate

	def transformAudio(self):
		self.signal += self.dBFS
		return np.array(self.signal.get_array_of_samples()), self.sr



class NoisePerturb():
	"""
	Noise perturbation.

	Params:
		audio (str) : path of audio file.
		noise (str) : path of noisy audio file.

	Returns:
		numpy array of transform audio and sampling rate.
	"""
	def __init__(self, audio, noise):
		self.audio = audio
		self.noise = noise

	def transformAudio(self):
		audio_y, audio_sr = file.read(self.audio)
		noise_y, noise_sr = file.read(self.noise)
		
		assert len(noise_y) > len(audio_y), 'Noise audio length is smaller than audio length.'
		assert audio_sr == noise_sr, 'Audio and Noise sampling rate is not equal.'
		
		diff = len(noise_y) - len(audio_y)
		trim_start = np.squeeze(np.random.randint(low=0, high=diff, size=1))
		trim_end = trim_start + len(audio_y)
		perturb = noise_y[trim_start : trim_end]

		return audio_y + perturb, audio_sr

