from tkinter import *
from PIL import Image, ImageTk
import requests

def imagedisplay(data, day):
	img_url = data[day]['icon_url']
	img = requests.get(img_url)
	img_name = day + '.png'
	if img.status_code==200:
		with open(img_name,'wb') as image_file:
			image_file.write(img.content)
