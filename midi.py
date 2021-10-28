from machine import UART

# generic MIDI macros
BAUD = 31250
FREQUENCY = BAUD

# MIDI message macros
MESSAGE_NOTE_OFF = 0x80
MESSAGE_NOTE_ON = 0x90
MESSAGE_POLYPHONIC_AFTERTOUCH = 0XA0
MESSAGE_CONTROL_CHANGE = 0xB0
MESSAGE_PROGRAM_CHANGE = 0xC0
MESSAGE_CHANNEL_AFTERTOUCH = 0xD0
MESSAGE_PITCH_BEND = 0xE0
MESSAGE_SYSTEM_EXCLUSIVE_START = 0xF0
MESSAGE_MIDI_TIME_CODE_QTR_FRAME = 0xF1
MESSAGE_SONG_POSITION_POINTER = 0xF2
MESSAGE_SONG_SELECT = 0xF3
# 0xF4 and 0xF5 reserved
MESSAGE_TUNE_REQUEST = 0xF6
MESSAGE_SYSTEM_EXCLUSIVE_STOP = 0xF7
MESSAGE_TIMING_CLOCK = 0xF8
# 0xF9 reserved
MESSAGE_START = 0xFA
MESSAGE_CONTINUE = 0xFB
MESSAGE_STOP = 0xFC
# 0xFD reserved
MESSAGE_ACTIVE_SENSING = 0xFE
MESSAGE_SYSTEM_RESET = 0xFF

CHANNEL = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7,
    9: 8,
    10: 9,
    11: 10,
    12: 11,
    13: 12,
    14: 13,
    15: 14,
    16: 15,
}

