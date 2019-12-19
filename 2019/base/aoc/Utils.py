import colorama

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
    colorama.init(convert=True)
    block = u'\u2588' + colorama.Fore.RESET
    minRow = min(panel.keys(), key=lambda panel:panel[1])[1]
    maxRow = max(panel.keys(), key=lambda panel:panel[1])[1]
    minCol = min(panel.keys(), key=lambda panel:panel[0])[0]
    maxCol = max(panel.keys(), key=lambda panel:panel[0])[0]

    drawing = ""
    for row in range(minRow, maxRow+1):
        for col in range(minCol, maxCol+1):
            char = panel.get((col, row), defaultChar)
            if char in colors:
                char = colors.get(char) + block
            drawing += char
        drawing += "\n"
    print(drawing)
