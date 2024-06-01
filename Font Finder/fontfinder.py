from pygame import *
fonts = font.get_fonts()

def findfont(font):
    pos = 0
    while pos < len(fonts)-1:
        if fonts[pos] == font:
            return(pos,font)
        else:
            pos = -1
            return(pos)
        pos = pos + 1

print(findfont(''))