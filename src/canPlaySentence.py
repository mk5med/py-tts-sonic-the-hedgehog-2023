import typing


class State(typing.TypedDict):
    oldSentence: str
    sentenceIsStableCount: int


def canPlaySentence(state: State, sentence: str):
    """
    Detects if the incoming sentence is changing

    Returns a new state and True/False if the sentence can be played

    `(newState, play)`
    """

    # Copy the object to remove the reference
    state = state.copy()

    sentenceMatchesOld = state["oldSentence"] == sentence

    # The sentence is changing
    if not sentenceMatchesOld:
        # Record the change
        state["oldSentence"] = sentence
        state["sentenceIsStableCount"] = 0
        return (state, False)

    state["sentenceIsStableCount"] += 1

    # If sentenceIsStableCount is less than 2 the sentence is new and might change
    # If sentenceIsStableCount is 3 the sentence will be read
    # Otherwise the sentence has been read and will be skipped
    if state["sentenceIsStableCount"] < 2 or state["sentenceIsStableCount"] != 3:
        # Increment a flag
        return (state, False)

    return (state, True)
