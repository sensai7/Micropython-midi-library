# generic midi thru program
from machine import Pin
import midi

MIDI_TX = Pin(8)  # Optocoupled MIDI input in general purpose pin 8 (UART1TX)
MIDI_RX = Pin(9)  # MIDI output in general purpose pin 9 (UART1RX)
led = Pin(25, Pin.OUT)

my_midi = midi.Midi(1, tx=MIDI_TX, rx=MIDI_RX)

while True:
    while my_midi.any() > 0:
        byte = my_midi.read(1)
        my_midi.load_message(byte)
        my_midi.write(my_midi.message)
