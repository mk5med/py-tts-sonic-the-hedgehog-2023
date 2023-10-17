import pytesseract
from PIL import ImageGrab
import typing
import os

# Check that the debug mode flag exists
__DEBUG_MODE__ = str(os.getenv("DEBUG")).lower() == "true"


def getText(imageBoundingBox: typing.Tuple[int, int, int, int]) -> str:
    img = ImageGrab.grab(bbox=imageBoundingBox)
    if __DEBUG_MODE__:
        img.save("debug_getText.png")

    readText: str = pytesseract.image_to_string(img)

    # Fix common bugs
    readText = readText.replace("|", "I").strip()
    return readText
