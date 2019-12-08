import os
import colorama

# Preparation            
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")
input = inputFile.readline()

width=25
height=6
layerSize=width*height

layers=[]
startIndex=0
endIndex=layerSize
while endIndex<len(input)+1:
    layers.append(input[startIndex:endIndex])
    startIndex+=layerSize
    endIndex+=layerSize

# Part 1

result=-1
minZeros=layerSize+1
for layer in layers:
    currentZeros = layer.count('0')
    if currentZeros<minZeros:
        minZeros=currentZeros
        result=layer.count('1') * layer.count('2')

print(result)


# Part 2

picture=[]
for i in range(layerSize):
    picture.append('2')

for layer in layers:
    for i, pixel in enumerate(layer):
        if picture[i]=='2':
            picture[i]=pixel

encodedPicture = ""
for i in range(height):
    pixelRow = ''.join(picture[i*width:(i+1)*width])
    pixelRow = pixelRow.replace('0', 'X')
    pixelRow = pixelRow.replace('1', ' ')
    pixelRow = pixelRow.replace('2', ' ')
    encodedPicture += pixelRow + "\n"

print(encodedPicture)

encodedPicture = ""
block = u'\u2588'
colors = {
    '0': colorama.Fore.BLACK,
    '1': colorama.Fore.WHITE,
    '2': colorama.Fore.YELLOW # some other color for transparent
}

for i, pixel in enumerate(picture):
    coloredPixel = colors[pixel] + block
    encodedPicture += coloredPixel + ("\n" if (i+1)%width==0 else "")

print(encodedPicture)






