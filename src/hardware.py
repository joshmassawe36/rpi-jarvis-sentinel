import time
from abc import ABC, abstractmethod

from fsm import Event
from vision_analysis import analyze_scene as get_scene_description


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


class RealHardware(SentinelHardware):
    
    def __init__(self):
        # Tracks state between steps within one cycle (capture -> analyze -> respond)
        self.last_image_path = None
        self.last_description = None

    def capture_image(self) -> Event:
        print(f"Capturing image...\n")
        time.sleep(1)
        self.last_image_path = "test_image.jpg"  # placeholder until camera arrives
        return Event.CAPTURE_COMPLETE

    def analyze_scene(self) -> Event:
        print(f"Analyzing scene...\n")
        self.last_description = get_scene_description(self.last_image_path)
        time.sleep(1)
        return Event.ANALYSIS_COMPLETE

    def respond(self) -> Event:
        print(f"Jarvis: {self.last_description}\n")
        time.sleep(1)
        return Event.RESPONSE_COMPLETE

    def cooldown(self) -> Event:
        print("Cooling down...")
        time.sleep(2)
        return Event.TIMEOUT
