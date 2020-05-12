import pyautogui, win32gui, time

i = 1
while i <= 20:
    raid = win32gui.FindWindow(None, r'Raid: Shadow Legends')
    win32gui.SetForegroundWindow(raid)
    time.sleep(1)
    pyautogui.click(1100, 980)
    time.sleep(1)
    #pyautogui.keyDown('altleft')
    #pyautogui.press('tab')
    #pyautogui.keyUp('altleft')
    time.sleep(600)
    print(i)
    i += 1
exit()
