import re
import time
import typing
import pyttsx3 as tts
from canPlaySentence import canPlaySentence
from src.getBoundingBox import getBoundingBox
from src.getText import getText
from src.debug import takeDebugScreenshot

cleanRegex = re.compile("([A-Za-z\\d\\s&.,\"'\\n])+")


def printReadyHeader():
    """
    Print a header that the user can continue playing the game
    """

    print("-" * 20)
    print("Ready to go! Select 'NEW GAME' or 'CONTINUE'")
    print("-" * 20)


def trySpeakSentence(sentence: str, engine: tts.Engine):
    if len(sentence) != 0:
        print("Read: ", sentence)
        engine.say(sentence)
        engine.runAndWait()
        engine.stop()
    else:
        print("No text read")


def mainLoop(boundingBox: typing.Tuple[int, int, int, int], engine: tts.Engine):
    """
    Main processing loop for TTS
    """
    shouldSkipState = {"oldSentence": "", "sentenceIsStableCount": 0}

    while True:
        sentence = getText(boundingBox)
        (_newState, play) = canPlaySentence(shouldSkipState, sentence)
        shouldSkipState = _newState

        if not play:
            continue

        trySpeakSentence(sentence, engine)
        time.sleep(2)


def main():
    """
    Entry point
    """

    # Get the location of the games text
    boundingBox = getBoundingBox()

    if boundingBox is None:
        print(
            "Bounding box not found. Is the game open to the loading screen and visible?"
        )

        # Take a screenshot
        takeDebugScreenshot("debug_screenshot")

        exit(1)

    printReadyHeader()

    # Initialise the engine
    engine = tts.init()
    mainLoop(boundingBox, engine)


if __name__ == "__main__":
    main()
