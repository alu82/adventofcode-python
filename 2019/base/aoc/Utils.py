import colorama
import os

def drawPanel(panel, colors, defaultColor=0):
    colorama.init(convert=True)
    block = u'\u2588'
    minRow = min(panel.keys(), key=lambda panel:panel[1])[1]
    maxRow = max(panel.keys(), key=lambda panel:panel[1])[1]
    minCol = min(panel.keys(), key=lambda panel:panel[0])[0]
    maxCol = max(panel.keys(), key=lambda panel:panel[0])[0]

    drawing = ""
    for row in range(minRow, maxRow+1):
        for col in range(minCol, maxCol+1):
            colorKey = panel.get((col, row), defaultColor)
            color = colors.get(colorKey, colors[defaultColor])
            drawing += color + block
        drawing += "\n"
    print(drawing)

def drawMixPanel(panel, colors={}, defaultChar=' '):
    if str.lower(os.name) != 'posix':
        colorama.init(convert=True)
    block = u'\u2588' + colorama.Fore.RESET
    minRow = min(panel.keys(), key=lambda panel:panel[1])[1]
    maxRow = max(panel.keys(), key=lambda panel:panel[1])[1]
    minCol = min(panel.keys(), key=lambda panel:panel[0])[0]
    maxCol = max(panel.keys(), key=lambda panel:panel[0])[0]

    drawing = ""
    for row in range(minRow, maxRow+1):
        for col in range(minCol, maxCol+1):
            char = str(panel.get((col, row), defaultChar))
            if char in colors:
                char = colors.get(char) + block
            drawing += char
        drawing += "\n"
    print(drawing)

def drawAsciiPanel(panel, colors={}, default=32):
    minRow = min(panel.keys(), key=lambda panel:panel[1])[1]
    maxRow = max(panel.keys(), key=lambda panel:panel[1])[1]
    minCol = min(panel.keys(), key=lambda panel:panel[0])[0]
    maxCol = max(panel.keys(), key=lambda panel:panel[0])[0]

    drawing = ""
    for row in range(minRow, maxRow+1):
        for col in range(minCol, maxCol+1):
            value = panel.get((col, row), default)
            if value <= 1114111:
                char = chr(value)
            else:
                char = str(value)
            drawing += char
        drawing += "\n"
    print(drawing)
