import time
import threading
import ctypes
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode


delay = 1
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

ctypes.windll.user32.MessageBoxW(0, "Auto Clicker Running In background\nPress s to Start or Stop and e to exit\n1 click every second", "Auto Clicker", 0)
class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            print("Auto Clicker Stopped")
            click_thread.stop_clicking()
            ctypes.windll.user32.MessageBoxW(0, "Auto Clicker Stopped.", "Auto Clicker", 0)
        else:
            print("Auto Clicker Started")
            ctypes.windll.user32.MessageBoxW(0, "Auto Clicker Started.", "Auto Clicker", 0)
            click_thread.start_clicking()
    elif key == exit_key:
        print("Exiting....")
        ctypes.windll.user32.MessageBoxW(0, "Auto Clicker Exited.", "Auto Clicker", 0)
        click_thread.exit()
        listener.stop()

with Listener(on_press=on_press) as listener:
    listener.join()