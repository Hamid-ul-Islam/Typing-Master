from PIL import Image
import pytesseract as tess
import pyautogui
import time
import re
import random

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pyautogui.click(1670, 10, interval=0.4)
# start_time = time.time()
it = 0
while True:
    # duration = (time.time() - start_time)
    it +=1
    #! for normal test
    pyautogui.screenshot('image.png', region=(300, 330, 1200, 80))

    #! for competition
    # pyautogui.screenshot('image.png', region=(320, 285, 1060, 60))

    img = Image.open('image.png')
    text = tess.image_to_string(img)

    list = re.findall(r'\w+', text)
    result = len(list)

    if len(text) < 40:
        exit()

    #!Error
    if it==3:
        for i in range(0, result):
            word = random.choice(list)
            pyautogui.write(word, 0.07)
            pyautogui.press('space')
            text = ''



    #! for normal typing
    pyautogui.screenshot('image.png', region=(300, 330, 1200, 80))

    #! for competition
    # pyautogui.screenshot('image.png', region=(320, 285, 1060, 60))

    #!Writer. typing speed (0.06 == 165 and 0.045==210,  0.06 - 0.07is recommended)
    img = Image.open('image.png')
    text = tess.image_to_string(img)
    pyautogui.write(text, 0.09)
    pyautogui.press('space')