CONTROL_CHANGE_CODE = {
    0: "BANK_SELECT",
    1: "MODULATION_WHEEL",
    2: "BREATH_CONTROLLER",
    3: "UNDEFINED",
    4: "FOOT_CONTROLLER",
    5: "PORTAMENTO_TIME",
    6: "DATA_ENTRY",
    7: "CHANNEL_VOLUME",
    8: "BALANCE",
    9: "UNDEFINED",
    10: "PAN",
    11: "EXPRESSION_CONTROLLER",
    12: "EFFECT_CONTROL_1",
    13: "EFFECT_CONTROL_2",
    14: "UNDEFINED",
    15: "UNDEFINED",
    16: "GENERAL_PURPOSE_CONTROLLER_1",
    17: "GENERAL_PURPOSE_CONTROLLER_2",
    18: "GENERAL_PURPOSE_CONTROLLER_3",
    19: "GENERAL_PURPOSE_CONTROLLER_4",
    20: "UNDEFINED",
    21: "UNDEFINED",
    22: "UNDEFINED",
    23: "UNDEFINED",
    24: "UNDEFINED",
    25: "UNDEFINED",
    26: "UNDEFINED",
    27: "UNDEFINED",
    28: "UNDEFINED",
    29: "UNDEFINED",
    30: "UNDEFINED",
    31: "UNDEFINED",
    32: "CONTROL_0",
    33: "CONTROL_1",
    34: "CONTROL_2",
    35: "CONTROL_3",
    36: "CONTROL_4",
    37: "CONTROL_5",
    38: "CONTROL_6",
    39: "CONTROL_7",
    40: "CONTROL_8",
    41: "CONTROL_9",
    42: "CONTROL_10",
    43: "CONTROL_11",
    44: "CONTROL_12",
    45: "CONTROL_13",
    46: "CONTROL_14",
    47: "CONTROL_15",
    48: "CONTROL_16",
    49: "CONTROL_17",
    50: "CONTROL_18",
    51: "CONTROL_19",
    52: "CONTROL_20",
    53: "CONTROL_21",
    54: "CONTROL_22",
    55: "CONTROL_23",
    56: "CONTROL_24",
    57: "CONTROL_25",
    58: "CONTROL_26",
    59: "CONTROL_27",
    60: "CONTROL_28",
    61: "CONTROL_29",
    62: "CONTROL_30",
    63: "CONTROL_31",
    64: "DAMPER_PEDAL_ON_OFF",
    65: "PORTAMENTO_ON_OFF",
    66: "SOSTENUTO_ON_OFF",
    67: "SOFT_PEDAL_ON_OFF",
    68: "LEGATO_FOOTSWITCH",
    69: "HOLD_2",
    70: "SOUND_CONTROLLER_1",
    71: "SOUND_CONTROLLER_2",
    72: "SOUND_CONTROLLER_3",
    73: "SOUND_CONTROLLER_4",
    74: "SOUND_CONTROLLER_5",
    75: "SOUND_CONTROLLER_6",
    76: "SOUND_CONTROLLER_7",
    77: "SOUND_CONTROLLER_8",
    78: "SOUND_CONTROLLER_9",
    79: "SOUND_CONTROLLER_10",
    80: "GENERAL_PURPOSE_CONTROLLER_5",
    81: "GENERAL_PURPOSE_CONTROLLER_6",
    82: "GENERAL_PURPOSE_CONTROLLER_7",
    83: "GENERAL_PURPOSE_CONTROLLER_8",
    84: "PORTAMENTO_CONTROL",
    85: "UNDEFINED",
    86: "UNDEFINED",
    87: "UNDEFINED",
    88: "HIGH_RESOLUTION_VELOCITY_PREFIX",
    89: "UNDEFINED",
    90: "UNDEFINED",
    91: "EFFECTS_1_DEPTH",
    92: "EFFECTS_2_DEPTH",
    93: "EFFECTS_3_DEPTH",
    94: "EFFECTS_4_DEPTH",
    95: "EFFECTS_5_DEPTH",
    96: "DATA_INCREMENT",
    97: "DATA_DECREMENT",
    98: "NON_REGISTERED_PARAMETER_NUMBER_LSB",
    99: "NON_REGISTERED_PARAMETER_NUMBER_MSB",
    100: "REGISTERED_PARAMETER_NUMBER_LSB",
    101: "REGISTERED_PARAMETER_NUMBER_MSB",
    102: "UNDEFINED",
    103: "UNDEFINED",
    104: "UNDEFINED",
    105: "UNDEFINED",
    106: "UNDEFINED",
    107: "UNDEFINED",
    108: "UNDEFINED",
    109: "UNDEFINED",
    110: "UNDEFINED",
    111: "UNDEFINED",
    112: "UNDEFINED",
    113: "UNDEFINED",
    114: "UNDEFINED",
    115: "UNDEFINED",
    116: "UNDEFINED",
    117: "UNDEFINED",
    118: "UNDEFINED",
    119: "UNDEFINED",
    120: "ALL_SOUND_OFF",
    121: "RESET_ALL_CONTROLLERS",
    122: "LOCAL_CONTROL_ON_OFF",
    123: "ALL_NOTES_OFF",
    124: "OMNI_MODE_OFF",
    125: "OMNI_MODE_ON",
    126: "MONO_MODE_ON",
    127: "POLY_MODE_ON",
    "BANK_SELECT": 0,
    "MODULATION_WHEEL": 1,
    "BREATH_CONTROLLER": 2,
    "FOOT_CONTROLLER": 4,
    "PORTAMENTO_TIME": 5,
    "DATA_ENTRY": 6,
    "CHANNEL_VOLUME": 7,
    "BALANCE": 8,
    "PAN": 10,
    "EXPRESSION_CONTROLLER": 11,
    "EFFECT_CONTROL_1": 12,
    "EFFECT_CONTROL_2": 13,
    "GENERAL_PURPOSE_CONTROLLER_1": 16,
    "GENERAL_PURPOSE_CONTROLLER_2": 17,
    "GENERAL_PURPOSE_CONTROLLER_3": 18,
    "GENERAL_PURPOSE_CONTROLLER_4": 19,
    "CONTROL_0": 32,
    "CONTROL_1": 33,
    "CONTROL_2": 34,
    "CONTROL_3": 35,
    "CONTROL_4": 36,
    "CONTROL_5": 37,
    "CONTROL_6": 38,
    "CONTROL_7": 39,
    "CONTROL_8": 40,
    "CONTROL_9": 41,
    "CONTROL_10": 42,
    "CONTROL_11": 43,
    "CONTROL_12": 44,
    "CONTROL_13": 45,
    "CONTROL_14": 46,
    "CONTROL_15": 47,
    "CONTROL_16": 48,
    "CONTROL_17": 49,
    "CONTROL_18": 50,
    "CONTROL_19": 51,
    "CONTROL_20": 52,
    "CONTROL_21": 53,
    "CONTROL_22": 54,
    "CONTROL_23": 55,
    "CONTROL_24": 56,
    "CONTROL_25": 57,
    "CONTROL_26": 58,
    "CONTROL_27": 59,
    "CONTROL_28": 60,
    "CONTROL_29": 61,
    "CONTROL_30": 62,
    "CONTROL_31": 63,
    "DAMPER_PEDAL_ON_OFF": 64,
    "PORTAMENTO_ON_OFF": 65,
    "SOSTENUTO_ON_OFF": 66,
    "SOFT_PEDAL_ON_OFF": 67,
    "LEGATO_FOOTSWITCH": 68,
    "HOLD_2": 69,
    "SOUND_CONTROLLER_1": 70,
    "SOUND_CONTROLLER_2": 71,
    "SOUND_CONTROLLER_3": 72,
    "SOUND_CONTROLLER_4": 73,
    "SOUND_CONTROLLER_5": 74,
    "SOUND_CONTROLLER_6": 75,
    "SOUND_CONTROLLER_7": 76,
    "SOUND_CONTROLLER_8": 77,
    "SOUND_CONTROLLER_9": 78,
    "SOUND_CONTROLLER_10": 79,
    "GENERAL_PURPOSE_CONTROLLER_5": 80,
    "GENERAL_PURPOSE_CONTROLLER_6": 81,
    "GENERAL_PURPOSE_CONTROLLER_7": 82,
    "GENERAL_PURPOSE_CONTROLLER_8": 83,
    "PORTAMENTO_CONTROL": 84,
    "HIGH_RESOLUTION_VELOCITY_PREFIX": 88,
    "EFFECTS_1_DEPTH": 91,
    "EFFECTS_2_DEPTH": 92,
    "EFFECTS_3_DEPTH": 93,
    "EFFECTS_4_DEPTH": 94,
    "EFFECTS_5_DEPTH": 95,
    "DATA_INCREMENT": 96,
    "DATA_DECREMENT": 97,
    "NON_REGISTERED_PARAMETER_NUMBER_LSB": 98,
    "NON_REGISTERED_PARAMETER_NUMBER_MSB": 99,
    "REGISTERED_PARAMETER_NUMBER_LSB": 100,
    "REGISTERED_PARAMETER_NUMBER_MSB": 101,
    "ALL_SOUND_OFF": 120,
    "RESET_ALL_CONTROLLERS": 121,
    "LOCAL_CONTROL_ON_OFF": 122,
    "ALL_NOTES_OFF": 123,
    "OMNI_MODE_OFF": 124,
    "OMNI_MODE_ON": 125,
    "MONO_MODE_ON": 126,
    "POLY_MODE_ON": 127,
    "UNDEFINED": [3, 9, 14, 15, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 85, 86, 87, 89, 90, 102,
                  103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119]
}

