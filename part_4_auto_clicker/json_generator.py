from pynput.keyboard import Listener  as KeyboardListener
from pynput.mouse    import Listener  as MouseListener
from pynput.keyboard import Key
import json

def add_json(data):
    with open('data.json', 'w+', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

dane = []

# events = [pressed, click, scrolled, moved]
def on_press(key): 
    if key == Key.esc:
        return False
    data = {"Event": "keyboard_pressed", "key": f"{key}"}
    dane.append(data)

def on_move(x, y): 
    data = {"Event": "mouse_moved", "x": x, "y": y}
    dane.append(data)

def on_click(x, y, button, pressed):
    if pressed:
        data = {"Event": "mouse_clicked", "x": x, "y": y, "button": f"{button}"}
        dane.append(data)

def on_scroll(x, y, dx, dy):
    data = {"Event": "mouse_scrolled", "x": x, "y": y, "dx": dx, "dy": dy}
    dane.append(data)

with MouseListener(on_move = on_move, on_click = on_click, on_scroll = on_scroll) as listener:
    with KeyboardListener(on_press=on_press) as listener:
        listener.join()

add_json(dane)
