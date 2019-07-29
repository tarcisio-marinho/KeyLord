from pynput import keyboard
import pynput
# https://github.com/moses-palmer/pynput/issues/20

buffer = []
buffer_size = 0


def write_to_buffer(key, buffer, buffer_size):
    if(buffer_size == 1024 or key == pynput.keyboard.Key.enter):
        buffer.append("\n")
        print(''.join(buffer))
        buffer = []
    else:
        if(key == pynput.keyboard.Key.space):
            buffer.append(" ")
        else:
            buffer.append(str(key).replace("'", ""))

    buffer_size += 1

def on_press(key):
    write_to_buffer(key, buffer, buffer_size)

def on_release(key):
    pass

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

