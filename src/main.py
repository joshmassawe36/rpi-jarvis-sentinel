from fsm import JarvisFSM, State, Event
import time


def simulate_camera_capture():
    print("Capturing image...")
    time.sleep(1)
    return Event.CAPTURE_COMPLETE


def simulate_ai_analysis():
    print("Analyzing scene...")
    time.sleep(1)
    return Event.ANALYSIS_COMPLETE


def simulate_response():
    print("Jarvis: Presence detected.")
    time.sleep(1)
    return Event.RESPONSE_COMPLETE


def simulate_cooldown():
    print("Cooling down...")
    time.sleep(2)
    return Event.TIMEOUT


def run_jarvis_cycle(fsm):
    fsm.handle_event(Event.MOTION)

    if fsm.state == State.MOTION_DETECTED:
        fsm.handle_event(Event.CAPTURE_COMPLETE)

    if fsm.state == State.CAPTURE_IMAGE:
        event = simulate_camera_capture()
        fsm.handle_event(event)

    if fsm.state == State.ANALYZE_SCENE:
        event = simulate_ai_analysis()
        fsm.handle_event(event)

    if fsm.state == State.RESPOND:
        event = simulate_response()
        fsm.handle_event(event)

    if fsm.state == State.COOLDOWN:
        event = simulate_cooldown()
        fsm.handle_event(event)


def main():
    fsm = JarvisFSM()

    print("Jarvis Sentinel")
    print("m = simulate motion")
    print("q = quit")

    while True:
        print(f"\nCurrent state: {fsm.state.name}")
        command = input("Input: ").strip().lower()

        if command == "q":
            break

        if command == "m":
            run_jarvis_cycle(fsm)


if __name__ == "__main__":
    main()