#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def get_num_letters(text):
    nLetters = 0
    for c in text:
        nLetters += c.isalnum()

    return nLetters


def get_word_length_histogram(text):
    lines = text.split("\n")
    words = []
    for line in lines:
        words.extend(line.split(" "))

    hist = [0]
    currentMax = 0  # max word length supported
    for word in words:
        length = get_num_letters(word)
        if length > currentMax:
            for _ in range(length - currentMax):
                hist.append(0)

            currentMax = length

        hist[length] += 1

    return hist


def format_histogram(histogram):
    ROW_CHAR = "*"
    maxWidth = len(str(len(histogram) - 1))

    txt = ""
    length = 1
    for count in histogram[1:]:
        txt += f"{length:>{maxWidth}} " + ROW_CHAR * count + "\n"
        length += 1

    return txt.rstrip()


def format_horizontal_histogram(histogram):
    BLOCK_CHAR = "|"
    LINE_CHAR = "¯"

    height = 0
    for count in histogram:
        height = max(height, count)

    txtRows = []
    while height > 0:
        row = ""
        for i in range(1, len(histogram)):
            count  = histogram[i]

            if count == height:
                histogram[i] -= 1
                row += BLOCK_CHAR
            else:
                row += " "

        height -= 1
        txtRows.append(row)
    
    txtRows.append(LINE_CHAR * (len(histogram)-1))
    
    return "\n".join(txtRows)


if __name__ == "__main__":
    spam = "Stop right there criminal scum! shouted the guard confidently."
    eggs = get_word_length_histogram(spam)
    print(eggs, "\n")
    print(format_histogram(eggs), "\n")
    print(format_horizontal_histogram(eggs))
