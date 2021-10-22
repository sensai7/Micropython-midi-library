# Micropython-midi-library
 A complete MIDI I/O library for Micropython devices 

To use, simply download the midi.py file and add it to your project. Availability thorugh pip is on the works.

At the current state this library supports all types of MIDI messages via input or output.

Some usage examples are provided in the /examples folder.

## Quick Reference

### Initializing a MIDI instance object

```python
MIDI_TX = Pin(8)             # Optocoupled MIDI input in general purpose pin 8 (UART1TX)
MIDI_RX = Pin(9)             # MIDI output in general purpose pin 9 (UART1RX)
UART_1 = 1
my_midi = midi.Midi(UART_1, tx=MIDI_TX, rx=MIDI_RX)
```

### Sending MIDI messages

```python
my_midi.send_note_on(midi.CHANNEL[1], midi.NOTE_CODE["C#4"], velocity=100)
my_midi.send_note_off(midi.CHANNEL[1], midi.NOTE_CODE["C#4"])
my_midi.send_control_change(midi.CHANNEL[1], midi.CONTROL_CHANGE_CODE["MODULATION_WHEEL"], value=80)
# (...Other send methods)
```

### Receiving MIDI messages
```python
while True:
    if my_midi.any() > 0:
        my_midi.load_message(my_midi.read(1))
        if my_midi.last_sequence == midi.MIDI_SEQUENCE["NOTE_ON"]:
            channel = my_midi.channel
            note = my_midi.get_parameter("note_on", "note")
            velocity = my_midi.get_parameter("note_on", "velocity")
            # do something with these parameters

        if my_midi.last_sequence == midi.MIDI_SEQUENCE["NOTE_OFF"]:
            channel = my_midi.channel
            note = my_midi.get_parameter("note_off", "note")
            # do something with this parameter
            
        # (...Other receive blocks)
```
