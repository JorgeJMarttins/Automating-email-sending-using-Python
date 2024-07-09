class Message():
    
    def acess_browser():
        import pyautogui
        
        pyautogui.PAUSE = 0.5
        pyautogui.press('win')
        pyautogui.write('edge') #browser name
        pyautogui.press('enter')
    
    def login_gmail():
        import pyautogui
        import time
        
        time.sleep(0.5)
        pyautogui.write('gmail.com')
        pyautogui.press('enter')
        pyautogui.press('f11')
        
    def creating_gmail(name, gmail, subject, body):
        import pyautogui
        import time
        
        pyautogui.PAUSE = 0.5
        time.sleep(1)
        pyautogui.click(x=47, y=129)
        time.sleep(0.5)
        pyautogui.write(str(gmail))
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.write(str(subject))
        pyautogui.press("tab")
        time.sleep(0.5)
        pyautogui.write('Hello '+name+',\n\n'+body+' \n\nyour sincerely '+'users name') # You should put the name of the person who sent the email
        pyautogui.press('tab')
        pyautogui.press('enter')
    
    def end_submission():
        import pyautogui
        import time
         
        pyautogui.PAUSE = 0.5
        time.sleep(0.5)
        pyautogui.press('f11')
        pyautogui.click(x=1882, y=16)
        
        