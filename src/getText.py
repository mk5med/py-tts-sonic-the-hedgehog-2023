import pytesseract
import typing
import os
from PIL import ImageGrab
from src.debug import takeDebugScreenshot

# Check that the debug mode flag exists
__DEBUG_MODE__ = str(os.getenv("DEBUG")).lower() == "true"


def getText(imageBoundingBox: typing.Tuple[int, int, int, int]) -> str:
    img = ImageGrab.grab(bbox=imageBoundingBox)
    if __DEBUG_MODE__:
        takeDebugScreenshot("debug_getText", verbose=False)

    readText: str = pytesseract.image_to_string(img)

    # Fix common bugs
    readText = readText.replace("|", "I").strip()
    return readText
