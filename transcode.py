from sys import stdin

input_character = None
while input_character != '':
    input_character = stdin.read(1)
    input_character = transcode_character(input_character)
    print(input_character, end='')

def transcode_character(character):
    return character
