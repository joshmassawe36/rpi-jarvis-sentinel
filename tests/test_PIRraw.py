"""
Raw GPIO polling test - prints the live HIGH/LOW state of GPIO17 every
second. Use this to sanity check wiring before trusting gpiozero's
motion events.

If OUT is wired correctly:
    - No motion: should read LOW (0) most of the time
    - Motion:    should flip to HIGH (1) while triggered

If it's stuck at 1 (always HIGH) or always 0 no matter what you do,
that points to a wiring issue rather than a sensitivity issue.
"""

from gpiozero import DigitalInputDevice
from time import sleep

GPIO_PIN = 17

sensor = DigitalInputDevice(GPIO_PIN)

print(f"Polling GPIO{GPIO_PIN} raw state every second (Ctrl+C to quit)...")
while True:
    print(f"GPIO{GPIO_PIN} state: {sensor.value}")
    sleep(1)

