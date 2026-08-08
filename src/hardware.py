import time
from abc import ABC, abstractmethod

from fsm import Event


class SentinelHardware(ABC):
    """
    Interface that any hardware backend (simulated or real) must implement.
    The FSM driver loop only ever talks to this interface, so swapping
    simulated hardware for real Raspberry Pi hardware later requires no
    changes to fsm.py or run_jarvis_cycle().
    """

    @abstractmethod
    def capture_image(self) -> Event:
        ...

    @abstractmethod
    def analyze_scene(self) -> Event:
        ...

    @abstractmethod
    def respond(self) -> Event:
        ...

    @abstractmethod
    def cooldown(self) -> Event:
        ...


class SimulatedHardware(SentinelHardware):
    """Fake hardware backend for development without physical sensors/camera."""

    def capture_image(self) -> Event:
        print("Capturing image...")
        time.sleep(1)
        return Event.CAPTURE_COMPLETE

    def analyze_scene(self) -> Event:
        print("Analyzing scene...")
        time.sleep(1)
        return Event.ANALYSIS_COMPLETE

    def respond(self) -> Event:
        print("Jarvis: Presence detected.")
        time.sleep(1)
        return Event.RESPONSE_COMPLETE

    def cooldown(self) -> Event:
        print("Cooling down...")
        time.sleep(2)
        return Event.TIMEOUT


# --------------------------------------------------------------------------
# Later, on the Raspberry Pi, implement a class like this and swap it in
# wherever SimulatedHardware() is currently instantiated in main.py:
#
# class RealHardware(SentinelHardware):
#     def capture_image(self) -> Event:
#         # e.g. picamera2 capture
#         return Event.CAPTURE_COMPLETE
#
#     def analyze_scene(self) -> Event:
#         # e.g. call a vision/AI API on the captured image
#         return Event.ANALYSIS_COMPLETE
#
#     def respond(self) -> Event:
#         # e.g. text-to-speech or LED/display output
#         return Event.RESPONSE_COMPLETE
#
#     def cooldown(self) -> Event:
#         # e.g. real timer, or wait for PIR sensor to clear
#         return Event.TIMEOUT
# --------------------------------------------------------------------------