# Cynboard firmware
import board
import busio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.layers import Layers

COL0 = board.GP9
COL1 = board.GP8
COL2 = board.GP7
COL3 = board.GP6
ROW0 = board.GP3
ROW1 = board.GP2
ROW2 = board.GP1
ROW3 = board.GP0

bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(i2c=bus, device_address=0x3C)

display = Display(
    display=driver,
    width=128,
    height=32,
    dim_time=10,
    dim_target=0.2,
    off_time=1200,
    brightness=0.8
)

display.entries = [
        ImageEntry(image="cynboard.bmp", x=0, y=0),
        # Couldn't find any conclusive way to change this text. Will have to test thing when I get the board
        TextEntry(text='Layer 1', x=128, y=32, x_anchor="B", y_anchor="R"),
]

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

keyboard.extensions.append(display)

keyboard.modules.append(Layers())

keyboard.col_pins = (COL0, COL1, COL2, COL3)
keyboard.row_pins = (ROW0, ROW1, ROW2, ROW3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

FUNNY = KC.MACRO(":3")

midiNoteOctave = 4

def sendMidiNote(noteName: str):
    return KC.MIDI_NOTE(noteName + str(midiNoteOctave), 1)

def increaseMidiNoteOctave():
    global midiNoteOctave
    midiNoteOctave += 1

def decreaseMidiNoteOctave():
    global midiNoteOctave
    midiNoteOctave -= 1

keyboard.keymap = [
    #Normal Keymap
    [
        FUNNY, KC.MEH, KC.RELOAD, KC.TG(1),
        KC.F13, KC.F14, KC.F15, KC.F16,
        KC.F17, KC.F18, KC.F19, KC.F20,
        KC.F21, KC.F22, KC.F23, KC.F24
    ],
    #Midi Keymap
    [
        sendMidiNote("F#"), sendMidiNote("G#"), sendMidiNote("A#"), KC.TRNS,
        sendMidiNote("F"), sendMidiNote("G"), sendMidiNote("A"), sendMidiNote("B"),
        sendMidiNote("C#"), sendMidiNote("D#"), KC.NO, increaseMidiNoteOctave(),
        sendMidiNote("C"), sendMidiNote("D"), sendMidiNote("E"), decreaseMidiNoteOctave(),
    ]
]

if __name__ == '__main__':
    keyboard.go()

