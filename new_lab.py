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
	print(new_tasklist)
	if my_pid != None and my_pid == new_tasklist[0]:
		for i in range(3):
			new_tasklist.pop(0)
		print(new_tasklist)
	return new_tasklist


def first_time():
	first_time = True
	if first_time == True:
		sys("C:\\Users\\yaret\\PycharmProjects\\auto_login\\auto_login.bat")


def main():
	def press(keys):
		hotkeys.press(listener.canonical(keys))


	def not_press(keys):
		hotkeys.release(listener.canonical(keys))


	def launcher():
		new_tasklist = getting_pid(my_pid, forbidden)
		pid = new_tasklist[0]
		sys('taskkill /pid {} /f'.format(pid))
		sys("C:\\Users\\yaret\\PycharmProjects\\auto_login\\auto_login.bat")


	combination_keys = kb.HotKey.parse('<ctrl>+<shift>+ñ')
	hotkeys = kb.HotKey(combination_keys, launcher)

	with kb.Listener(press, not_press) as listener:
		listener.run()


if __name__ == "__main__":
	new_tasklist = getting_pid(my_pid, forbidden)
	my_pid = new_tasklist[0]
	main()