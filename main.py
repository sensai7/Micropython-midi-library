# generic midi send program
from machine import Pin
import midi
import time

MIDI_TX = Pin(8)  # Optocoupled MIDI input in general purpose pin 8 (UART1TX)
MIDI_RX = Pin(9)  # MIDI output in general purpose pin 9 (UART1RX)
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
my_midi.send_control_change(midi.CHANNEL[1], midi.CONTROL_CHANGE_CODE["MODULATION_WHEEL"], value=80)
led.off()
time.sleep(1)

led.on()
my_midi.send_channel_aftertouch(midi.CHANNEL[1], amount=23)
led.off()
time.sleep(1)

led.on()
my_midi.send_playback_start()
led.off()
time.sleep(1)

led.on()
my_midi.send_playback_continue()
led.off()
time.sleep(1)

led.on()
my_midi.send_playback_stop()
led.off()
time.sleep(1)

led.on()
my_midi.send_sysex_start()
led.off()
time.sleep(1)

led.on()
my_midi.send_sysex([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
led.off()
time.sleep(1)

led.on()
my_midi.send_sysex_stop()
led.off()
time.sleep(1)

led.on()
my_midi.send_poly_aftertouch(midi.CHANNEL[10], midi.NOTE_CODE['C6'], pressure=24)
led.off()
time.sleep(1)

led.on()
my_midi.send_program_change(midi.CHANNEL[3], program=21)
led.off()
time.sleep(1)

led.on()
my_midi.send_timing_clock()
led.off()
time.sleep(1)

led.on()
my_midi.send_tune_request()
led.off()
time.sleep(1)

led.on()
my_midi.send_song_select(10)
led.off()
time.sleep(1)

led.on()
my_midi.send_song_position_pointer(64)
led.off()
time.sleep(1)

led.on()
my_midi.send_time_code_qtr_frame(midi.MIDI_QTR_FRAME_CODE["30 fps"], hours=23, minutes=24, seconds=14, frames=1)
led.off()
time.sleep(1)

led.on()
my_midi.send_active_sensing()
led.off()
time.sleep(1)

led.on()
my_midi.send_reset()
led.off()
time.sleep(1)


print("Execution finished.")
