# import os
# from PIL import Image


# PC_PATH = ('utils', 'theme_preview', 'pc_theme_layers')
# PC_USER_ICON_LIST = []
# PC_IMAGE_LAYER_LIST = []


# with Image.open(os.path.join(*PC_PATH, 'user_icon_1.png')) as img:
#     USER_ICON_1 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     PC_USER_ICON_LIST.append(USER_ICON_1)
    
# with Image.open(os.path.join(*PC_PATH, 'user_icon_2.png')) as img:
#     USER_ICON_2 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     PC_USER_ICON_LIST.append(USER_ICON_2)
    
# with Image.open(os.path.join(*PC_PATH, 'user_icon_3.png')) as img:
#     USER_ICON_3 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     PC_USER_ICON_LIST.append(USER_ICON_3)
    
# with Image.open(os.path.join(*PC_PATH, 'user_icon_4.png')) as img:
#     USER_ICON_4 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     PC_USER_ICON_LIST.append(USER_ICON_4)
    
# with Image.open(os.path.join(*PC_PATH, 'user_icon_5.png')) as img:
#     USER_ICON_5 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     PC_USER_ICON_LIST.append(USER_ICON_5)
    
# with Image.open(os.path.join(*PC_PATH, 'user_icon_6.png')) as img:
#     USER_ICON_6 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     PC_USER_ICON_LIST.append(USER_ICON_6)
    
# with Image.open(os.path.join(*PC_PATH, 'user_icon_7.png')) as img:
#     USER_ICON_7 = {
#         'size': img.size,
#         'alpha': img.split()[3]
#     }
#     PC_USER_ICON_LIST.append(USER_ICON_7)
    

# with Image.open(os.path.join(*PC_PATH, 'img_bg.png')) as image:
#     IMAGE_LAYER_1 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_1)
    
# with Image.open(os.path.join(*PC_PATH, 'chat_bg.png')) as image:
#     IMAGE_LAYER_2 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_2)
    
# with Image.open(os.path.join(*PC_PATH, 'side_bar.png')) as image:
#     IMAGE_LAYER_3 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_3)
    
# with Image.open(os.path.join(*PC_PATH, 'selected_chat.png')) as image:
#     IMAGE_LAYER_4 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_4)
    
# with Image.open(os.path.join(*PC_PATH, 'clouds_in.png')) as image:
#     IMAGE_LAYER_5 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_5)
    
# with Image.open(os.path.join(*PC_PATH, 'clouds_out.png')) as image:
#     IMAGE_LAYER_6 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_6)
    
# with Image.open(os.path.join(*PC_PATH, 'prime_txt.png')) as image:
#     IMAGE_LAYER_7 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_7)
    
# with Image.open(os.path.join(*PC_PATH, 'secondary_txt.png')) as image:
#     IMAGE_LAYER_8 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_8)
    
# with Image.open(os.path.join(*PC_PATH, 'shadows.png')) as image:
#     IMAGE_LAYER_9 = {
#         'img_data': list(image.getdata()),
#         'alpha': list(image.split()[3].getdata()),
#         'size': image.size
#     }
#     PC_IMAGE_LAYER_LIST.append(IMAGE_LAYER_9)


import os
from PIL import Image

PC_PATH = ('utils', 'theme_preview', 'pc_theme_layers')
PC_USER_ICON_FILES = [
    'user_icon_1.png', 'user_icon_2.png', 'user_icon_3.png',
    'user_icon_4.png', 'user_icon_5.png', 'user_icon_6.png',
    'user_icon_7.png'
]

PC_IMAGE_LAYER_FILES = [
    'img_bg.png', 'chat_bg.png', 'side_bar.png', 'selected_chat.png',
    'clouds_in.png', 'clouds_out.png', 'prime_txt.png', 'secondary_txt.png',
    'shadows.png'
]

PC_USER_ICON_LIST = []
PC_IMAGE_LAYER_LIST = []

# Завантаження користувацьких іконок
for filename in PC_USER_ICON_FILES:
    with Image.open(os.path.join(*PC_PATH, filename)) as img:
        user_icon = {
            'size': img.size,
            'alpha': img.split()[3]
        }
        PC_USER_ICON_LIST.append(user_icon)

# Завантаження шарів зображень
for filename in PC_IMAGE_LAYER_FILES:
    with Image.open(os.path.join(*PC_PATH, filename)) as image:
        img_data = (pixel for pixel in image.getdata())
        alpha = (pixel for pixel in image.split()[3].getdata())
        image_layer = {
            'img_data': img_data,
            'alpha': alpha,
            'size': image.size
        }
        PC_IMAGE_LAYER_LIST.append(image_layer)

