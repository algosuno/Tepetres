#!/usr/bin/python3
import soundPlayer as pysounds

sp = pysounds.SoundPlayer(2)
A = pysounds.SoundFactory.get_sine_sound(440, 0.1)
B = pysounds.SoundFactory.get_sine_sound(493.88, 0.1)
C = pysounds.SoundFactory.get_sine_sound(523.25, 0.1)
D = pysounds.SoundFactory.get_sine_sound(587.33, 0.1)
E = pysounds.SoundFactory.get_sine_sound(659.25, 0.1)
G = pysounds.SoundFactory.get_sine_sound(783.99, 0.1)
Gm = pysounds.SoundFactory.get_sine_sound(392.00, 0.1)
Em = pysounds.SoundFactory.get_sine_sound(329.63, 0.1)

tempo = 0.1
sp.play_sounds([B, E], 4 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([B, D], 2 * tempo)
sp.play_sounds([E], 1 * tempo)
sp.play_sounds([D], 1 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 2 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([C, E], 4 * tempo)
sp.play_sounds([B, D], 2 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([B, Em], 2 * tempo)
sp.play_sounds([B, Gm], 2 * tempo)
sp.play_sounds([A, C], 2 * tempo)
sp.play_sounds([B, D], 4 * tempo)
sp.play_sounds([C, E], 4 * tempo)
sp.play_sounds([A, C], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)
sp.play_sounds([A, Em], 4 * tempo)

sp.close()
