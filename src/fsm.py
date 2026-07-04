from enum import Enum, auto


class State(Enum):
    IDLE = auto()
    MOTION_DETECTED = auto()
    CAPTURE_IMAGE = auto()
    ANALYZE_SCENE = auto()
    RESPOND = auto()
    COOLDOWN = auto()


class Event(Enum):
    MOTION = auto()
    CAPTURE_COMPLETE = auto()
    ANALYSIS_COMPLETE = auto()
    RESPONSE_COMPLETE = auto()
    TIMEOUT = auto()


class JarvisFSM:
    def __init__(self):
        self.state = State.IDLE

    def handle_event(self, event):
        old_state = self.state

        if self.state == State.IDLE:
            if event == Event.MOTION:
                self.state = State.MOTION_DETECTED

        elif self.state == State.MOTION_DETECTED:
            self.state = State.CAPTURE_IMAGE

        elif self.state == State.CAPTURE_IMAGE:
            if event == Event.CAPTURE_COMPLETE:
                self.state = State.ANALYZE_SCENE

        elif self.state == State.ANALYZE_SCENE:
            if event == Event.ANALYSIS_COMPLETE:
                self.state = State.RESPOND

        elif self.state == State.RESPOND:
            if event == Event.RESPONSE_COMPLETE:
                self.state = State.COOLDOWN

        elif self.state == State.COOLDOWN:
            if event == Event.TIMEOUT:
                self.state = State.IDLE

        if old_state != self.state:
            print(f"{old_state.name} -> {self.state.name}")
        
        return self.state
    