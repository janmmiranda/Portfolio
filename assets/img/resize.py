import cv2
import numpy as np
import argparse
from PIL import Image

def resize(img):
	size = (1280, 720)
	vis = img.copy()
	im = Image.fromarray(vis)
	new = im.resize(size,Image.ANTIALIAS)
	new = np.array(new)

	return new

def inputImg():
	parser = argparse.ArgumentParser()
	parser.add_argument("image")
	args = parser.parse_args()
	image_file = str(args.image)
	img = cv2.imread(image_file)
	return img, image_file

def main():
	img, name = inputImg()

	resized = resize(img)
	cv2.imwrite("new%s" %name, resized)

main()