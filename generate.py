#!/usr/bin/python

"""
Generate font files based on Comic Shanns font.

based on -> Comic Mono generate.py:
https://github.com/dtinth/comic-mono-font/blob/master/generate.py
"""

import os
import re
import sys

import fontforge
import psMat
import unicodedata


def flip_glyphs():
    #font = fontforge.open('comic-family/comic-shanns.ttf')
    # I found it easier to just work with comic mono instead
    font = fontforge.open('comic-family/comic-mono.ttf')

    font.selection.all()
    font.transform(psMat.scale(-1, 1))  # where magic happens

    font.familyname = 'Comic snnahS'
    font.version = '0.0.1'
    font.comment = 'https://github.com/z3tr/comic-snnahs'
    font.copyright = 'https://github.com/m5tfi/comic-snnahs/blob/master/LICENSE'

    font.fontname = 'Comic-snnahS'
    font.fullname = 'Comic snnahS'
    font.generate('Comic-snnahS.ttf')

    font.selection.all()
    font.fontname = 'Comic-snnahS-dlob'
    font.fullname = 'Comic snnahS dlob'
    font.weight = 'Bold'
    font.changeWeight(64)
    font.generate('Comic-snnahS-dlob.ttf')


if __name__ == "__main__":
    print('Script started ...')

    flip_glyphs()

    print('Done!')