NOTE_CODE = {
    127: ["G9", 12543.85],
    126: ["F#9", 11839.82],
    125: ["F9", 11175.30],
    124: ["E9", 10548.08],
    123: ["D#9", 9956.06],
    122: ["D9", 9397.27],
    121: ["C#9", 8869.84],
    120: ["C9", 8372.02],
    119: ["B8", 7902.13],
    118: ["A#8", 7458.62],
    117: ["A8", 7040.00],
    116: ["G#8", 6644.88],
    115: ["G8", 6271.93],
    114: ["F#8", 5919.91],
    113: ["F8", 5587.65],
    112: ["E8", 5274.04],
    111: ["D#8", 4978.03],
    110: ["D8", 4698.64],
    109: ["C#8", 4434.92],
    108: ["C8", 4186.01],
    107: ["B7", 3951.07],
    106: ["A#7", 3729.31],
    105: ["A7", 3520.00],
    104: ["G#7", 3322.44],
    103: ["G7", 3135.96],
    102: ["F#7", 2959.96],
    101: ["F7", 2793.83],
    100: ["E7", 2637.02],
    99: ["D#7", 2489.02],
    98: ["D7", 2349.32],
    97: ["C#7", 2217.46],
    96: ["C7", 2093.00],
    95: ["B6", 1975.53],
    94: ["A#6", 1864.66],
    93: ["A6", 1760.00],
    92: ["G#6", 1661.22],
    91: ["G6", 1567.98],
    90: ["F#6", 1479.98],
    89: ["F6", 1396.91],
    88: ["E6", 1318.51],
    87: ["D#6", 1244.51],
    86: ["D6", 1174.66],
    85: ["C#6", 1108.73],
    84: ["C6", 1046.50],
    83: ["B5", 987.77],
    82: ["A#5", 932.33],
    81: ["A5", 880.00],
    80: ["G#5", 830.61],
    79: ["G5", 783.99],
    78: ["F#5", 739.99],
    77: ["F5", 698.46],
    76: ["E5", 659.26],
    75: ["D#5", 622.25],
    74: ["D5", 587.33],
    73: ["C#5", 554.37],
    72: ["C5", 523.25],
    71: ["B4", 493.88],
    70: ["A#4", 466.16],
    69: ["A4", 440.00],
    68: ["G#4", 415.30],
    67: ["G4", 392.00],
    66: ["F#4", 369.99],
    65: ["F4", 349.23],
    64: ["E4", 329.63],
    63: ["D#4", 311.13],
    62: ["D4", 293.66],
    61: ["C#4", 277.18],
    60: ["C4", 261.63],
    59: ["B3", 246.94],
    58: ["A#3", 233.08],
    57: ["A3", 220.00],
    56: ["G#3", 207.65],
    55: ["G3", 196.00],
    54: ["F#3", 185.00],
    53: ["F3", 174.61],
    52: ["E3", 164.81],
    51: ["D#3", 155.56],
    50: ["D3", 146.83],
    49: ["C#3", 138.59],
    48: ["C3", 130.81],
    47: ["B2", 123.47],
    46: ["A#2", 116.54],
    45: ["A2", 110.00],
    44: ["G#2", 103.83],
    43: ["G2", 98.00],
    42: ["F#2", 92.50],
    41: ["F2", 87.31],
    40: ["E2", 82.41],
    39: ["D#2", 77.78],
    38: ["D2", 73.42],
    37: ["C#2", 69.30],
    36: ["C2", 65.41],
    35: ["B1", 61.74],
    34: ["A#1", 58.27],
    33: ["A1", 55.00],
    32: ["G#1", 51.91],
    31: ["G1", 49.00],
    30: ["F#1", 46.25],
    29: ["F1", 43.65],
    28: ["E1", 41.20],
    27: ["D#1", 38.89],
    26: ["D1", 36.71],
    25: ["C#1", 34.65],
    24: ["C1", 32.70],
    23: ["B0", 30.87],
    22: ["A#0", 29.14],
    21: ["A0", 27.50],
    "G9": 127,
    "F#9": 126,
    "F9": 125,
    "E9": 124,
    "D#9": 123,
    "D9": 122,
    "C#9": 121,
    "C9": 120,
    "B8": 119,
    "A#8": 118,
    "A8": 117,
    "G#8": 116,
    "G8": 115,
    "F#8": 114,
    "F8": 113,
    "E8": 112,
    "D#8": 111,
    "D8": 110,
    "C#8": 109,
    "C8": 108,
    "B7": 107,
    "A#7": 106,
    "A7": 105,
    "G#7": 104,
    "G7": 103,
    "F#7": 102,
    "F7": 101,
    "E7": 100,
    "D#7": 99,
    "D7": 98,
    "C#7": 97,
    "C7": 96,
    "B6": 95,
    "A#6": 94,
    "A6": 93,
    "G#6": 92,
    "G6": 91,
    "F#6": 90,
    "F6": 89,
    "E6": 88,
    "D#6": 87,
    "D6": 86,
    "C#6": 85,
    "C6": 84,
    "B5": 83,
    "A#5": 82,
    "A5": 81,
    "G#5": 80,
    "G5": 79,
    "F#5": 78,
    "F5": 77,
    "E5": 76,
    "D#5": 75,
    "D5": 74,
    "C#5": 73,
    "C5": 72,
    "B4": 71,
    "A#4": 70,
    "A4": 69,
    "G#4": 68,
    "G4": 67,
    "F#4": 66,
    "F4": 65,
    "E4": 64,
    "D#4": 63,
    "D4": 62,
    "C#4": 61,
    "C4": 60,
    "B3": 59,
    "A#3": 58,
    "A3": 57,
    "G#3": 56,
    "G3": 55,
    "F#3": 54,
    "F3": 53,
    "E3": 52,
    "D#3": 51,
    "D3": 50,
    "C#3": 49,
    "C3": 48,
    "B2": 47,
    "A#2": 46,
    "A2": 45,
    "G#2": 44,
    "G2": 43,
    "F#2": 42,
    "F2": 41,
    "E2": 40,
    "D#2": 39,
    "D2": 38,
    "C#2": 37,
    "C2": 36,
    "B1": 35,
    "A#1": 34,
    "A1": 33,
    "G#1": 32,
    "G1": 31,
    "F#1": 30,
    "F1": 29,
    "E1": 28,
    "D#1": 27,
    "D1": 26,
    "C#1": 25,
    "C1": 24,
    "B0": 23,
    "A#0": 22,
    "A0": 21,
}

