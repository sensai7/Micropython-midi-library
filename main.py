# generic midi send program
from machine import Pin
import midi
import time

MIDI_TX = Pin(8)             # Optocoupled MIDI input in general purpose pin 8 (UART1TX)
MIDI_RX = Pin(9)             # MIDI output in general purpose pin 9 (UART1RX)
led = Pin(25, Pin.OUT)

my_midi = midi.Midi(1, midi.BAUD, tx=MIDI_TX, rx=MIDI_RX)

led.on()
my_midi.send_note_on(midi.CHANNEL[1], midi.NOTE_CODE["C#4"], velocity=100)
led.off()
time.sleep(1)

led.on()
my_midi.send_note_off(midi.CHANNEL[1], midi.NOTE_CODE["C#4"])
led.off()
time.sleep(1)

led.on()
my_midi.send_cc(midi.CHANNEL[1], midi.CONTROL_CHANGE_CODE["MODULATION_WHEEL"], value=80)
led.off()
time.sleep(1)
# ... or other send methods

print("Execution finished.")
