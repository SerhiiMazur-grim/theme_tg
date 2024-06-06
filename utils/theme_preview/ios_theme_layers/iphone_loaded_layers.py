import os

from PIL import Image


IPHONE_PATH = ('utils', 'theme_preview', 'ios_theme_layers')
IPHONE_IMAGE_LAYER_LIST = []


with Image.open(os.path.join(*IPHONE_PATH, 'bg.png')) as image:
    IMAGE_LAYER_1 = {
        'img_data': list(image.getdata()),
        'alpha': list(image.split()[3].getdata()),
        'size': image.size
    }
    IPHONE_IMAGE_LAYER_LIST.append(IMAGE_LAYER_1)
    
with Image.open(os.path.join(*IPHONE_PATH, 'bg_chat_color_2.png')) as image:
    IMAGE_LAYER_2 = {
        'img_data': list(image.getdata()),
        'alpha': list(image.split()[3].getdata()),
        'size': image.size
    }
    IPHONE_IMAGE_LAYER_LIST.append(IMAGE_LAYER_2)
    
with Image.open(os.path.join(*IPHONE_PATH, 'message_clouds_out.png')) as image:
    IMAGE_LAYER_3 = {
        'img_data': list(image.getdata()),
        'alpha': list(image.split()[3].getdata()),
        'size': image.size
    }
    IPHONE_IMAGE_LAYER_LIST.append(IMAGE_LAYER_3)
    
with Image.open(os.path.join(*IPHONE_PATH, 'message_clouds_in.png')) as image:
    IMAGE_LAYER_4 = {
        'img_data': list(image.getdata()),
        'alpha': list(image.split()[3].getdata()),
        'size': image.size
    }
    IPHONE_IMAGE_LAYER_LIST.append(IMAGE_LAYER_4)
    
with Image.open(os.path.join(*IPHONE_PATH, 'prime_txt.png')) as image:
    IMAGE_LAYER_5 = {
        'img_data': list(image.getdata()),
        'alpha': list(image.split()[3].getdata()),
        'size': image.size
    }
    IPHONE_IMAGE_LAYER_LIST.append(IMAGE_LAYER_5)
    
with Image.open(os.path.join(*IPHONE_PATH, 'second_txt.png')) as image:
    IMAGE_LAYER_6 = {
        'img_data': list(image.getdata()),
        'alpha': list(image.split()[3].getdata()),
        'size': image.size
    }
    IPHONE_IMAGE_LAYER_LIST.append(IMAGE_LAYER_6)
    
with Image.open(os.path.join(*IPHONE_PATH, 'shadow.png')) as image:
    IMAGE_LAYER_7 = {
        'img_data': list(image.getdata()),
        'alpha': list(image.split()[3].getdata()),
        'size': image.size
    }
    IPHONE_IMAGE_LAYER_LIST.append(IMAGE_LAYER_7)
