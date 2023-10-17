import pyttsx3 as tts
import re
import time

from src.getBoundingBox import getBoundingBox
from src.getText import getText

cleanRegex = re.compile("([A-Za-z\\d\\s&.,\"'\\n])+")


def main():
    # Get the location of the games text
    boundingBox = getBoundingBox()

    if boundingBox is None:
        print("Bounding box not found")
        exit(0)

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

        print("Read: ", sentence)
        if len(sentence) != 0:
            engine.say(sentence)
            engine.runAndWait()
            engine.stop()
        time.sleep(2)


if __name__ == "__main__":
    main()