MIDI_QTR_FRAME_CODE = {
    0: "24 fps",
    1: "25 fps",
    2: "29.97 fps",
    3: "30 fps",
    "24 fps": 0,
    "25 fps": 1,
    "29.97 fps": 2,
    "30 fps": 3,
}

MIDI_SEQUENCE = {
    "NONE": None,
    "NOTE_OFF": 0x80,
    "NOTE_ON": 0x90,
    "POLY_AFTERTOUCH": 0xA0,
    "CONTROL_CHANGE": 0xB0,
    "PROGRAM_CHANGE": 0xC0,
    "CHANNEL_AFTERTOUCH": 0xD0,
    "PITCH_BEND": 0xE0,
    "SYSEX": 0xF0,
    "TIME_CODE_QTR_FRAME": 0xF1,
    "SONG_POSITION_POINTER": 0xF2,
    "SONG_SELECT": 0xF3,
    "TUNE_REQUEST": 0xF6,
    "SYSEX_END": 0xF7,
    "TIMING_CLOCK": 0xF8,
    "START": 0xFA,
    "CONTINUE": 0xFB,
    "STOP": 0xFC,
    "ACTIVE_SENSING": 0xFD,
    "RESET": 0xFF,
}


# Misc. methods ########################################################################################################
def percentage_to_7_bit(percentage: float) -> int:
    return int(percentage / 100 * 127)


