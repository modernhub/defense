from pynput import mouse, keyboard

def mouse_position() -> tuple:
    "return a mouse coordinate (0 element - coord x, 1 element - coord y)"
    return mouse.Controller().position


def keyboard_event() -> bool:
    with keyboard.Events() as events:
        event = events.get(1)
        if event is None:
            return False
        if event.key.char == '0':
            return True
