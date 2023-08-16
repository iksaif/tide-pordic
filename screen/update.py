import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

from PIL import Image

import epd7in5_V2

def init_screen():
    print("init")
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()
    return epd

def write_to_screen(epd):
    print("write")
    h_image = Image.new('1', (epd.width, epd.height), 255)
    bmp = Image.open("screen.bmp")
    h_image.paste(bmp, (0, 0))

    epd.init()
    epd.display(epd.getbuffer(h_image))
    epd.sleep()


def close():
    print("close")
    epd7in5_V2.epdconfig.module_exit()
    exit()

def main():
    edp = init_screen()
    write_to_screen(edp)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close()
