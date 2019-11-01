"""Example functions on arrays and strings"""

import string
import numpy as np


def increment(x):
    """adds 1 to x"""
    return(x+1)


def strip_punctiuation(text):
    """strips punctuations"""
    exclude = string.punctuation
    return ''.join(s for s in text if s not in exclude)