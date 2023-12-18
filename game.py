import keyboard,pyautogui
CONTROLS_DICT = {"up":"w","down":"s","left":"a","right":"d"}
def move(control):
    """Given a control: move up, down, left, right, execute it
    Possible controls (str): up, down, left, right"""
    pyautogui.press(CONTROLS_DICT[control])

    