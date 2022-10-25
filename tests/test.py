#!/usr/bin/env python3
"""PyAudio Example: Play a WAVE file."""

import pyaudio
import wave
import sys

CHUNK = 1024

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

p = pyaudio.PyAudio()
print(p.get_default_output_device_info(), wf.getsampwidth(), wf.getnchannels(), wf.getframerate())

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != b'':
    stream.write(data)
    data = wf.readframes(CHUNK)


stream.stop_stream()
stream.close()

p.terminate()

def stream_text(text: str):
    import pyttsx3
    import uuid
    import sounddevice as sd
    import soundfile as sf
    from sanitize_filename import sanitize
    import time

    filename = sanitize(text + ".wav").replace(" ", '_')
    print(filename)

    engine = pyttsx3.init()
    engine.save_to_file(text=text, filename=filename)
    engine.runAndWait()
    data, fs = sf.read(filename, always_2d=True)
    sd.play(data, fs, device=32)    
    sd.wait()



# stream_text("hello there")

