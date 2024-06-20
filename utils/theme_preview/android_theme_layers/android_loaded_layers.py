# import os

# from PIL import Image


# ANDROID_PATH = ('utils', 'theme_preview', 'android_theme_layers')
# ANDROID_USER_ICON_LIST = []
# ANDROID_IMAGE_LAYER_LIST = []


# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_1.png')) as img:
#     USER_ICON_1 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_1)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_2.png')) as img:
#     USER_ICON_2 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_2)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_3.png')) as img:
#     USER_ICON_3 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_3)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_4.png')) as img:
#     USER_ICON_4 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_4)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_5.png')) as img:
#     USER_ICON_5 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_5)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_6.png')) as img:
#     USER_ICON_6 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_6)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_7.png')) as img:
#     USER_ICON_7 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_7)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'user_icon_8.png')) as img:
#     USER_ICON_8 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     ANDROID_USER_ICON_LIST.append(USER_ICON_8)


# with Image.open(os.path.join(*ANDROID_PATH, 'bg.png')) as image:
#     IMAGE_LAYER_1 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     ANDROID_IMAGE_LAYER_LIST.append(IMAGE_LAYER_1)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'bg_chat_color_2.png')) as image:
#     IMAGE_LAYER_2 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     ANDROID_IMAGE_LAYER_LIST.append(IMAGE_LAYER_2)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'message_clouds_out.png')) as image:
#     IMAGE_LAYER_3 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     ANDROID_IMAGE_LAYER_LIST.append(IMAGE_LAYER_3)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'message_clouds_in.png')) as image:
#     IMAGE_LAYER_4 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     ANDROID_IMAGE_LAYER_LIST.append(IMAGE_LAYER_4)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'prime_txt.png')) as image:
#     IMAGE_LAYER_5 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     ANDROID_IMAGE_LAYER_LIST.append(IMAGE_LAYER_5)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'second_txt.png')) as image:
#     IMAGE_LAYER_6 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     ANDROID_IMAGE_LAYER_LIST.append(IMAGE_LAYER_6)
    
# with Image.open(os.path.join(*ANDROID_PATH, 'shadow.png')) as image:
#     IMAGE_LAYER_7 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     ANDROID_IMAGE_LAYER_LIST.append(IMAGE_LAYER_7)


import os
from PIL import Image

ANDROID_PATH = ('utils', 'theme_preview', 'android_theme_layers')
ANDROID_USER_ICON_FILES = [
    'user_icon_1.png', 'user_icon_2.png', 'user_icon_3.png', 'user_icon_4.png',
    'user_icon_5.png', 'user_icon_6.png', 'user_icon_7.png', 'user_icon_8.png'
]
ANDROID_IMAGE_LAYER_FILES = [
    'bg.png', 'bg_chat_color_2.png', 'message_clouds_out.png', 'message_clouds_in.png',
    'prime_txt.png', 'second_txt.png', 'shadow.png'
]

ANDROID_USER_ICON_LIST = []
ANDROID_IMAGE_LAYER_LIST = []

# Завантаження користувацьких іконок
for filename in ANDROID_USER_ICON_FILES:
    with Image.open(os.path.join(*ANDROID_PATH, filename)) as img:
        user_icon = {
            'size': img.size,
            'alpha': img.split()[3]
        }
        ANDROID_USER_ICON_LIST.append(user_icon)

# Завантаження шарів зображень
for filename in ANDROID_IMAGE_LAYER_FILES:
    with Image.open(os.path.join(*ANDROID_PATH, filename)) as image:
        img_data = list(image.getdata())
        alpha = list(image.split()[3].getdata())
        image_layer = {
            'img_data': (pixel for pixel in img_data),
            'alpha': (pixel for pixel in alpha),
            'size': image.size
        }
        ANDROID_IMAGE_LAYER_LIST.append(image_layer)


