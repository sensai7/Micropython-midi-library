# generic MIDI to CV/GATE
from machine import Pin, PWM
import midi

MIDI_TX = Pin(8)             # Optocoupled MIDI input in general purpose pin 8 (UART1TX)
MIDI_RX = Pin(9)             # MIDI output in general purpose pin 9 (UART1RX)
GATE = Pin(1)                # Gate out in general purpose pin 8
PWM_NOTE = PWM(Pin(20))      # Note CV PWM out in general purpose pin 20
PWM_VELOCITY = PWM(Pin(21))  # Velocity CV PWM out in general purpose pin 21

my_midi = midi.Midi(1, tx=MIDI_TX, rx=MIDI_RX)
note_balance = 0
PWM_NOTE.freq(10000)
PWM_VELOCITY.freq(10000)

while True:
    if my_midi.any() > 0:
        byte = my_midi.read(1)
        my_midi.load_message(byte)
        if my_midi.last_sequence == midi.MIDI_SEQUENCE["NOTE_ON"]:
            note = my_midi.last_rx_parameters["note_on"]["note"]
            velocity = my_midi.last_rx_parameters["note_on"]["velocity"]
            note_duty = (note - 36) * pow(2, 16) // 60              # Pitch CV 0V~3.3V (C2~C7)
            velocity_duty = (velocity + 1) * pow(2, 9) - 1          # Velocity CV 0V~3.3V
            PWM_NOTE.duty_u16(note_duty)
            PWM_VELOCITY.duty_u16(velocity_duty)
            note_balance += 1
            GATE.high()

        if my_midi.last_sequence == midi.MIDI_SEQUENCE["NOTE_OFF"]:
            note_balance -= 1
            if note_balance == 0:
                GATE.low()
