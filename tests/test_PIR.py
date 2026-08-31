"""
Confirms the sensor is wired correctly and gpiozero can detect motion.
"""

from gpiozero import MotionSensor
from signal import pause

GPIO_PIN = 17

pir = MotionSensor(GPIO_PIN)


def motion_detected():
    print("Motion detected!")


def motion_stopped():
    print("Motion stopped.")


pir.when_motion = motion_detected
pir.when_no_motion = motion_stopped

print(f"Watching GPIO{GPIO_PIN} for motion... (Ctrl+C to quit)")
pause()  # keeps the script running, waiting for GPIO interrupts
