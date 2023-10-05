from os import system as sys
from pynput import keyboard as kb

my_pid = None
forbidden = ['pythonw.exe', 'Console', 'KB\n', 'KB\npythonw.exe']

def getting_pid(my_pid, forbidden):
    sys('tasklist | findstr "pythonw" > C:\\temp\\auto_login.txt')
    tasklist = open("C:\\temp\\auto_login.txt")
    tasklist = tasklist.read()
    tasklist = tasklist.split(' ')
    new_tasklist = []
    for i in tasklist:
        if i != '' and i not in forbidden:
            new_tasklist.append(i)
    if my_pid != None and my_pid == new_tasklist[0]:
        for i in range(3):
            new_tasklist.pop(0)
    return new_tasklist


def first_time():
    sys("C:\\Users\\yaret\\PycharmProjects\\auto_login\\auto_login.bat")


def main():

    def cleaner():
        new_tasklist = getting_pid(my_pid, forbidden)
        pids = []
        counter = 0
        for element in new_tasklist:
            if counter % 3:
                pass
            else:
                pids.append(element)
            counter += 1
        for pid in pids:
            sys('taskkill /pid {} /f'.format(pid))

    def launcher():
        cleaner()
        sys("C:\\Users\\yaret\\PycharmProjects\\auto_login\\auto_login.bat")


    def stop():
        cleaner()
        sys("C:\\Users\\yaret\\PycharmProjects\\auto_login\\stop.bat")

    hotkeys = {'<ctrl>+<shift>+ñ': launcher,
               '<ctrl>+<shift>+l': stop}


    with kb.GlobalHotKeys(hotkeys) as listener:
        listener.run()


if __name__ == "__main__":
    first_time()
    new_tasklist = getting_pid(my_pid, forbidden)
    my_pid = new_tasklist[0]
    main()