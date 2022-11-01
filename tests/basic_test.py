from __future__ import print_function

import os
import uuid

import pyttsx3


class TextToFrequency:

    def __init__(self, engine: pyttsx3.Engine):
        self.engine = engine


    def text_to_wav(self, text: str) -> str:
        filename = str(uuid.uuid4()) + ".wav"
        self.engine.save_to_file(text, filename)
        self.engine.runAndWait()
        return os.path.abspath(filename)


    def display_wav_freq(self, filename: str):
        import numpy as np
        import scipy
        import scipy.fftpack
        import scipy.io.wavfile as wavfile
        from matplotlib import pyplot as plt

        fs_rate, signal = wavfile.read(filename)
        print ("Frequency sampling", fs_rate)
        l_audio = len(signal.shape)
        print ("Channels", l_audio)
        if l_audio == 2:
            signal = signal.sum(axis=1) / 2
        N = signal.shape[0]
        print ("Complete Samplings N", N)
        secs = N / int(fs_rate)
        print ("secs", secs)
        Ts = 1.0/fs_rate # sampling interval in time
        print ("Timestep between samples Ts", Ts)
        t = np.arange(0, secs, Ts) # time vector as scipy arange field / numpy.ndarray
        FFT = abs(scipy.fftpack.fft(signal))
        FFT_side = FFT[range(N//2)] # one side FFT range
        freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
        fft_freqs = np.array(freqs)
        freqs_side = freqs[range(N//2)] # one side frequency range
        fft_freqs_side = np.array(freqs_side)
        plt.subplot(311)
        p1 = plt.plot(t, signal, "g") # plotting the signal
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.subplot(312)
        print(list(FFT))
        p2 = plt.plot(freqs, FFT, "r") # plotting the complete fft spectrum
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Count dbl-sided')
        plt.subplot(313)
        p3 = plt.plot(freqs_side, abs(FFT_side), "b") # plotting the positive fft spectrum
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Count single-sided')
        plt.show()

    def wav_to_freq_amp(self, filename: str):
        import scipy.io.wavfile as wavfile
        import numpy as np
        import matplotlib.pyplot as plt
        sampFreq, sound = wavfile.read(filename)
        length_in_s = sound.shape[0] / sampFreq
        sound = sound / 2.0**15
        time = np.arange(sound.shape[0]) / sound.shape[0] * length_in_s
        signal = sound
        plt.plot(time, signal)
        plt.xlabel("time, s")
        plt.ylabel("Signal, relative units")
        plt.show()


    


if __name__ == "__main__":
    test = TextToFrequency(pyttsx3.init())
    fname = test.text_to_wav("workin")

    import time
    time.sleep(0.5)

    test.wav_to_freq_amp(fname)

