from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanner import DiodeOrientation
from kmk.extensions.rgb import RGB

kb =KMKKeyboard()

kb.col_pins(0,27,28)
kb.row_pins(1,2,4)

kb.diodeorientation = DiodeOrientation.COL2ROW

kb.keymap =  [
    [
        KC.A , KC.B , KC.C,
        KC.D , KC.E , KC.F,
        KC.G , KC.H , KC.I,
    ]
]

rgb = RGB(
    pixel_pin = 10
    num_pixels = 8
    hue_default = 120
    sat_default = 255
    val_default = 100
)

kb.extensions.append(rgb)

kb.go()