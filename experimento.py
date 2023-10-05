from time import sleep as sp
from time import time as tm
from multiprocessing import Process
from pynput import keyboard as kb

first_time = True
future_time = tm() + 1

def chronometer():
    global future_time
    while tm() < future_time:
        sp(0.1)
        pass
    print('Se ajustó el tiempo')
    future_time = tm() + 1
    chronometer()

def main():

    def press(keys):
        hotkeys.press(listener.canonical(keys))


    def not_press(keys):
        hotkeys.release(listener.canonical(keys))


    def launcher():
        global future_time
        future_time = tm()
        print('<ctrl>+<shift>+ñ')


    combination_keys = kb.HotKey.parse('<ctrl>+<shift>+ñ')
    hotkeys = kb.HotKey(combination_keys, launcher)

    with kb.Listener(press, not_press) as listener:
        listener.run()



if __name__ == "__main__":
    main = Process(target=main)
    chronometer = Process(target=chronometer)

    main.start()
    chronometer.start()







