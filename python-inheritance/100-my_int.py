#!/usr/bin/python3
"""Module that defines a rebel integer class MyInt"""


class MyInt(int):
    """MyInt is a rebel: == and != are inverted"""

    def __eq__(self, other):
        """Inverts == operator"""
        return int(self) != other

    def __ne__(self, other):
        """Inverts != operator"""
        return int(self) == other
