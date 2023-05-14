#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """Return a length of the string and its first characters."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
