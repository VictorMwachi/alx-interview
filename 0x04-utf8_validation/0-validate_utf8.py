#!/usr/bin/python3
"""0. UTF-8 Validation """


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding."""
    if False in [num > -1 and num <= 255 for num in data]:
        return False
    else:
        return True
