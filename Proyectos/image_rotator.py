from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('input_file')
parser.add_argument('output_file')
parser.add_argument('--angle', '-a', type=int, default=90)
parser.add_argument('-i', '--info', action='store_true')

args = parser.parse_args()

im = Image.open(args.input_file)

if args.info:
    print('dimensiones de la imagen de entrada:', im.size)

rotated = im.rotate(args.angle)

rotated.save(args.output_file)
rotated.show()