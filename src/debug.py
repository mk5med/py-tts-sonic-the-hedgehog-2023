import pyautogui as pyg


def takeDebugScreenshot(fileName: str, verbose=True):
    """
    Takes a screenshot of the entire screen and save it to `fileName`.png

    Used for debugging why the program is not detecting the loading screen
    """

    fileName += ".png"
    pyg.screenshot().save(fileName)
    if verbose:
        print(f"Saved a debug screenshot to '{fileName}'")
