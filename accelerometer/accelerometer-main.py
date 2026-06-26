from microbit import *
import log

log.set_labels('x', 'y', 'z', timestamp=log.SECONDS)

log.set_mirroring(True)

logging = False

@run_every(ms=100)
def log_data():
    if logging:
        log.add({
            'x': accelerometer.get_x(),
            'y': accelerometer.get_y(),
            'z': accelerometer.get_z()
        })

while True:
    if button_a.was_pressed():
        logging = not logging
        