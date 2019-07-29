from pynput import keyboard

# https://github.com/moses-palmer/pynput/issues/20

def write_to_buffer(key):
    print(key)

def on_press(key):
    write_to_buffer(key)

def on_release(key):
    pass

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

