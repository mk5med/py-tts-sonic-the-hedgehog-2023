import cv2
import pyautogui as pyg


def getBoundingBox():
    """
    Gets the bounding box of the text area for the game
    """
    # Read the calibration image
    _img = cv2.imread("baseimg.png")

    # Find the calibration image on the screen
    posInfo = pyg.locateOnScreen(_img, minSearchTime=1)

    # Take a screenshot
    img = pyg.screenshot()
    img.save("out.png")

    if posInfo is not None:
        left = posInfo.left - 1700
        right = img.width - posInfo.width
        top = posInfo.top + 100
        bottom = posInfo.top + posInfo.height * 1.5
        return (left, top, right, bottom)
    else:
        return None
