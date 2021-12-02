import time
import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI 
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
lsm303 = Adafruit_LSM303.LSM303()
# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

yvalue = 0
xvalue = 0
size = 3
# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
while True:
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    font = ImageFont.load_default()
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    xvalue = (accel_x/33) + 32
    yvalue = (accel_y/33) + 64
    draw.text((1, 1), 'X,Y Accel display:', font=font, fill=255)
    draw.text((1, 31), 'X'+ str(round(accel_x/107, 3)), font=font, fill=255)
    draw.text((64,54), 'Y'+ str(round(accel_y/107, 3)), font=font, fill=255)
    draw.ellipse((xvalue/2+(48-size),yvalue/2+(5-size),xvalue/2+(48+size),yvalue/2+(5+size)), outline=255, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    # Wait half a second and repeat.
    time.sleep(0.01)
