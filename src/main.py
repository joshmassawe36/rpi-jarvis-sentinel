from fsm import JarvisFSM, State, Event
from hardware import SimulatedHardware  # swap for RealHardware() later


def run_jarvis_cycle(fsm: JarvisFSM, hardware) -> None:
    fsm.handle_event(Event.MOTION)

    if fsm.state == State.MOTION_DETECTED:
        fsm.handle_event(Event.MOTION_CONFIRMED)

    if fsm.state == State.CAPTURE_IMAGE:
        event = hardware.capture_image()
        fsm.handle_event(event)

    if fsm.state == State.ANALYZE_SCENE:
        event = hardware.analyze_scene()
        fsm.handle_event(event)

    if fsm.state == State.RESPOND:
        event = hardware.respond()
        fsm.handle_event(event)

    if fsm.state == State.COOLDOWN:
        event = hardware.cooldown()
        fsm.handle_event(event)


def main():
    fsm = JarvisFSM()
    hardware = SimulatedHardware()  # swap for RealHardware() later

    print("Jarvis Sentinel")
    print("m = simulate motion")
    print("q = quit")

    while True:
        print(f"\nCurrent state: {fsm.state.name}")
        command = input("Input: ").strip().lower()

        if command == "q":
            break
        if command == "m":
            run_jarvis_cycle(fsm, hardware)


if __name__ == "__main__":
    main()