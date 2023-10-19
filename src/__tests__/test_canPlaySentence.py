from src.canPlaySentence import canPlaySentence


def test_sentenceIsChanging_newText():
    (newState, shouldPlay) = canPlaySentence(
        dict(oldSentence="", sentenceIsStableCount=0), ""
    )
    assert not shouldPlay
    assert newState["oldSentence"] == ""
    assert newState["sentenceIsStableCount"] == 1


def test_sentenceIsChanging_readyToReadText():
    (newState, shouldPlay) = canPlaySentence(
        dict(oldSentence="sample", sentenceIsStableCount=2), "sample"
    )
    assert shouldPlay
    assert newState["oldSentence"] == "sample"
    assert newState["sentenceIsStableCount"] == 3


def test_sentenceIsChanging_blocksOldText():
    (newState, shouldPlay) = canPlaySentence(
        dict(oldSentence="sample", sentenceIsStableCount=3), "sample"
    )
    assert not shouldPlay
    assert newState["oldSentence"] == "sample"
    assert newState["sentenceIsStableCount"] == 4


def test_sentenceIsChanging_resetsWhenTextChanges():
    (newState, shouldPlay) = canPlaySentence(
        dict(oldSentence="sample", sentenceIsStableCount=3), "newSample"
    )
    assert not shouldPlay
    assert newState["oldSentence"] == "newSample"
    assert newState["sentenceIsStableCount"] == 0
