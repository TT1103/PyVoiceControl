import pyautogui

def Move(x,y):
    xSize,ySize = pyautogui.size()
    
    if x<0 or y<0 or x>xSize or y>ySize:
        return False
    pyautogui.moveTo(x,y)
    
    
    
def Click():
    pyautogui.click()
    
def DoubleClick():
    pyautogui.doubleClick()
    
def MoveAndClick(x,y):
    if Move(x,y):
        
def ScrollUp():
    pyautogui.scroll(2)
        
def ScrollDown():
    pyautogui.scroll(-2)