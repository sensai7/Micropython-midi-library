# generic midi send program
from machine import Pin
import midi
import time

MIDI_TX = Pin(8)  # Optocoupled MIDI input in general purpose pin 8 (UART1TX)
MIDI_RX = Pin(9)  # MIDI output in general purpose pin 9 (UART1RX)
led = Pin(25, Pin.OUT)

my_midi = midi.Midi(1, tx=MIDI_TX, rx=MIDI_RX)

led.on()
my_midi.send_note_on(midi.CHANNEL[1], midi.NOTE_CODE["C#4"], velocity=100)
led.off()
time.sleep(1)

# there seems to be a "ghost" message received when initialized. Read it and forget
# if my_midi.any() > 0:
#     my_midi.read(1)

while True:
    while my_midi.any() > 0:
        byte = my_midi.read(1)
        print(hex(byte[0]))
        my_midi.load_message(byte)

        if my_midi.last_sequence == midi.MIDI_SEQUENCE["NOTE_ON"]:
            channel = my_midi.channel
            note = my_midi.get_parameter("note_on", "note")
            velocity = my_midi.get_parameter("note_on", "velocity")
            # do something with these parameters
            led.on()

        if my_midi.last_sequence == midi.MIDI_SEQUENCE["NOTE_OFF"]:
            channel = my_midi.channel
            note = my_midi.get_parameter("note_off", "note")
            # do something with this parameter
            led.off()
