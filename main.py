import pyttsx3 as tts
import re
import time
import pyautogui as pyg
from src.getBoundingBox import getBoundingBox
from src.getText import getText

cleanRegex = re.compile("([A-Za-z\\d\\s&.,\"'\\n])+")


def printHeader():
    print("-" * 20)
    print("Ready to go! Select 'NEW GAME' or 'CONTINUE'")
    print("-" * 20)


def takeDebugScreenshot(fileName: str):
    fileName += ".png"
    pyg.screenshot().save(fileName)
    print(f"Saved a debug screenshot to '{fileName}'")


def main():
    # Get the location of the games text
    boundingBox = getBoundingBox()

    if boundingBox is None:
        print(
            "Bounding box not found. Is the game open to the loading screen and visible?"
        )

        # Take a screenshot
        takeDebugScreenshot("debug_screenshot")

        exit(1)

    printHeader()
    # Initialise the engine
    engine = tts.init()

    oldSentence = ""
    sentenceIsStableCount = 0

    while True:
        sentence = getText(boundingBox)
        sentenceMatchesOld = oldSentence == sentence

        # The sentence is changing
        if not sentenceMatchesOld:
            # Record the change
            oldSentence = sentence
            sentenceIsStableCount = 0
            continue

        sentenceIsStableCount += 1

        # If sentenceIsStableCount is less than 2 the sentence is new and might change
        # If sentenceIsStableCount is 3 the sentence will be read
        # Otherwise the sentence has been read and will be skipped
        if sentenceIsStableCount < 2 or sentenceIsStableCount != 3:
            # Increment a flag
            sentenceIsStableCount += 1
            continue

        if len(sentence) != 0:
            print("Read: ", sentence)
            engine.say(sentence)
            engine.runAndWait()
            engine.stop()
        else:
            print("No text read")
        time.sleep(2)


if __name__ == "__main__":
    main()
