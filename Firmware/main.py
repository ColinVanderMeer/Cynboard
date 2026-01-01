# Cynboard firmware
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
# from kmk.extensions.display import Display, TextEntry, ImageEntry
# from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.layers import Layers
from kmk.modules.midi import MidiKeys

COL0 = board.D2
COL1 = board.D1
COL2 = board.D7
COL3 = board.D8
ROW0 = board.D6
ROW1 = board.D5
ROW2 = board.D4
ROW3 = board.D3

# bus = busio.I2C(board.D9, board.D10)

# driver = SSD1306(i2c=bus, device_address=0x3C)

# display = Display(
#    display=driver,
#    width=128,
#    height=32,
#    dim_time=10,
#    dim_target=0.2,
#    off_time=1200,
#    brightness=0.8
# )

# display.entries = [
#        ImageEntry(image="cynboard.bmp", x=0, y=0),
#        # Couldn't find any conclusive way to change this text. Will have to test thing when I get the board
#        TextEntry(text='Layer 1', x=128, y=32, x_anchor="B", y_anchor="R"),
# ]

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# keyboard.extensions.append(display)

keyboard.modules.append(Layers())

keyboard.modules.append(MidiKeys())

keyboard.col_pins = (COL0, COL1, COL2, COL3)
keyboard.row_pins = (ROW0, ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

FUNNY = KC.MACRO(":3")

keyboard.keymap = [
    #Normal Keymap
    [
        FUNNY, KC.MEH, KC.RELOAD, KC.TG(1),
        KC.F13, KC.F14, KC.F15, KC.F16,
        KC.F17, KC.F18, KC.F19, KC.F20,
        KC.F21, KC.F22, KC.F23, KC.F24
   ],
    # Midi Keymap
   [
       KC.MIDI_NOTE("F#4", 127), KC.MIDI_NOTE("G#4", 127), KC.MIDI_NOTE("A#4", 127), KC.TRNS,
       KC.MIDI_NOTE("F4", 127), KC.MIDI_NOTE("G4", 127), KC.MIDI_NOTE("A4", 127), KC.MIDI_NOTE("B4", 127),
       KC.MIDI_NOTE("C#4", 127), KC.MIDI_NOTE("D#4", 127), KC.NO, KC.NO,
       KC.MIDI_NOTE("C4", 127), KC.MIDI_NOTE("D4", 127), KC.MIDI_NOTE("E4", 127), KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()

