import colorama

def drawPanel(panel, colors, defaultColor=0):
    block = u'\u2588'
    minRow = min(panel.keys(), key=lambda panel:panel[1])[1]
    maxRow = max(panel.keys(), key=lambda panel:panel[1])[1]
    minCol = min(panel.keys(), key=lambda panel:panel[0])[0]
    maxCol = max(panel.keys(), key=lambda panel:panel[0])[0]

    drawing = ""
    for row in range(minRow, maxRow+1):
        for col in range(minCol, maxCol+1):
            color = colors[panel.get((col, row), defaultColor)]
            drawing += color + block
        drawing += "\n"
    print(drawing)