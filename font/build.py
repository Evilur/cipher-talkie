import sys
from PIL import Image
from pathlib import Path

##################
# CONFIG SECTION #
##################

# Set the font size
swidth, sheight = 7, 8
bwidth, bheight = 0, 0

# Set the spacing: top, right, bottom, left
sspacing = [ 1, 1, 0, 1 ]

######################
# END CONFIG SECTION #
######################

# Validate the config
if sheight > 8:
    print('Error: regular font height can not be more than 8', file=sys.stderr)
    print('Aborting', file=sys.stderr)
    exit(-1)

# Get the sctipt directory
script_dir = Path(__file__).resolve().parent

# Read the regular image
simage = Image.open(str(script_dir) + '/regular.jpg', 'r').convert('L')
spixels = simage.load()
if spixels is None:
    print('Error: can\'t open the regular.jpg', file=sys.stderr)
    print('Aborting', file=sys.stderr)
    exit(-1)

# Loop through the regular symbols
char = 32  # The number of the first element in the ASCII table
for y in range(0, simage.height, sheight + 1 + sspacing[0] + sspacing[2]):
    for x in range(0, simage.width, swidth + 1 + sspacing[1] + sspacing[3]):
        # Init the byte array
        bytearr = []

        # Get the bytes array
        for xoff in range(sspacing[3], sspacing[3] + swidth):
            # Init the byte
            byte = 0

            # Get the byte
            for yoff in range(sspacing[0], sspacing[0] + sheight):
                pixel = spixels[x + xoff, y + yoff]
                bit = int(pixel < 128) # type: ignore
                byte = (byte << 1) | bit

            # Add the byte to the byte array
            bytearr += [ byte ]

        # Increase the char number in the ASCII table
        char += 1

        # Check for the last element
        if char > 126: break
        print(char, bytearr)
