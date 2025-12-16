import board
import digitalio
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.direct_pins = (
    board.GP1,  
    board.GP2,  
    board.GP3,  
    board.GP4,  
    board.GP5,  
    board.GP6,  
)

keyboard.coord_mapping = (0, 1, 2, 3, 4, 5)

LED_PIN = board.GP11

led = digitalio.DigitalInOut(LED_PIN)
led.direction = digitalio.Direction.OUTPUT
led.value = False 

def led_on(*args):
    led.value = True


encoder = EncoderHandler()
keyboard.modules.append(encoder)

encoder.pins = (
    (board.GP8, board.GP9),  
)

encoder.map = [
    ((KC.VOLD, KC.VOLU),),  
]

# Encoder push button
keyboard.encoder_switch = board.GP7
keyboard.encoder_switch_map = [KC.MUTE]

encoder.on_move = led_on


keyboard.keymap = [
    [
        KC.LCTL(KC.B),              
        KC.LCTL(KC.I),              
        KC.LCTL(KC.LALT(KC.H)),     
        KC.LCTL(KC.TAB),            
        KC.LGUI(KC.LSFT(KC.S)),     
        KC.LGUI(KC.X), KC.U, KC.S   
    ]
]


for key in keyboard.keymap[0]:
    key.after_press_handler(led_on)

keyboard.encoder_switch.after_press_handler(led_on)


if __name__ == "__main__":
    keyboard.go()
