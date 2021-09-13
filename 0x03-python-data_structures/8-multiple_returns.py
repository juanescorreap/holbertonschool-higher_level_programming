#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence:
        letter = sentence[0]
    else:
        letter = None
    tuple_8 = (length, letter)
    return(tuple_8)
