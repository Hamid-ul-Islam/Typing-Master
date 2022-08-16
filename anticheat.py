from PIL import Image
import pytesseract as tess
import pyautogui
import cv2
import numpy as np
import pyautogui
import time
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


pyautogui.click(1670, 10, interval=0.30)

pyautogui.hotkey('tab', 'enter')
time.sleep(2)

pyautogui.screenshot('image.png', region=(450, 350, 900, 220))
time.sleep(0.1)
img = Image.open('image.png')
text = tess.image_to_string(img)
pyautogui.write(text, 0.041)
pyautogui.hotkey('tab', 'enter')

