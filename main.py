import pyautogui
import time
import pytesseract
import pyscreenshot
from PIL import ImageEnhance, ImageOps
from screeninfo import get_monitors
import random

# Get screen specs
m = get_monitors()
scrnWidth = m[0].width
scrnHeight = m[0].height
stop = False


def getData():
    global stop
    # Get Screenshot
    sc = pyscreenshot.grab(bbox=(int(scrnWidth * .6468), int(scrnHeight * .3666), int(scrnWidth * .6636),
                                 int(scrnHeight * .3861),))
    # Convert to grayscale
    img = ImageOps.grayscale(sc)
    # Increase contrast
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(5)
    # Save image
    # img.save('data2.png')
    # Extract Text from image
    text = pytesseract.image_to_string(img)
    # Clean Text
    text = text.strip("\n")

    print(text)
    # Check for 'Sell' button
    if not 'Sell' in text:
        stop = True
        print("No items or damaged item detected!")



def sellItem():
    # Get random delay
    rng = random.randrange(5, 20, 1) / 1000

    # Get Relative sell button position
    sellX = scrnWidth * .65
    sellY = scrnHeight * .37

    # Move to Sell button and click
    pyautogui.moveTo(sellX, sellY)
    pyautogui.mouseDown(); time.sleep(rng); print(rng)
    rng = random.randrange(5, 20, 1) / 1000
    pyautogui.mouseUp(); time.sleep(rng); print(rng)

    # Get Relative lower price button
    sellX = scrnWidth * .435
    sellY = scrnHeight * .61

    # Click sell button
    pyautogui.moveTo(sellX, sellY)
    # Lower price 3x
    for i in range(2):
        pyautogui.mouseDown()
        pyautogui.mouseUp()

    # Get Relative sell button position
    sellX = scrnWidth * .6
    sellY = scrnHeight * .72

    # Click sell button
    pyautogui.moveTo(sellX, sellY)
    rng = random.randrange(5, 20, 1) / 1000
    pyautogui.mouseDown(); time.sleep(rng); print(rng)
    rng = random.randrange(5, 20, 1) / 1000
    pyautogui.mouseUp(); time.sleep(rng); print(rng)


if __name__ == '__main__':
    print('Beginning Sell Bot...')
    time.sleep(3)
    while not stop:
        getData()
        if stop:
            break
        sellItem()
    print('Sell Bot Complete!')
