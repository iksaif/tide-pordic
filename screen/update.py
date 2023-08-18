import sys
import logging
import requests
import argparse
import PIL

import epd7in5_V2

def setup_logging():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)

def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--image")
    parser.add_argument("--dry-run", action="store_true")
    return parser.parse_args(args)

def init_screen(dry_run=False):
    logging.info("Init screen")
    if dry_run:
        return None
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()
    return epd

def write_to_screen(epd, image):
    logging.info("Writing to screen...")
    width, height = (800, 480)
    if epd:
        width, height = epd.width, epd.height

    h_image = PIL.Image.new('1', (width, height), 255)
    bmp = PIL.Image.open(image)

    h_image.paste(bmp, (0, 0))

    if epd:
        epd.init()
        epd.display(epd.getbuffer(h_image))
        epd.sleep()

def close():
    print("close")
    epd7in5_V2.epdconfig.module_exit()
    exit()

def main():
    args = parse_args(sys.argv[1:])
    setup_logging()
    image = args.image
    edp = init_screen(args.dry_run)
    write_to_screen(edp, image)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        close()
