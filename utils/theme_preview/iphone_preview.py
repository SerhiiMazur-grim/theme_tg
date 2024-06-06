import os

from PIL import Image, ImageDraw, ImageFont

from config import water_mark_text
from .hex_to_rgba_convert import HexColorToRgba
from .crop_wallpaper import CropWallpaper
from .ios_theme_layers.iphone_loaded_layers import IPHONE_IMAGE_LAYER_LIST


class CreateIphonePreview(HexColorToRgba, CropWallpaper):
    
    async def _colored_iphone_layers(self, images, colors):
        layers = []
        for image, color in zip(images, colors):
            img_data = image['img_data']
            alpha_channel = image['alpha']

            if len(color) == 4:
                new_img_data = [
                    (color[0], color[1], color[2],  color[3]) if alpha > 0 else pixel
                    for pixel, alpha in zip(img_data, alpha_channel)
                ]
            else:
                new_img_data = [
                (color[0], color[1], color[2],  alpha) if alpha > 0 else pixel
                for pixel, alpha in zip(img_data, alpha_channel)
                ]

            new_img = Image.new("RGBA", image['size'])
            new_img.putdata([tuple(p) for p in new_img_data])
            layers.append(new_img)

        return layers
    
    async def create_ios_preview(self, bot_username, chat_id, photo, preview_bg, bg, primary_txt,
                              secondary_txt, chat_in):
        watermark = water_mark_text(bot_username)
        background = Image.new('RGB', (1088, 1088), 'white')

        layers = []
        wallpaper = await self._crop_wallpaper(photo)
        images = IPHONE_IMAGE_LAYER_LIST.copy()
        
        colors = await self._hex_color_to_rgba([
            preview_bg,
            bg,
            bg,
            chat_in,
            primary_txt,
            secondary_txt,
            chat_in
        ])

        
        assets = await self._colored_iphone_layers(images, colors)
        layers.extend(i for i in assets)
        
        background.paste(wallpaper, (45, 155))
        
        for layer in layers:
            background.paste(layer, (0, 0), layer)
        
        with Image.open(os.path.join('utils', 'theme_preview', 'ios_theme_layers', 'user_icons.png')) as img:
            background.paste(img, (0, 0), img)
        
        draw = ImageDraw.Draw(background)
        font = ImageFont.truetype("arial.ttf", 20)
        text_color = colors[1]
        position = (40, 1025)

        draw.text(position, watermark, font=font, fill=text_color)
        
        preview = os.path.join('src', 'users_data', str(chat_id), 'preview.jpg')
        
        background.save(preview)
        
        return preview
