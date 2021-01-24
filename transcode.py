#!/usr/bin/env python3

import random

def read_mapping(filename):
    import csv
    with open (filename, newline ='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        ct = dict()
        for row in reader:
            row_len = len(row)
            for i in range(0, row_len, 2):
                key = row[i]
                value = row[i + 1]
                if key != '':
                    ct[key] = value
        return ct

def transcode_character(character, mapping_dict):
        return mapping_dict.get(character, character)

def should_transcode(randomness):
    return random.choices((True, False), weights=(1, randomness - 1))[0]

if __name__ == '__main__':
    import sys
    from sys import stdin

    mapping_file = sys.argv[1]
    mapping_dict = read_mapping(mapping_file)

    randomness = int(sys.argv[2])

    input_character = None
    while input_character != '':
        input_character = stdin.read(1)
        output_character = (transcode_character(input_character, mapping_dict)
                            if should_transcode(randomness)
                            else input_character)
        print(output_character, end='')
