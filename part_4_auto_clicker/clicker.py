import json
from pynput.keyboard import Key, KeyCode, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController
import time


keyboard = KeyboardController()
mouse = MouseController()

data = json.load(open('data.json', 'r', encoding='utf-8'))

def keyboard_pressed(**kwargs):
    pass
def mouse_moved(**kwargs):
    x = kwargs["x"]
    y = kwargs["y"]
    mouse.move(x ,y)

def mouse_clicked(**kwargs):
    x = kwargs["x"]
    print(x)
    y = kwargs["y"]
    print(y)
    but = kwargs["button"]
    map_button = {
        "Button.left" : Button.left,
        "Button.right" : Button.right,
        "Button.middle" : Button.middle,
    }
    mouse.position = (x, y)
    mouse.click(map_button[but])

def mouse_scrolled(**kwargs):
    x = kwargs["x"]
    y = kwargs["y"]
    dx = kwargs["dx"]
    dy = kwargs["dy"]
    mouse.position = (x, y)
    mouse.scroll(dx, dy)

print()
action_mapper = {
    "keyboard_pressed" : keyboard_pressed,
    "mouse_clicked" : mouse_clicked,
    "mouse_moved" : mouse_moved,
    "mouse_scrolled" : mouse_scrolled,
}

for i in data:
    action = i.pop("Event")
    print(action)
    kwargs = i
    function = action_mapper[action]
    function(**kwargs)
    time.sleep(0.5)

