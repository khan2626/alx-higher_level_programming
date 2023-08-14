#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """returns length and first character of tuple"""
    str_size = len(sentence)
    for char in sentence:
        if len(sentence) == 0:
            return(0, None)
        else:
            return(len(sentence), sentence[0])
        
