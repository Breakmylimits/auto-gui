import pyautogui
pyautogui.FAILSAFE = True
#print(pyautogui.position())

pyautogui.moveTo(479,197,duration=2)
pyautogui.doubleClick(479,197)
pyautogui.typewrite('hi i am bot ')  
pyautogui.moveTo(514,449,duration=2)
pyautogui.doubleClick(514,449)
