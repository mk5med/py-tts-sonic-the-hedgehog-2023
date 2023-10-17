import pytesseract
from PIL import ImageGrab
import typing


def getText(imageBoundingBox: typing.Tuple[int, int, int, int]) -> str:
    img = ImageGrab.grab(bbox=imageBoundingBox)
    readText: str = pytesseract.image_to_string(img)

    # Fix common bugs
    readText = readText.replace("|", "I").strip()
    return readText