# Midi class ###########################################################################################################
# noinspection PyTypeChecker
class Midi:
    def __init__(self, uart, tx, rx):
        self.last_sequence = MIDI_SEQUENCE["NONE"]
        self.message = 0
        self.channel = 0
        self.state = 0
        self.last_rx_parameters = {
            "note_off": {
                "note": None,
            },
            "note_on": {
                "note": None,
                "velocity": None,
            },
            "poly_aftertouch": {
                "note": None,
                "pressure": None,
            },
            "control_change": {
                "code": None,
                "value": None,
            },
            "program_change": {
                "program": None,
            },
            "channel_aftertouch": {
                "pressure": None,
            },
            "pitch_bend": {
                "bend_LSB": None,
                "bend_MSB": None,
                "bend": None,
            },
            "song_position": 0,
            "song_position_pointer": {
                "LSB": None,
                "MSB": None,
                "Position": None,
            },
            "song_select": {
                "song": None,
            },
            "time_code_qtr_frame": {
                "rate": None,
                "hours": None,
                "minutes": None,
                "seconds": None,
                "frames": None,
            },
            "sysex_vendor_id": "",
            "sysex": [],
        }
        print("Starting MIDI...")
        self.uart = UART(uart, BAUD, tx=tx, rx=rx)
        print("Success!\t->OUTPUT  <-INPUT")

    # UART "inherited" methods.  C-based classes don't work when inherited in python ###################################
    def write(self, value: int):
        self.uart.write(bytes([value]))

    def read(self, n_bytes: int):
        return self.uart.read(n_bytes)

    def any(self):
        return self.uart.any()

    # Other ############################################################################################################
    def get_parameter(self, message_type, parameter):
        return self.last_rx_parameters[message_type][parameter]

    # MIDI send methods ################################################################################################
    def send_note_off(self, channel: int, note: int):
        self.write(MESSAGE_NOTE_OFF | channel)
        self.write(note)
        self.write(0)
        print(f"-> NOTE OFF\t\t{note} ({NOTE_CODE[note][0]})")

    def send_note_on(self, channel: int, note: int, velocity: int):
        self.write(MESSAGE_NOTE_ON | channel)
        self.write(note)
        self.write(velocity)
        print(f"-> NOTE ON\t\t{note} ({NOTE_CODE[note][0]})\t\tVELOCITY {velocity}")

    def send_poly_aftertouch(self, channel: int, note: int, pressure: int):
        self.write(MESSAGE_POLYPHONIC_AFTERTOUCH | channel)
        self.write(note)
        self.write(pressure)
        print(f"-> POLY AT\t\t{note} ({NOTE_CODE[note][0]})\t\t\tPRESSURE {pressure}")

    def send_control_change(self, channel: int, cc: int, value: int):
        self.write(MESSAGE_CONTROL_CHANGE | channel)
        self.write(cc)
        self.write(value)
        print(f"-> CONTROL CHANGE\t{cc} ({CONTROL_CHANGE_CODE[cc]})\tVALUE {value}")

    def send_program_change(self, channel: int, program: int):
        self.write(MESSAGE_PROGRAM_CHANGE | channel)
        self.write(program)
        print(f"-> PROGRAM CHANGE\t{channel} TO {program}")

    def send_channel_aftertouch(self, channel: int, amount: int):
        self.write(MESSAGE_CHANNEL_AFTERTOUCH | channel)
        self.write(amount)
        print(f"-> CHANNEL AT\t\tCHANNEL {channel+1}\t\tAMOUNT {amount}")

    def send_pitch_bend(self, channel: int, note: int, amount: int):
        self.write(MESSAGE_PITCH_BEND | channel)
        self.write(note)
        self.write(amount)
        print(f"-> PITCH BEND\t{note} AMOUNT {amount}")

    def send_sysex_start(self):
        self.write(MESSAGE_SYSTEM_EXCLUSIVE_START)
        print(f"-> SYSEX START")

    def send_time_code_qtr_frame(self, rate: int, hours: int, minutes: int, seconds: int, frames: int):
        self.write(MESSAGE_MIDI_TIME_CODE_QTR_FRAME)
        self.write((rate << 5) | hours)
        self.write(minutes)
        self.write(seconds)
        self.write(frames)
        print(f"-> TIME CODE\t\t{hours}:{minutes}:{seconds}.{frames}")

    def send_song_position_pointer(self, beats_since_start: int):
        lsb = beats_since_start & 0x7F
        msb = (beats_since_start >> 7) & 0x7F
        self.write(MESSAGE_SONG_POSITION_POINTER)
        self.write(lsb)
        self.write(msb)
        print(f"-> SONG POSITION\tBEAT {beats_since_start}")

    def send_song_select(self, song: int):
        self.write(MESSAGE_SONG_SELECT)
        self.write(song)
        print(f"-> SONG SELECT\t\tSONG {song}")

    def send_tune_request(self):
        self.write(MESSAGE_TUNE_REQUEST)
        print(f"-> TUNE REQUEST")

    def send_sysex(self, sysex_list: list):
        for item in sysex_list:
            self.write(item)

    def send_sysex_stop(self):
        self.write(MESSAGE_SYSTEM_EXCLUSIVE_STOP)
        print(f"-> SYSEX STOP")

    def send_timing_clock(self):
        self.write(MESSAGE_TIMING_CLOCK)
        print(f"-> TIMING CLOCK")

    def send_playback_start(self):
        self.write(MESSAGE_START)
        print(f"-> PLAYBACK START")

    def send_playback_continue(self):
        self.write(MESSAGE_CONTINUE)
        print(f"-> PLAYBACK CONTINUE")

    def send_playback_stop(self):
        self.write(MESSAGE_STOP)
        print(f"-> PLAYBACK STOP")

    def send_active_sensing(self):
        self.write(MESSAGE_ACTIVE_SENSING)
        print(f"-> ACTIVE SENSING")

    def send_reset(self):
        self.write(MESSAGE_SYSTEM_RESET)
        print(f"-> SYSTEM RESET")

    # MIDI receive methods #############################################################################################
    def load_message(self, msg: int):
        self.message = msg
        self.analyze_message()

    def get_channel(self):
        return self.message & 0x0F

    def analyze_message(self):
        # ANYTHING GOES
        if self.state == 0:
            if self.message < 0xF0:
                self.state = self.message & 0xF0
                self.channel = self.get_channel()
            else:
                self.state = self.message
        # NOTE OFF
        elif self.state == MESSAGE_NOTE_OFF:
            self.last_rx_parameters["note_off"]["note"] = self.message
            self.state = 0x81
        elif self.state == 0x81:
            self.state = 0
            note_code = self.last_rx_parameters["note_off"]["note"]
            note_name = NOTE_CODE[self.last_rx_parameters["note_off"]["note"]][0]
            print(f"<- CH{self.channel+1} NOTE OFF\t\t{note_code} ({note_name})")
            self.last_sequence = MIDI_SEQUENCE["NOTE_OFF"]
        # NOTE ON
        elif self.state == MESSAGE_NOTE_ON:
            self.last_rx_parameters["note_on"]["note"] = self.message
            self.state = 0x91
        elif self.state == 0x91:
            self.last_rx_parameters["note_on"]["velocity"] = self.message
            self.state = 0
            note_code = self.last_rx_parameters["note_on"]["note"]
            note_name = NOTE_CODE[self.last_rx_parameters["note_on"]["note"]][0]
            velocity = self.last_rx_parameters["note_on"]['velocity']
            print(f"<- CH{self.channel+1} NOTE ON\t\t{note_code} ({note_name})\t\t\tVELOCITY {velocity}")
            self.last_sequence = MIDI_SEQUENCE["NOTE_ON"]
        # POLY AFTERTOUCH
        elif self.state == MESSAGE_POLYPHONIC_AFTERTOUCH:
            self.last_rx_parameters["poly_aftertouch"]["note"] = self.message
            self.state = 0xA1
        elif self.state == 0xA1:
            self.last_rx_parameters["poly_aftertouch"]["pressure"] = self.message
            self.state = 0
            note_code = self.last_rx_parameters["poly_aftertouch"]["note"]
            note_name = NOTE_CODE[self.last_rx_parameters["poly_aftertouch"]["note"]][0]
            pressure = self.last_rx_parameters["poly_aftertouch"]["pressure"]
            print(f"<- CH{self.channel+1} POLY AFTERTOUCH\t\t{note_code} ({note_name})\t\tPRESSURE {pressure}")
            self.last_sequence = MIDI_SEQUENCE["POLY_AFTERTOUCH"]
        # CONTROL CHANGE
        elif self.state == MESSAGE_CONTROL_CHANGE:
            self.last_rx_parameters["control_change"]["code"] = self.message
            self.state = 0xB1
        elif self.state == 0xB1:
            self.last_rx_parameters["control_change"]["value"] = self.message
            self.state = 0
            cc_name = CONTROL_CHANGE_CODE[self.last_rx_parameters["control_change"]["code"]]
            cc_code = self.last_rx_parameters["control_change"]["code"]
            value = self.last_rx_parameters["control_change"]["value"]
            print(f"<- CH{self.channel+1} CONTROL CHANGE\t{cc_code} ({cc_name})\tVALUE {value}")
            self.last_sequence = MIDI_SEQUENCE["CONTROL_CHANGE"]
        # PROGRAM CHANGE
        elif self.state == MESSAGE_PROGRAM_CHANGE:
            self.last_rx_parameters["program_change"]["program"] = self.message
            self.state = 0
            program = self.last_rx_parameters["program_change"]["program"]
            print(f"<- CH{self.channel + 1} PROGRAM CHANGE\t{program}")
            self.last_sequence = MIDI_SEQUENCE["PROGRAM_CHANGE"]
        # CHANNEL AFTERTOUCH
        elif self.state == MESSAGE_CHANNEL_AFTERTOUCH:
            self.last_rx_parameters["channel_aftertouch"]["pressure"] = self.message
            self.state = 0
            pressure = self.last_rx_parameters["channel_aftertouch"]["pressure"]
            print(f"<- CH{self.channel + 1} CHANNEL AFTERTOUCH\t\t\tPRESSURE {pressure}")
            self.last_sequence = MIDI_SEQUENCE["CHANNEL_AFTERTOUCH"]
        # PITCH BEND
        elif self.state == MESSAGE_PITCH_BEND:
            self.last_rx_parameters["pitch_bend"]["bend_LSB"] = self.message
            self.state = 0xE1
        elif self.state == 0xE1:
            self.last_rx_parameters["pitch_bend"]["bend_MSB"] = self.message
            bend_msb = self.last_rx_parameters["pitch_bend"]["bend_MSB"]
            bend_lsb = self.last_rx_parameters["pitch_bend"]["bend_LSB"]
            self.state = 0
            self.last_rx_parameters["pitch_bend"]["bend"] = (bend_msb << 8) | bend_lsb
            bend = self.last_rx_parameters["pitch_bend"]["bend"]
            print(f"<- CH{self.channel+1} PITCH BEND\t\tBEND {bend}")
            self.last_sequence = MIDI_SEQUENCE["PITCH_BEND"]
        # START
        elif self.state == MESSAGE_START:
            self.state = 0
            print(f"<- START")
            self.last_sequence = MIDI_SEQUENCE["START"]
        # STOP
        elif self.state == MESSAGE_STOP:
            self.state = 0
            print(f"<- STOP")
            self.last_sequence = MIDI_SEQUENCE["STOP"]
        # CONTINUE
        elif self.state == MESSAGE_CONTINUE:
            self.state = 0
            print(f"<- CONTINUE")
            self.last_sequence = MIDI_SEQUENCE["CONTINUE"]
        # TIMING CLOCK
        elif self.state == MESSAGE_TIMING_CLOCK:
            self.state = 0
            print(f"<- TIMING CLOCK")
            self.last_sequence = MIDI_SEQUENCE["TIMING_CLOCK"]
        # SYSEX START
        elif self.state == MESSAGE_START:
            self.state = 0xF4
            print(f"<- SYSEX START")
            self.last_sequence = MIDI_SEQUENCE["SYSEX"]
            self.last_rx_parameters["sysex_vendor_id"] = self.message
        # SYSEX SEQUENCE
        elif self.state == MESSAGE_SYSTEM_EXCLUSIVE_START:
            if self.message != MESSAGE_SYSTEM_EXCLUSIVE_STOP:
                self.last_rx_parameters["sysex"].append(self.message)
                print(f"<- SYSEX: {hex(self.message)}")
            else:
                self.state = 0
                print(f"<- SYSEX STOP")
                self.last_sequence = MIDI_SEQUENCE["SYSEX_END"]
        # TUNE REQUEST
        elif self.state == MESSAGE_TUNE_REQUEST:
            self.state = 0
            print(f"<- TUNE REQUEST")
            self.last_sequence = MIDI_SEQUENCE["TUNE_REQUEST"]
        # SONG SELECT
        elif self.state == MESSAGE_SONG_SELECT:
            self.last_rx_parameters["song_select"]["song"] = self.message
            self.state = 0
            song = self.last_rx_parameters["song_select"]["song"]
            print(f"<- SONG SELECT\t\t{song}")
            self.last_sequence = MIDI_SEQUENCE["SONG_SELECT"]
        # ACTIVE SENSING
        elif self.state == MESSAGE_ACTIVE_SENSING:
            self.state = 0
            print(f"<- ACTIVE SENSING")
            self.last_sequence = MIDI_SEQUENCE["ACTIVE_SENSING"]
        # SYSTEM RESET
        elif self.state == MESSAGE_SYSTEM_RESET:
            self.state = 0
            print(f"<- SYSTEM RESET")
            self.last_sequence = MIDI_SEQUENCE["SYSTEM_RESET"]
        # MIDI TIME CODE QTR FRAME
        elif self.state == 0xF1:
            self.state = 0xF10
            rate = (0b01100000 | self.message) >> 5
            self.last_rx_parameters["time_code_qtr_frame"]["rate"] = MIDI_QTR_FRAME_CODE[rate]
            hour = (0b00011111 | self.message)
            self.last_rx_parameters["time_code_qtr_frame"]["hour"] = hour
        elif self.state == 0xF10:
            self.state = 0xF11
            minute = self.message
            self.last_rx_parameters["time_code_qtr_frame"]["minute"] = minute
        elif self.state == 0xF11:
            self.state = 0xF12
            second = self.message
            self.last_rx_parameters["time_code_qtr_frame"]["second"] = second
        elif self.state == 0xF12:
            self.state = 0
            frame = self.message
            self.last_rx_parameters["time_code_qtr_frame"]["frame"] = frame
            rate = self.last_rx_parameters["time_code_qtr_frame"]["rate"]
            hour = self.last_rx_parameters["time_code_qtr_frame"]["hour"]
            second = self.last_rx_parameters["time_code_qtr_frame"]["second"]
            minute = self.last_rx_parameters["time_code_qtr_frame"]["minute"]
            print(f"<- TIME CODE QTR FRAME\t{rate}\t{hour}:{minute}:{second}.{frame}")
            self.last_sequence = MIDI_SEQUENCE["TIME_CODE_QTR_FRAME"]
        # SONG POSITION POINTER
        elif self.state == 0xF2:
            self.last_rx_parameters["song_position_pointer"]["LSB"] = self.message
            self.state = 0xF9
        elif self.state == 0xF9:
            self.state = 0
            self.last_rx_parameters["song_position_pointer"]["MSB"] = self.message
            msb = self.last_rx_parameters["song_position_pointer"]["MSB"]
            lsb = self.last_rx_parameters["song_position_pointer"]["LSB"]
            position = (msb << 8) | lsb
            self.last_rx_parameters["song_position_pointer"]["position"] = position
            print(f"<- SONG POSITION POINTER {position}")
            self.last_sequence = MIDI_SEQUENCE["SONG_POSITION_POINTER"]
        # OTHER (THIS SHOULD NEVER HAPPEN)
        else:
            self.state = 0
            print("<- NOT DEFINED")

