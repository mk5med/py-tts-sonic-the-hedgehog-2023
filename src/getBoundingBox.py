import cv2
import pyautogui as pyg


def getBoundingBox():
    """
    Gets the bounding box of the text area for the game
    """
    # Read the calibration image
    _img = cv2.imread("loading_screen.png")

    # Find the calibration image on the screen
    posInfo = pyg.locateOnScreen(_img, minSearchTime=1)

    writableArea = 0.9

    if posInfo is not None:
        left = posInfo.left
        right = left + posInfo.width * writableArea
        top = posInfo.top + posInfo.height // 4 * 3 + 80
        bottom = top + posInfo.height // 4 - 80
        return (left, top, right, bottom)
    else:
        return None
